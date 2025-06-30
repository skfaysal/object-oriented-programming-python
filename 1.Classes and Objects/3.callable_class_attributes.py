"""
- Attribute values can be any object, including functions, other classes, any callable object, or even instances of other classes.

"""
class MyCallableClass:
    language = "Python"  # Class attribute
     
    def say_hello():
        print("Hellow World!")   


print(MyCallableClass.__dict__)  # {'__module__': '__main__', 'language': 'Python', 'say_hello': <function MyCallableClass.say_hello at 0x...>, '__dict__': <attribute '__dict__' of 'MyCallableClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyCallableClass' objects>, '__doc__': None}

print(MyCallableClass.language)  # 'Python'
print(MyCallableClass.say_hello)  # <function MyCallableClass.say_hello at 0x...>
print(MyCallableClass.say_hello())  # Hellow World!



"""
- Classes are callable.
    - When a class is called, it creates an instance of the class.
    - Its also called Class Instantiation.


- Objects created from same class has its own namespace.
     - Distinct from the class namespace that was used to create the object

"""

"""
Simple example of callable class attributes and class instantiation
"""

class Calculator:
    # Class attribute (data)
    name = "Simple Calculator"
    
    # Class attribute (callable/function)
    def add_numbers(a, b):
        return a + b
    
    # Instance method (requires self)
    def multiply(self, x, y):
        return x * y

# Accessing class attributes directly
print(f"Class Namespace: {Calculator.__dict__}")
print(f"\nCalculator name: {Calculator.name}")
print(f"Function object: {Calculator.add_numbers}")
print(f"Calling class function: {Calculator.add_numbers(5, 3)}")

print("-" * 40)

# Class instantiation - creating objects
calc1 = Calculator()  # Calculator class is callable
calc2 = Calculator()  # Creates another instance

# Each instance has its own namespace
print(f"calc1 namespace: {calc1.__dict__}")
print(f"calc2 namespace: {calc2.__dict__}")

# Instances can access class attributes
print(f"calc1.name: {calc1.name}")
print(f"calc2.name: {calc2.name}")

# Instance methods need an instance to be called
print(f"calc1.multiply(4, 7): {calc1.multiply(4, 7)}")

# Adding instance attributes - only affects that specific object
calc1.owner = "Alice" ## These are instance attributes
calc2.owner = "Bob"

print(f"calc1.owner: {calc1.owner}")
print(f"calc2.owner: {calc2.owner}")

print(f"calc1 namespace after: {calc1.__dict__}")
print(f"calc2 namespace after: {calc2.__dict__}")


"""
- Instance attributes vs class attributes
    - Instance attributes are specific to each object and can be modified independently.
    - Class attributes are shared across all instances of the class.

"""


"""
- Function attributes

"""