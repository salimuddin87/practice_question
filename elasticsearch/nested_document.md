## Nested document in Elasticsearch
The **nested** type is a specialised version ot the [object](https://www.elastic.co/guide/en/elasticsearch/reference/current/object.html) 
data type that allows arrays of objects to be indexed in a way that they can be queried independently of each other.

### Using nested fields for arrays of objects
If you need to index arrays of objects and to maintain the independence of each object in the array, use the nested 
data type instead of the object data type.

Internally, nested objects index each object in the array as a separate hidden document, meaning that each nested 
object can be queried independently of the others with the nested query:
```
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "user": {
        "type": "nested"        #1 The user field is mapped as type nested instead of type object.
      }
    }
  }
}

PUT my-index-000001/_doc/1
{
  "group" : "fans",
  "user" : [
    {
      "first" : "John",
      "last" :  "Smith"
    },
    {
      "first" : "Alice",
      "last" :  "White"
    }
  ]
}

GET my-index-000001/_search
{
  "query": {
    "nested": {
      "path": "user",
      "query": {
        "bool": {
          "must": [
            { "match": { "user.first": "Alice" }},
            { "match": { "user.last":  "Smith" }}   #2 This query doesn't match because Alice and Smith are not in the same nested object.
          ]
        }
      }
    }
  }
}

GET my-index-000001/_search
{
  "query": {
    "nested": {
      "path": "user",
      "query": {
        "bool": {
          "must": [
            { "match": { "user.first": "Alice" }},
            { "match": { "user.last":  "White" }}   #3 This query matches because Alice and White are in the same nested object.
          ]
        }
      },
      "inner_hits": {       #4 it allow us to highlight the matching nested documents.
        "highlight": {
          "fields": {
            "user.first": {}
          }
        }
      }
    }
  }
}
```
Nested documents can be:
1. queried with the nested query.
2. analyzed with the nested and reverse_nested aggregations.
3. sorted with nested sorting.
4. retrieved and highlighted with nested inner hits.

Important:-
1. Because nested documents are indexed as separate documents, they can only be accessed within the scope of the nested 
query, the nested/reverse_nested aggregations, or nested inner hits.
2. For instance, if a string field within a nested document has index_options set to offsets to allow use of the 
postings during the highlighting, these offsets will not be available during the main highlighting phase. Instead, 
highlighting needs to be performed via nested inner hits. The same consideration applies when loading fields during 
a search through docvalue_fields or stored_fields.
