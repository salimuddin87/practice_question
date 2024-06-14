## Query optimization to increase search performance
1. **Size parameter:** Assigning a huge value to size parameter causes Elasticsearch to compute vast amounts of hits,
which causes severe performance issues. Instead of setting a huge size, you should batch requests in small sizes.
2. **Shards and Replicas:** Optimize necessary index settings that play a crucial role in Elasticsearch performance,
like the number of shards and replicas. In many cases having more replicas helps improve search performance.
3. **Deleted documents:** Having a large number of deleted documents in the Elasticsearch index also causes search
performance issues, as explained in this [official document](https://www.elastic.co/blog/lucenes-handling-of-deleted-documents).
4. **Search filters:** Effective use of filters in Elasticsearch queries can improve search performance dramatically
as the filter clauses are 1) cached, and 2) able to reduce the target documents to be searched in the query clause.
5. **Wildcard queries:** Avoid wildcard, especially leading wildcard queries, which causes the entire Elasticsearch
index to be scanned.
6. **Regex and parent-child:** Regex queries and parent-child can cause search latency.
7. **Multitude of small shards:** Having many small shards could cause a lot of network calls and threads, which
severely impact search performance.
8. **Heavy aggregations:** Avoid heavy aggregations that involve unique IDs.
9. **Timeout and terminate:** Timeout param and terminate after param can be useful when executing heavy searches,
or when result is vast.
10. **search templates:** Use [search templates](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-template.html)
to achieve better abstraction, meaning without exposing your query syntax to your users. Search templates also help
you transfer less data over the network, which is particularly useful when you have large Elasticsearch queries.
11. **Multi search API:** Use [msearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-multi-search.html)
whenever possible. In most of the applications it's required to query multiple Elasticsearch indices for a single
transaction, and sometimes users do so in a serial order even when it's not requiered. 
12. **Term queries:** Use term query when you need an exact match and on keywords fields. By default, Elasticsearch 
generates both text and keyword fields for every field that consists of a string value if explicit mapping is not 
supplied. Users tend to use the match query even on keyword data types like product-ids, which is costly as match 
query goes through an analysis operation. Read the difference between [Term vs Match](https://stackoverflow.com/questions/60867242/elasticsearch-match-vs-term-in-filter/60867368#60867368) 
query and always use term query on keyword data types and wherever you need exact searches for better performance.
13. **Source filtering:** [_source filtering](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/search-fields.html#source-filtering)
is a great way to improve the performance of Elasticsearch queries when retrieving a large number of documents or 
documents of large sizes. By default, Elasticsearch returns the complete source of matching documents. If you don’t 
need _source at all or need only values of specific fields, you can achieve this with _source filtering.
