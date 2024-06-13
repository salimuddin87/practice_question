## Inverted Index in Elasticsearch
In Elasticsearch, the inverted index is a core component that enables efficient and fast full-text search.

**The inverted index is a mapping structure that stores the relationship between terms (tokens) and the documents 
they appear in. It “inverts” the normal structure of storing documents with their terms. Instead, it stores a 
list of documents for each term.**

When you index a document in Elasticsearch, the text content is processed through a tokenizer. The tokenizer breaks 
down the text into individual units called tokens. These tokens are usually words, but they could be other units
depending on the tokenizer and the language analyzer in use. During this process, common words like "a", "an", and
"the" (known as stop words) are often removed.

Example:- if you have two documents
1. "The quick brown fox"
2. "A quick brown dog"

The inverted index might look like:

| Term  | Document |
|-------|----------|
| the   | 1        |
| quick | 1, 2     |
| brown | 1,2      |
| fox   | 1        |
| dog   | 2        |

We can note following important points:
1. When you search for a term, Elasticsearch can quickly look up the term in the inverted index and retrieve the list
of documents that contain the term.
2. **Term Frequency and  Document Frequency:** The inverted index may also store additional information, such as the 
term frequency and the document frequency. This information is crucial for relevance scoring in search queries.
3. **Posting Lists:** The lists of documents for each term are often referred to as posting lists. These lists contain
the document IDs or pointers to the documents that contain the respective term.
4. **Query Processing:** When you perform a search query, Elasticsearch analyzes the query terms, looks them up in the
inverted index, and retrieves the relevant posting lists. The intersection of these lists provides the set of 
documents that match the query.

The use of an inverted index allows Elasticsearch to perform complex search operations quickly and efficiently, 
making it a powerful tool for handling large volumes of textual data and providing relevant search results in 
near real-time.
