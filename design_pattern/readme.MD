### Factory Method
* Factory Method is a creational design pattern used to create concrete implementations of a common interface.
* It separates the process of creating an object from the code that depends on the interface of the object.
* Factory Method allows an interface or a class to create an object, but lets subclasses decide 
  which class or object to instantiate. Using the Factory method, we have the best ways to create 
  an object. Here, objects are created without exposing the logic to the client, and for creating 
  the new type of object, the client uses the same common interface.

### Advantages of using Factory method: 
We can easily add new types of products without disturbing the existing client code. 
Generally, tight coupling is being avoided between the products and the creator classes and objects.

### Disadvantages of using Factory method:
To create a particular concrete product object, the client might have to sub-class the creator class.
You end up with a huge number of small files i.e, cluttering the files.
