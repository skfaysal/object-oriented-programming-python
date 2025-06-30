"""
- What is an object?
 a Container
   contains data --> state --> attributes
   contains functionality --> behavior --> methods
   can be used to model real-world entities

   
- How to create an object?
 1. Define a class
 2. Create an instance of the class
 3. Use the instance to access attributes and methods

- What is a class?
 A blueprint or template for creating objects 
    Classes have behavior and state
    They are callable.  MyClass() creates an instance of the class
    Classes can be used to create multiple objects with the same structure and behavior

- Insytances are created from classes
  Their type is the class they are created from
  If MyClass is a class, then
  
  my_instance = MyClass() is an instance and type of MyClass
  type(my_instance) is MyClass
  isinstance(my_instance, MyClass) is True

- How to create a class?
 1. Use the class keyword
 2. Define the class name (usually CamelCase)
 3. Define the class body with attributes and methods
 4. Use the class to create instances
 5. Use the instances to access attributes and methods
 Example:
class MyClass:
    pass

Now type of MyClass is <class 'type'>, which is a metaclass
"""

class MyClass:
    pass

print(type(MyClass))  # <class 'type'>

# Already created metaclass for MyClass
print(MyClass.__class__)  # <class 'type'>
print(MyClass.__name__)  # MyClass
print(MyClass.__module__)  # __main__
print(MyClass.__qualname__)  # MyClass
print(MyClass.__doc__)  # None

## Creating an instance of MyClass
my_instance = MyClass()
print(type(my_instance))  # <class '__main__.MyClass'>
print(isinstance(my_instance, MyClass))  # True
print(my_instance.__class__)  # <class '__main__.MyClass'>

