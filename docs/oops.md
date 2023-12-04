# Object Oriented Programming

Procedural
- Distinguishes data(variables) and code (modules and functions)
- the program is divided into data types and functions
- Functions can use data but data cannot use functions
- Data can use methods

Object Oriented
- Data and code are enclosed together in classes
- the program is divided into objects, which include data and methods
- Objects exchange data and activate their methods

## Constructor Function
- special function called to create an object each time the class is invoked
- name of the constructor function is always `__init__` and needs atleast one parameter usually named `self`

when a class component starts with two underscores it becomes private. The property can in that cas only be accessed from within the class. This is called encapsulation

superclass: an abstract class from which other more specific objects can derive

instance variable: an variable that is created and added to the object on initialization

hasattr: specifies whether an instance contain a certain attribute

Contrary to instance variables, class variables are stored outside any object, thus:
- they aren't shown in an object's `__dict__`
- they always return the same value in all class instances (objects), except if they are altered inside the class method. In the latter case, any new object that invokes that method, alters the class variable's value
- they can still be accessed with the `hasattr()` function and with `object.<variable>` notation
- they can be private like any other properties and accessed with `'_ClassName__PrivatePropertyName'` notation