## GraphQL
GraphQL enables precise data retrieval with a single query, eliminating the 
need to navigate multiple REST endpoints on the client app side.
Hot Chocolate is a GraphQL server framework for .NET developers.

## Journey of a GraphQL operation
To get that data, it sends a GraphQL operation to our GraphQL server. The app 
shapes the operation as a string that defines the selection set of fields it 
needs. Then, it sends that operation to the server in an HTTP POST or GET request.

## In server-land
When our server receives the HTTP request, it first extracts the string with the 
GraphQL operation. It parses and transforms it into something it can better 
manipulate: a tree-structured document called an AST (Abstract Syntax Tree). With 
this AST, the server validates the operation against the types and fields in our 
schema.
If anything is off (e.g. a requested field is not defined in the schema or the 
operation is malformed), the server throws an error and sends it right back to 
the app.
In this case, the operation looks good, and the server can "execute" it. Meaning, 
the server can continue its process and actually fetch the data. The server walks 
down the AST.

Note:- In this way, GraphQL is a powerful bridge to REST (and other data sources!) 
that ties all of your app's data together. The GraphQL API acts as the layer on top 
of them, providing a single interface through which multiple data sources can be 
queried simultaneously.

As all of the operation's fields are resolved, the data is assembled into a nicely 
ordered JSON object with the exact same shape as the query.

The server assigns the object to the HTTP response body's data key, and it's time 
for the return trip, back to our app.

## Back to client-land
Our client receives the response with exactly the data it needs and passes that data 
to the right components to render them.
