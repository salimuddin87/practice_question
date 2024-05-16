## Anatomy of a GraphQL server
The GraphQL server is where all the magic happens.

### The schema
The GraphQL schema is a collection of types and fields that make up the 
comprehensive picture of everything we can do with the data in a GraphQL server.

### Schema definition language (SDL)
The GraphQL schema has its own language called schema definition language, or SDL.
GraphQL example schema:
```
type Fruit {
  name: String! (Non-nullable or required field)
  quantity: Int
  averageWeight: Float
  hasEdibleSeeds: Boolean
  nutrients: [String]
  soldBy: Vendor
}

type Vendor {
  name: String!
  fruitCatalog: [Fruit]
}
```
The Fruit type is an example of an object type. We define an object type using 
the type keyword, then the name of the object, followed by curly braces. Inside 
the curly braces, we define the fields associated with that type.

A field starts with the name of the field, then a colon (:) and then the type for 
that field. In the example above, all the fields in the Fruit type are scalar types.

The available scalar types in GraphQL are String, Int, Float, Boolean and ID. 
These are similar to scalar types in any programming language. The square brackets 
([]) indicate a List type.

#### Entry point
A GraphQL operation (the thing that the client sends to the GraphQL server) can either 
be a query, a mutation, or a subscription. A query reads data, a mutation changes data 
and a subscription listens for live, streaming data.

All three operations map to a corresponding type in the schema: Query, Mutation and 
Subscription. Let's take the query as an example.
```
type Query {
  mostPopularFruit: Fruit
}
```
#### The resolver functions
For every type and field in the GraphQL schema, we need to define a resolver function. 
This is a function that can retrieve the data for a specific field. These functions have 
access to various data sources: databases, REST APIs, even text files or JSON!

Resolvers for fields in our schema follow the hierarchy of the schema. This means that 
resolver functions for the name and quantity fields on a Fruit type are methods that 
belong to a Fruit class. This keeps our resolver functions just as organized as our schema.

## Anatomy of a GraphQL operation
The journey starts with a GraphQL operation sent from the client. We described a GraphQL 
operation as "a string that defines the selection set of fields [the client] needs". When 
we write this operation, we use the schema as our reference guide for what types and fields 
we have access to, and how they relate to each other.
```
query GetMostPopularFruit {
  mostPopularFruit {
    name
    hasEdibleSeeds
    soldBy {
      name
    }
  }
}
```
First, we start with the type of GraphQL operation, in this case query, followed by an 
operation name of our choosing, GetMostPopularFruit, then curly braces. Inside, we can 
start to add fields from the Fruit type: name, hasEdibleSeeds, soldBy. And since soldBy 
is a field that returns a Vendor type, we add fields from that type as well, like name.

### Key takeaways
* There are three types of GraphQL operations: queries, mutations and subscriptions. A 
  query reads data, a mutation changes data and a subscription listens for live, streaming data.
* The GraphQL schema is a collection of types and fields that make up the comprehensive 
  picture of everything we can do with the data in a GraphQL server. It is written in schema 
  definition language (SDL).
* A resolver function retrieves the data for a specific field in our schema. These functions 
  have access to various data sources: databases, REST APIs, even text files or JSON. These 
  data sources don't need to live within the GraphQL server.
