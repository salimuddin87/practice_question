## Circuit breaker settings
Elasticsearch contains multiple circuit breakers used to prevent operations from causing an **_OutOfMemoryError_**. 

Each breaker specifies a limit for how much memory it can use. Additionally, there is a parent-level breaker that 
specifies the total amount of memory that can be used across all breakers.

Except where noted otherwise, these settings can be dynamically updated on a live cluster with the 
cluster-update-settings API.

### Parent circuit breaker


### Field data circuit breaker
The field data circuit breaker estimates the heap memory required to load a field into the field data cache. If 
loading the field would cause the cache to exceed a predefined memory limit, the circuit breaker stops the operation 
and returns an error.

### Request circuit breaker
The request circuit breaker allows Elasticsearch to prevent per-request data structures (for example, memory used for 
calculating aggregations during a request) from exceeding a certain amount of memory.

### In flight requests circuit breaker
The in flight requests circuit breaker allows Elasticsearch to limit the memory usage of all currently active incoming 
requests on transport or HTTP level from exceeding a certain amount of memory on a node. The memory usage is based on 
the content length of the request itself. This circuit breaker also considers that memory is not only needed for 
representing the raw request but also as a structured object which is reflected by default overhead.

### Script compilation circuit breaker
Slightly different than the previous memory-based circuit breaker, the script compilation circuit breaker limits 
the number of inline script compilations within a period of time.

### Regex circuit breaker
Poorly written regular expressions can degrade cluster stability and performance. The regex circuit breaker limits 
the use and complexity of regex in Painless scripts.

### EQL(Event Query Language) circuit breaker
When a sequence query is executed, the node handling the query needs to keep some structures in memory, which are 
needed by the algorithm implementing the sequence matching. When large amounts of data need to be processed, and/or 
a large amount of matched sequences is requested by the user (by setting the size query param), the memory occupied 
by those structures could potentially exceed the available memory of the JVM. This would cause an OutOfMemory exception 
which would bring down the node.

To prevent this from happening, a special circuit breaker is used, which limits the memory allocation during the 
execution of a sequence query. When the breaker is triggered, an org.elasticsearch.common.breaker.CircuitBreakingException 
is thrown and a descriptive error message is returned to the user.

### Machine learning circuit breaker
* **_breaker.model_inference.limit_** 

(Dynamic) The limit for the trained model circuit breaker. This value is defined as a percentage of the JVM heap. 
Defaults to 50%. If the parent circuit breaker is set to a value less than 50%, this setting uses that value as its 
default instead.

* **_breaker.model_inference.overhead_**

(Dynamic) A constant that all trained model estimations are multiplied by to determine a final estimation. 
See Circuit breaker settings. Defaults to 1 

* **_breaker.model_inference.type_**

(Static) The underlying type of the circuit breaker. There are two valid options: noop and memory. noop means the 
circuit breaker does nothing to prevent too much memory usage. memory means the circuit breaker tracks the memory 
used by trained models and can potentially break and prevent OutOfMemory errors. The default value is memory.
