## Tune for indexing speed

### Use bulk requests
Bulk requests will yield much better performance than single-document index requests. In order to know the optimal size 
of a bulk request, you should run a benchmark on a single node with a single shard. First try to index 100 documents at 
once, then 200, then 400, etc. doubling the number of documents in a bulk request in every benchmark run. When the 
indexing speed starts to plateau then you know you reached the optimal size of a bulk request for your data. 

In case of tie, it is better to err in the direction of too few rather than too many documents. Beware that too large 
bulk requests might put the cluster under memory pressure when many of them are sent concurrently, so it is advisable 
to avoid going beyond a couple tens of megabytes per request even if larger requests seem to perform better.

### Use multiple workers/threads to send data
A single thread sending bulk requests is unlikely to be able to max out the indexing capacity of an Elasticsearch 
cluster. In order to use all resources of the cluster, you should send data from multiple threads or processes. In 
addition to making better use of the resources of the cluster, this should help reduce the cost of each fsync.

Make sure to watch for TOO_MANY_REQUESTS (429) response codes (EsRejectedExecutionException with the Java client), 
which is the way that Elasticsearch tells you that it cannot keep up with the current indexing rate. When it happens, 
you should pause indexing a bit before trying again, ideally with randomized exponential backoff.

Similarly to sizing bulk requests, only testing can tell what the optimal number of workers is. This can be tested by 
progressively increasing the number of workers until either I/O or CPU is saturated on the cluster.

### Unset or increase the refresh interval (index.refresh_interval)
The operation that consists of making changes visible to search - called a refresh - is costly, and calling it often 
while there is ongoing indexing activity can hurt indexing speed.

By default, Elasticsearch periodically refreshes indices every second, but only on indices that have received one 
search request or more in the last 30 seconds.

### Disable replicas for initial loads
If you have a large amount of data that you want to load all at once into Elasticsearch, it may be beneficial to set 
**_index.number_of_replicas_** to 0 in order to speed up indexing. Having no replicas means that losing a single node 
may incur data loss, so it is important that the data lives elsewhere so that this initial load can be retried in case 
of an issue. Once the initial load is finished, you can set **_index.number_of_replicas_** back to its original value.

If **_index.refresh_interval_** is configured in the index settings, it may further help to unset it during this 
initial load and setting it back to its original value once the initial load is finished.

### Give memory to the filesystem cache
The filesystem cache will be used in order to buffer I/O operations. You should make sure to give at least half the 
memory of the machine running Elasticsearch to the filesystem cache.

### Use auto-generated ids
When indexing a document that has an explicit id, Elasticsearch needs to check whether a document with the same id already exists within the same shard, which is a costly operation and gets even more costly as the index grows. By using auto-generated ids, Elasticsearch can skip this check, which makes indexing faster.

### Use faster hardware
If indexing is I/O-bound, consider increasing the size of the filesystem cache (see above) or using faster storage. Elasticsearch generally creates individual files with sequential writes. However, indexing involves writing multiple files concurrently, and a mix of random and sequential reads too, so SSD drives tend to perform better than spinning disks.

### Indexing buffer size
If your node is doing only heavy indexing, be sure **_indices.memory.index_buffer_size_** is large enough to give at most 512 MB indexing buffer per shard doing heavy indexing (beyond that indexing performance does not typically improve). Elasticsearch takes that setting (a percentage of the java heap or an absolute byte-size), and uses it as a shared buffer across all active shards. Very active shards will naturally use this buffer more than shards that are performing lightweight indexing.

The default is 10% which is often plenty: for example, if you give the JVM 10GB of memory, it will give 1GB to the index buffer, which is enough to host two shards that are heavily indexing.

### Use cross-cluster replication to prevent searching from stealing resources from indexing
Within a single cluster, indexing and searching can compete for resources. By setting up two clusters, configuring cross-cluster replication to replicate data from one cluster to the other one, and routing all searches to the cluster that has the follower indices, search activity will no longer steal resources from indexing on the cluster that hosts the leader indices.

### Avoid hot spotting 
Hot Spotting can occur when node resources, shards, or requests are not evenly distributed. Elasticsearch maintains cluster state by syncing it across nodes, so continually hot spotted nodes can cause overall cluster performance degredation.

### Additional optimizations
Many of the strategies outlined in [Tune for disk usage](https://www.elastic.co/guide/en/elasticsearch/reference/current/tune-for-disk-usage.html) 
also provide an improvement in the speed of indexing.
