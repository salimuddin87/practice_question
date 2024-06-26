## Builder method - python Design pattens
Builder Method is a Creation Design Pattern which aims to “Separate the construction of a complex object from 
its representation so that the same construction process can create different representations.” It allows you 
to construct complex objects step by step. Here using the same construction code, we can produce different types 
and representations of the object easily.

It is basically designed to provide flexibility to the solutions to various object creation problems in 
object-oriented programming.

### Problem without using the Builder Method:
Our main purpose is to design the system flexible, reliable, organized and lubricative. what Unexperienced 
developers will do is that they will create a separate and unique class for each and every course provided 
by GeeksforGeeks. Then they will create separate object instantiation for each and every class although which 
is not required every time. The main problem will arise when GeeksforGeeks will start new courses and developers 
have to add new classes as well because their code is not much flexible.

![without builder](C:\Users\md_salimuddin_ansari\PycharmProjects\practice_question\design_pattern\builder_method\problem-builder-Method-2.png)

### Solution by Builder Method:
Our final end product should be any course from GeeksforGeeks. It might be either SDE, STL or DSA. We have to go 
through many steps before choosing a particular course such as finding details about the courses, syllabus, fee 
structure, timings, and batches. Here using the same process we can select different courses available at 
GeeksforGeeks. That’s the benefit of using the builder Pattern.

![with builder](C:\Users\md_salimuddin_ansari\PycharmProjects\practice_question\design_pattern\builder_method\solution-Builder-method.png)

#### Advantages of using Builder Method:
* **Re-usability:** While making the various representations of the products, we can use the same construction code for other representations as well.
* **Single Responsibility Principle:** We can separate out both the business logic as well as the complex construction code from each other.
* **Construction of the object:** Here we construct our object step by step, defer construction steps or run steps recursively.
#### Disadvantages of using Builder method:
* **Code complexity increases:** The complexity of our code increases, because the builder pattern requires creating multiple new classes.
* **Mutability:** It requires the builder class to be mutable
* **Initialization:** Data members of the class are not guaranteed to be initialized.
