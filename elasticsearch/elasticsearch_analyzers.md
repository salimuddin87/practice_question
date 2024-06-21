# Built-in analyzer
Elasticsearch ships with a wide range of built-in analyzers, 
which can be used in any index without further configuration:
## Standard Analyzer
The standard analyzer divides text into terms on word boundaries, as defined by the Unicode Text Segmentation algorithm. 
It removes most punctuation, lowercases terms, and supports removing stop words.
## Simple Analyzer
The simple analyzer divides text into terms whenever it encounters a character which is not a letter. 
It lowercases all terms.
## Whitespace Analyzer
The whitespace analyzer divides text into terms whenever it encounters any whitespace character. 
It does not lowercase terms.
## Stop Analyzer
The stop analyzer is like the simple analyzer, but also supports removal of stop words.
## Keyword Analyzer
The keyword analyzer is a “noop” analyzer that accepts whatever text it is given and outputs the exact 
same text as a single term.
## Pattern Analyzer
The pattern analyzer uses a regular expression to split the text into terms. It supports lower-casing and stop words.
## Language Analyzers
Elasticsearch provides many language-specific analyzers like english or french.
## Fingerprint Analyzer
The fingerprint analyzer is a specialist analyzer which creates a fingerprint which can be used for duplicate detection.

## Custom analyzers
If you do not find an analyzer suitable for your needs, you can create a **_custom_** analyzer 
which combines the appropriate 
[character filters](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-charfilters.html), 
[tokenizer](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-tokenizers.html), 
and [token filters](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-tokenfilters.html).

When the built-in analyzers do not fulfill your needs, you can create a custom analyzer 
which uses the appropriate combination of:
1. zero or more character filters
2. a tokenizer
3. zero or more token filters.

```
PUT my-index-000001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_analyzer": {
          "type": "custom", 
          "tokenizer": "standard",
          "char_filter": [
            "html_strip"
          ],
          "filter": [
            "lowercase",
            "asciifolding"
          ]
        }
      }
    }
  }
}

POST my-index-000001/_analyze
{
  "analyzer": "my_custom_analyzer",
  "text": "Is this <b>déjà vu</b>?"
}
```
