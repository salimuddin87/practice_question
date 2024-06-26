### What is Elasticsearch?
Elasticsearch is an open-source, distributed search and analytics engine based on the Apache Lucene library. It is
designed to operate in near real-time, providing scalable, fast, and accurate text-based search capabilities along with
numerous analytical functions.

Elasticsearch can store, search, and analyze large volumes of structured and unstructured data, making it a popular
choice for various use cases such as full-text search, log, and event data analysis, and application performance
monitoring.

**Elasticsearch is a schema-less document-based search engine.** This means that you don't need to define a schema for your
documents before you index them. You can simply index the documents and elasticsearch will automatically create a schema
for you. When you index a document, Elasticsearch will create a mapping for the document. The mapping defines the fields
in the document and their types. Elasticsearch will use the mapping to index the document and to search the document.

### What is an Elasticsearch index?
An index is a logical namespace that stores collections of documents with similar characteristics. An index is identified
by a unique name, which helps in referring to the index during various operations such as searching, updating, and 
deleting.
The data is stored in the form of JSON documents. Elasticsearch utilizes a data structure known as in invested index, 
which is specifically designed to enable rapid full-text search. The inverted index notes down every distinct word in
any document and them identifies the complete list of documents where each unique word appears.

### How does Elasticsearch ensure data reliability?
Elasticsearch ensures data reliability through several features, including:
1. **Replication** : Data is replicated to multiple nodes in the cluster, which protects against data loss in the event of a node failure.
2. **Sharding** : Data is divided into shards, which can be distributed across multiple nodes. This improves performance and scalability.
3. **Snapshots and Restores** : Elasticsearch provides a snapshot and restore feature that allows you to create and restore backups of your data. 
This protects against data loss due to human error or disasters.
4. **Monitoring and Alerting** : Elasticsearch provides many monitoring and alerting features that can help you to identify and address potential data problems.
5. **Security** : Elasticsearch can be configured with several security features to protect your data from unauthorized access.

### How do you create, delete, list, and query indices in Elasticsearch?
1. Command to create a new index --- PUT /test_index?pretty
2. Command to delete an index --- DELETE /test_index?pretty
3. Command to list all index --- GET _cat/indices?v
4. Command to query an index --- GET test_index/_search?q=*
5. Command to query multiple indices --- GET test_index1, test_index2/_search?

### Explain the concept of Elasticsearch mapping.
In Elasticsearch, a mapping is a JSON object that defines the structure of a document. It specifies the fields that are
allowed in a document, as well as their data types and other properties.
Mappings are used to control how documents are stored and indexed, and they also affect how documents can be searched and
analyzed. Mappings are a powerful tool that can be used to store data in a structured way. To make it easier to search,
filter, and analyze your data.

### What are analyzers in Elasticsearch?
An analyzer is a component that is used to tokenize text. Analyzers are used to break down text into smaller units called
tokens. These tokens are then used to index and search the text. The primary goal of analyzers is to transform the raw
text into a structured format(tokens) that can be efficiently searched and analyzed.
An analyzer consist of three main components:
1. **Tokenizer :** The tokenizer breaks the input text into a sequence of terms (tokens), usually by splitting it on whitespace or punctuation boundaries.
2. **Token filters :** Token filters process the stream of tokens generated by the tokenizer and can modify, add, or remove tokens.
3. **Character filters :** They are used to preprocess the input text before it reaches the tokenizer. They can modify, add, or remove individual characters from the text.
Example:- 
```
GET /_analyze
{
  "tokenizer" : "standard",
  "filter" : ["lowercase", "asciifolding"],
  "char_filter": [my_char_filter()], # user define char filter
  "text" : "This is nice to learn"
}
```
