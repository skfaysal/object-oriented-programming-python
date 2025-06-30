"""
- Deifing attributes in classes
  - Attributes are variables that belong to a class
  - They are defined inside the class body
  - They can be accessed using the instance of the class

"""
class MyClass:
    language = "Python"  # Class attribute
    version = 3.10  # Class attribute

"""
- Get class attributes
  - Class attributes can be accessed using getattr() function
  Example:
  getattr(MyClass, 'language')  # 'Python'
  getattr(MyClass, 'version')  # 3.10
  - Class attributes can be accessed using dot notation
  Example:
  MyClass.language  # 'Python'
  MyClass.version  # 3.10

- Set class attributes
  - Class attributes can be set using setattr() function
  Example:
  setattr(MyClass, 'language', 'JavaScript')
  setattr(MyClass, 'version', 3.11)
  - Class attributes can be set using dot notation
  Example:
  MyClass.language = 'JavaScript'
  MyClass.version = 3.11
  - Class attributes can be deleted using del statement
  Example:
  del MyClass.language
  del MyClass.version
  
"""

## Get class attributes
print(getattr(MyClass, 'language'))  # 'Python'
print(getattr(MyClass, 'version'))  # 3.10

print(MyClass.language)  # 'Python'
print(MyClass.version)  # 3.10

## Set class attributes
setattr(MyClass, 'language', 'JavaScript')
setattr(MyClass, 'version', 3.11)
print(getattr(MyClass, 'language'))  # 'JavaScript'
print(getattr(MyClass, 'version'))  # 3.11      

MyClass.language = 'JavaScript'
MyClass.version = 3.11
print(MyClass.language)  # 'JavaScript'
print(MyClass.version)  # 3.11


"""
- Where is the state of the class stored?
  - In a dictionary.

"""

