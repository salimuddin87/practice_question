## REST AS A DATA SOURCE
* The data that our resolvers retrieve can come from all kinds of places: a database, 
    a third-party API, webhooks, and so on. These are called data sources. The beauty 
    of GraphQL is that you can mix any number of data sources to create an API that serves 
    the needs of your client applications and graph consumers.
* A GraphQL schema does not need to follow the shape, pattern, or naming of the data sources it uses.


### Resolvers
Resolvers are responsible for returning data for a specific field in our schema.
