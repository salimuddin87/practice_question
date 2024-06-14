### Cluster health API
1. **Request:** GET /_cluster/health/<target>
2. **Prerequisites:** If the Elasticsearch security features are enabled, you must have the monitor 
or manage cluster privilege to use this API.
3. **Description:** The cluster health status is: green, yellow or red. On the shard level, a red status indicates that the specific shard is not allocated in the cluster, yellow means that the primary shard is allocated but replicas are not, and green means that all shards are allocated.

Example:-
1. GET _cluster/health
2. GET _cluster/health/?level=shards
3. GET /_cluster/health/my-index-000001?level=shards



### Debug commands for ES
http://localhost:9200/my_index_test/_search?q=-entity_destinations:21+AND+is_typeahead:true+AND+is_publishable:true

http://localhost:9200/my_index_test/_search?q=NOT%20_exists_%3Aentity_type%20AND%20NOT%20entity_type%3AMIIndustryConcept&track_total_hits=true&size=10000

http://localhost:9200/my_index_test/_search?q=-entity_destinations:21+AND+entity_classes:%22Private%20Company%22+action:add           
http://localhost:9200/my_index_test/_search?q=rd_kos:874&_source=name,rd_kos,rating_status,has_csd_data

http://localhost:9200/private_company__prod__main/_search?size=10&sort=es_upddate:desc
http://localhost:9200/my_index_test/_search?pretty&q=-kensho_score:*
http://localhost:9200/my_index_test/_mapping
http://localhost:9200/_cat/aliases/company*?v&pretty

### To see indexing on es
http://localhost:9200/_cat/indices/*__*?v
http://localhost:9200/_cat/indices/graph_*?v
http://localhost:9200/my_index_test/_count

http://localhost:9200/_cat/nodes?help
http://localhost:9200/_cat/nodes?h=host,heap.percent
http://localhost:9200/_cat/nodes?h=name,fm,fcm,sm,qcm,im&v (Note: fielddata.memory_size(fm), filter_cache.memory_size(fcm), segments.memory(sm), query_cache.memory_size(qcm))
http://localhost:9200/_cat/thread_pool
http://localhost:9200/_cat/indices
http://localhost:9200/_cat/recovery
http://localhost:9200/_cat/shards?v=true&h=index,prirep,shard,store&s=prirep,store&bytes=gb
http://localhost:9200/my_index_test/_segments
