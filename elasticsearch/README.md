## Elasticsearch 
Elasticsearch (ES) is a combination of open-source, distributed, highly scalable 
data store and Lucene- a search engine that supports extremely fast full-text search.

### Elasticsearch Components
#### Cluster
   One or more servers collectively providing indexing and search capabilities form an 
   Elasticsearch cluster. The cluster size can vary from a single node to thousands of nodes, 
   depending on the use cases.
#### Node 
   Node is a single physical or virtual machine that holds full or part of your data and 
   provides computing power for indexing and searching your data.Every node is identified with a 
   unique name. If the node identifier is not specified, a random UUID is assigned as a node 
   identifier at the startup. Every node configuration has the property `cluster.name`. The 
   cluster will be formed automatically with all the nodes having the same `cluster.name` at startup.
#### Data Node
   Data node is the node that has storage and computation capability. Data node 
   stores the part of data in the form of shards. Data nodes also participate in the CRUD, 
   search, and aggregate operation. These operations are resource-intensive, and hence, it is 
   a good practice to have dedicated data nodes without having the additional load of cluster 
   administration. By default, every node of the cluster is a data node.
#### Master Node
   Master nodes are reserved to perform administrative tasks. Master nodes track 
   the availability/failure of the data nodes. The master nodes are responsible for creating 
   and deleting the indices.By default, all the nodes are both data nodes as well as master 
   nodes. However, some nodes can be master-eligible nodes only through explicit configuration.
#### Index
Index is a container to store data similar to a database in the relational databases. An index 
contains a collection of documents that have similar characteristics or are logically related. 
The index name is required to perform the add, update, or delete operations on the document.
#### Document
Document is the piece indexed by Elasticsearch. A document is represented in the JSON format. 
We can add as many documents as we want into an index.
#### Mapping Types
Mappings can be defined as a list of directives given to Elasticseach about how the data is 
supposed to be stored and retrieved. It is important to provide mapping information at the 
time of index creation based on how we want to retrieve our data later. 
#### Meta Fields
As the name indicates, meta fields store additional information about the document. Meta 
fields are meant for mostly internal usage purpose, and it is unlikely that end-user has to 
deal with meta fields. Meta field names start with an underscore. There are around 10 meta 
fields in total. Example:- _index, _id, _source, _size, _doc_count, _field_names, 
_ignored, _routing, _meta, _tier.
#### Simple Data Types
1. Text - This data type is used to store full text like product description. These fields 
   participate in full-text search. These type of fields are analyzed while storing which 
   enables to search these fields by the individual word in it. These type of fields are 
   not used in sorting and aggregation queries.
2. Keywords - This type is also used to store text data but unlike Text, it is not analyzed 
   and stored as-is. This is suitable to store information like a user’s mobile number, city, 
   age, etc. These fields are used in filter, aggregation and sorting queries.
3. Numeric - Elasticsearch supports a wide range of numeric type long, integer, short, byte, 
  double, float.

Note:- There are few more data types supported date (to store the date in a wide range of formats), 
       boolean (true/false, on / off, 1 / 0), IP (to store IP addresses).

#### Special Data Types
1. Geo Point - This data type is used to store geographical location. It accepts latitude and 
   longitude pair. To give an example, this data type can be used to arrange the user’s photo 
   library by their geographical location or graphically display the locations which are trending 
   on social media news.
2. Geo Shape - It allows storing arbitrary geometric shapes like rectangle, polygon.
3. Completion Suggester - This data type is used to provide auto-completion feature over a specific 
   field. As the user types certain text, completion suggester can guide the user to reach particular 
   results.
#### Complex Data Type
1. Object - If you know JSON well, this is not a new concept. Elasticsearch also allows storing 
   nested JSON object structure as a document.
2. Nested - The Object data type is not that useful due to its underlying data representation in 
   the Lucene index. Lucene index does not support inner JSON object. Most of the time what you 
   may want to use is Nested Datatype over Object.

#### Shards
Shards help with enabling Elasticsearch to become horizontally scalable. An index can store 
millions of documents and occupy terabytes of data. This can cause problems with performance, 
scalability, and maintenance.
Indices are divided into multiple units called Shards. Shard is a full-featured subset of an 
index. Shards of the same index now can reside on the same or different nodes of the cluster. 
Shard decides the degree of parallelism for search and indexing operations.
The number of shards per index can be specified at the time of index creation. By default, the 
number of shards created is 5. Although, once the index is created, the number of shards can 
not be changed. To change the number of shards, reindex the data.

#### Replication
Hardware can fail at any time. To ensure fault tolerance and high availability, ES provides a 
feature to replicate the data. Shards can be replicated. A shard, which is being copied, is 
called a Primary Shard. The copy of the primary shard is called a replica shard or simply a 
replica. Like the number of shards, the number of replication can also be specified at the 
time of index creation.
Replication served two purposes:
* High Availability — Replica is never created on the same node where the primary shard is present. 
  This ensures that data can be available through the replica shard even if a complete node is failed.
* Performance — Replica can also contribute to search capabilities. The search queries will be 
  executed parallelly across the replicas.

To summarize, to achieve high availability and performance, the index is split into multiple shards. 
In a production environment, multiple replicas are created for every index. In the replicated index, 
only primary shards can serve write requests. However, all the shards (the primary shard as well as 
replicated shards) can serve read / query requests. The replication factor is defined at the time of 
index creation and can be changed later if required. Choosing the number of shards is an important 
exercise as once defined, it can’t be changed. In critical scenarios, changing the number of shards 
requires creating a new index with required shards and reindexing old data.
