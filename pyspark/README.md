## PySpark
* PySpark is an open-source unified analytics engine for large-scale data processing. It provides high-level APIs in Java,
Scala, Python, and R, and an optimized engine that supports general execution graphs. It also supports powerful 
distributed SQL and machine learning libraries.

* Apache Spark is a lightning fast real-time processing framework. It does in-memory computations to analyze data in 
real-time. It came into picture as Apache Hadoop MapReduce was performing batch processing only and lacked a real-time 
processing feature. Hence, Apache Spark was introduced as it can perform stream processing in real-time and can also 
take care of batch processing.

* Apart from real-time and batch processing, Apache Spark supports interactive queries and iterative algorithms also. 
Apache Spark has its own cluster manager, where it can host its application. It leverages Apache Hadoop for both storage 
and processing. It uses HDFS (Hadoop Distributed File system) for storage and it can run Spark applications on YARN (Yet
Another Resource Negotiator) as well.

* YARN, or Yet Another Resource Negotiator, is a core component of Apache Hadoop that manages resources and schedules 
jobs for distributed applications running on a Hadoop cluster. YARN's architecture separates the processing layer from 
the resource management layer, which offers flexibility and scalability.

* Using PySpark, you can work with RDDs in Python programming language also. It is because of a library called **Py4j** that
they are able to achieve this. PySpark offers PySpark Shell which links the Python API to the spark core and initializes
the Spark context. Majority of data scientists and analytics experts today use Python because of its rich library set.

* Resilient Distributed Dataset (RDD) is a fundamental data structure in Apache Spark that represents a collection of 
data elements that are partitioned across nodes in a cluster. RDDs are immutable, fault-tolerant, and can be operated 
on in parallel. They are often used when working with unstructured data, such as media streams or text streams, and 
when low-level transformation and actions are desired.

### SparkContext
SparkContext is the entry point to any spark functionality. When we run any Spark application, a driver program starts, 
which has the main function and your SparkContext gets initiated here. The driver program then runs the operations 
inside the executors on worker nodes.

SparkContext uses **Py4J** to launch a JVM and creates a JavaSparkContext. By default, PySpark has SparkContext available 
as ‘sc’, so creating a new SparkContext won't work.
```
class pyspark.SparkContext (
   master = None, # URL of the cluster it connects to
   appName = None, # Name of the application
   sparkHome = None, # Spark installation diarectory
   pyFiles = None,  # The .zip or .py files to send to the cluster and add to the PYTHONPATH
   environment = None, # Worker nodes environment variables
   batchSize = 0, # The no of python objects, set 1 to disable, 0 to automatically choose the size, or -1 to use an unlimited batch size
   serializer = PickleSerializer(), # RDD serializer
   conf = None, # An object of SparkConf to set all the spark properties.
   gateway = None, # Use the existing gateway and JVM, otherwise initializing a new JVM
   jsc = None, # The JavaSparkContext instance
   profiler_cls = <class 'pyspark.profiler.BasicProfiler'> # Used to do profiling
)
```

### SparkConf
To run a Spark application on the local/cluster, you need to set a few configurations and parameters, this is what 
SparkConf helps with. It provides configurations to run a Spark application. 
Initially, we will create a SparkConf object with SparkConf(), which will load the values from spark.* Java system 
properties as well. Now you can set different parameters using the SparkConf object and their parameters will take 
priority over the system properties.

In a SparkConf class, there are setter methods, which support chaining. For example, you can write 
conf.setAppName(“PySpark App”).setMaster(“local”). 
Once we pass a SparkConf object to Apache Spark, it cannot be modified by any user.
Following are some of the most commonly used attributes of SparkConf −
```
set(key, value) − To set a configuration property.
setMaster(value) − To set the master URL.
setAppName(value) − To set an application name.
get(key, defaultValue=None) − To get a configuration value of a key.
setSparkHome(value) − To set Spark installation path on worker nodes.
```
Let us consider the following example of using SparkConf in a PySpark program. In this example, we are setting the spark
application name as PySpark App and setting the master URL for a spark application to → spark://master:7077.

The following code block has the lines, when they get added in the Python file, it sets the basic configurations for 
running a PySpark application.
```
from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("PySpark App").setMaster("spark://master:7077")
sc = SparkContext(conf=conf)
```

### SparkFiles
