## parent-child relationships in Elasticsearch
The **join** data type is a special field that creates parent/child relation within documents of the same index.
```
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "my_id": {
        "type": "keyword"
      },
      "my_join_field": {    # The name for the field
        "type": "join",
        "relations": {
          "question": "answer"  # Defines a single relation where question is parent of answer.
        }
      }
    }
  }
}
```

To index a document with a join, the name of the relation and the optional parent of the document must be provided
in the **source**. For instance the following example creates two **parent** documents in the **question** context.
```
PUT my-index-000001/_doc/1?refresh
{
  "my_id": "1",
  "text": "This is a question",
  "my_join_field": {
    "name": "question"   # This document is a question document
  }
}

PUT my-index-000001/_doc/2?refresh
{
  "my_id": "2",
  "text": "This is another question",
  "my_join_field": {
    "name": "question"
  }
}
```

When indexing a child, the name of the relation as well as the parent id of the document must be added in the **source**.
For instance the following example shows how to index two **_child_** documents.
```
PUT my-index-000001/_doc/3?routing=1&refresh  # The routing value is mandatory because parent and child documents must be indexed on the same shard.
{
  "my_id": "3",
  "text": "This is an answer",
  "my_join_field": {
    "name": "answer",   # answer is the name of the join for this document
    "parent": "1"       # The parent id of this child document
  }
}

PUT my-index-000001/_doc/4?routing=1&refresh
{
  "my_id": "4",
  "text": "This is another answer",
  "my_join_field": {
    "name": "answer",
    "parent": "1"
  }
}
```

### Parent-join and performance
The join field shouldn’t be used like joins in a relation database. In Elasticsearch the key to good performance is to 
de-normalize your data into documents. Each join field, has_child or has_parent query adds a significant tax to your 
query performance. It can also trigger global ordinals to be built.

The only case where the join field makes sense is if your data contains a one-to-many relationship where one entity 
significantly outnumbers the other entity. An example of such case is a use case with products and offers for these 
products. In the case that offers significantly outnumbers the number of products then it makes sense to model the 
product as parent document and the offer as child document.

### Parent-join restrictions
* Only one join field mapping is allowed per index.
* Parent and child documents must be indexed on the same shard. This means that the same routing value needs to be 
provided when getting, deleting, or updating a child document.
* An element can have multiple children but only one parent.
* It is possible to add a new relation to an existing join field.
* It is also possible to add a child to an existing element but only if the element is already a parent.

### Searching with parent-join
The parent-join creates one field to index the name of the relation within the document (my_parent, my_child, …​).

It also creates one field per parent/child relation. The name of this field is the name of the join field followed by # 
and the name of the parent in the relation. So for instance for the my_parent → [my_child, another_child] relation, 
the join field creates an additional field named my_join_field#my_parent.

### Global ordinals
The join field uses **_global ordinals_** to speed up joins. Global ordinals need to be rebuilt after any change to a 
shard. The more parent id values are stored in a shard, the longer it takes to rebuild the global ordinals for the join 
field.

Global ordinals, by default, are built eagerly: if the index has changed, global ordinals for the join field will be 
rebuilt as part of the refresh. This can add significant time to the refresh. However most of the times this is the 
right trade-off, otherwise global ordinals are rebuilt when the first parent-join query or aggregation is used. This 
can introduce a significant latency spike for your users and usually this is worse as multiple global ordinals for the 
join field may be attempt rebuilt within a single refresh interval when many writes are occurring.

When the join field is used infrequently and writes occur frequently it may make sense to disable eager loading:
```
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "my_join_field": {
        "type": "join",
        "relations": {
           "question": "answer"
        },
        "eager_global_ordinals": false # disable global ordinals
      }
    }
  }
}
```

### Multiple children per parent
It is also possible to define multiple children for a single parent:
```
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "my_join_field": {
        "type": "join",
        "relations": {
          "question": ["answer", "comment"]  # question is parent of answer and comment
        }
      }
    }
  }
}
```

### Multiple levels of parent join
Multiple levels of parent/child:
```
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "my_join_field": {
        "type": "join",
        "relations": {
          "question": ["answer", "comment"],  # question is parent of answer and comment
          "answer": "vote"                    # answer is parent of vote
        }
      }
    }
  }
}
```

Indexing a grandchild document requires a routing value equals to the grand-parent (the greater parent of the lineage):
```
PUT my-index-000001/_doc/3?routing=1&refresh  # This child document must be on the same shard than its grand-parent and parent
{
  "text": "This is a vote",
  "my_join_field": {
    "name": "vote",
    "parent": "2"               # The parent id of this document(must points to an answer document)
  }
}
```
