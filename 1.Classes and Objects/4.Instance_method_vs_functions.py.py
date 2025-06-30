"""
- A function defined in the class as a attributes is called a function.
- But we want to use the function from an object then its called an instance method not a function.
  - The difference between a function and an instance method is that:
    - A function is a standalone piece of code that can be called independently.
    - An instance method is bound to an object. So always takes the instance or objects as the first argument (usually named `self`).

"""

"""
Demonstrating the difference between functions and instance methods
"""

class Person:
    # Function defined as class attribute (no self parameter)
    def say_hello():
        return "Hello from function!"
    
    # Instance method (has self parameter)
    def introduce(self, name):
        return f"Hi, I'm {name}"

# Accessing as FUNCTION from the class directly
print("=== FUNCTION (from class) ===")
print(type(Person.say_hello))  # <class 'function'>
print(Person.say_hello())      # "Hello from function!"

print("\n=== INSTANCE METHOD (from object) ===")
# Create an instance
person1 = Person()

# Accessing as METHOD from the instance
print(type(person1.say_hello))  # <class 'method'>
# person1.say_hello()  # This would cause an error! No self parameter

# Instance method works correctly
print(type(person1.introduce))   # <class 'method'>
print(person1.introduce("Alice"))  # "Hi, I'm Alice"

print("\n=== Key Differences ===")
print(f"Class function: {Person.say_hello}")
print(f"Instance method: {person1.say_hello}")
print(f"Function callable independently: {Person.say_hello()}")
print(f"Method bound to object: {person1.introduce('Bob')}")

# The instance method automatically passes 'self'
print(f"Method is bound to: {person1.introduce.__self__}")