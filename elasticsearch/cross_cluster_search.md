## Search across clusters
[Cross-cluster search](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-cross-cluster-search.html) 
lets you run a single search request against one or more remote clusters. For example, you can use a cross-cluster 
search to filter and analyze log data stored on clusters in different data centers.

### Cross-cluster search examples

#### Remote cluster setup
The following **_cluster update settings_** API request adds three remote clusters: 
cluster_one, cluster_two, and cluster_three.
```ignore
PUT _cluster/settings
{
  "persistent": {
    "cluster": {
      "remote": {
        "cluster_one": {
          "seeds": [
            "35.238.149.1:9300"
          ],
          "skip_unavailable": true
        },
        "cluster_two": {
          "seeds": [
            "35.238.149.2:9300"
          ],
          "skip_unavailable": false
        },
        "cluster_three": {       #1 
          "seeds": [
            "35.238.149.3:9300"
          ]
        }
      }
    }
  }
}
```
1. Since **_skip_unavailable_** was not set on **cluster_three**. it uses the default of false.

#### Search a single remote cluster
```
GET /cluster_one:my-index-000001/_search
{
  "size": 1,
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  },
  "_source": ["user.id", "message", "http.response.status_code"]
}
```
Note that when you search one or more remote clusters, a _clusters section is included to provide information 
about the search on each cluster.

#### Search multiple remote clusters
The following search API request searches the my-index-000001 index on three clusters:
1. The local ("querying") cluster, with 10 shards
2. Two remote clusters, cluster_one, with 12 shards and cluster_two with 6 shards.
```
GET /my-index-000001,cluster_one:my-index-000001,cluster_two:my-index-000001/_search
{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  },
  "_source": ["user.id", "message", "http.response.status_code"]
}
```
The API returns the following response:
```
{
  "took": 150,
  "timed_out": false,
  "num_reduce_phases": 4,
  "_shards": {
    "total": 28,
    "successful": 28,
    "failed": 0,
    "skipped": 0
  },
  "_clusters": {
    "total": 3,
    "successful": 3,
    "skipped": 0,
    "running": 0,
    "partial": 0,
    "failed": 0,
    "details": {
      "(local)": {                                  #1    
        "status": "successful",
        "indices": "my-index-000001",
        "took": 21,
        "timed_out": false,
        "_shards": {
          "total": 10,
          "successful": 10,
          "skipped": 0,
          "failed": 0
        }
      },
      "cluster_one": {
        "status": "successful",
        "indices": "my-index-000001",
        "took": 48,
        "timed_out": false,
        "_shards": {
          "total": 12,
          "successful": 12,
          "skipped": 0,
          "failed": 0
        }
      },
      "cluster_two": {
        "status": "successful",
        "indices": "my-index-000001",
        "took": 141,
        "timed_out": false,
        "_shards": {
          "total" : 6,
          "successful" : 6,
          "skipped": 0,
          "failed": 0
        }
      }
    }
  },
  "hits": {
    "total" : {
        "value": 3,
        "relation": "eq"
    },
    "max_score": 1,
    "hits": [
      {
        "_index": "my-index-000001",                #2
        "_id": "0",
        "_score": 2,
        "_source": {
          "user": {
            "id": "kimchy"
          },
          "message": "GET /search HTTP/1.1 200 1070000",
          "http": {
            "response":
              {
                "status_code": 200
              }
          }
        }
      },
      {
        "_index": "cluster_one:my-index-000001",        #3
        "_id": "0",
        "_score": 1,
        "_source": {
          "user": {
            "id": "kimchy"
          },
          "message": "GET /search HTTP/1.1 200 1070000",
          "http": {
            "response":
              {
                "status_code": 200
              }
          }
        }
      },
      {
        "_index": "cluster_two:my-index-000001",        #4
        "_id": "0",
        "_score": 1,
        "_source": {
          "user": {
            "id": "kimchy"
          },
          "message": "GET /search HTTP/1.1 200 1070000",
          "http": {
            "response":
              {
                "status_code": 200
              }
          }
        }
      }
    ]
  }
}
```
1. The local(querying) cluster is identified as "(local)"
2. This document's _index parameter doesn't include a cluster name. This means the document came from the local cluster.
3. This document came from **cluster_one**
4. This document came from **cluster_two**

### Cross-cluster search failures
Failures during a cross-cluster search can result in one of two conditions:
1. partial results (2xx HTTP status code)
2. A failed search (4xx or 5xx HTTP status code)

Failure details will be present in the search response in both cases.

A search will be failed if a cluster marked with skip_unavailable=false is unavailable, disconnects during the search, 
or has search failures on all shards. In all other cases, failures will result in partial results.

Search failures on individual shards will be present in both the _shards section and the _clusters section of the response.
A failed search will have an additional top-level errors entry in the response.

### Excluding clusters or indices from a cross-cluster search
If you use a wildcard to include a large list of clusters and/or indices, you can explicitly exclude one or more 
clusters or indices with a **-** minus sign in front of the cluster or index.

To exclude an entire cluster, you would put the minus sign in front of the cluster alias, 
such as: **_-mycluster:*_**. When excluding a cluster, you must use * in the index position or an error will be returned.

To exclude a specific remote index, you would put the minus sign in front of the index, such as **_mycluster:-myindex_**.

#### Exclude a remote cluster
```
POST /my-index-000001,cluster*:my-index-000001,-cluster_three:*/_async_search  
{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  },
  "_source": ["user.id", "message", "http.response.status_code"]
}
```

#### Exclude a remote index
```
POST /my-index-000001,cluster*:my-index-*,cluster_three:-my-index-000001/_async_search  
{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  },
  "_source": ["user.id", "message", "http.response.status_code"]
}
```
