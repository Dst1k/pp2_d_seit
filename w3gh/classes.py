#OOP stands for Object-Oriented Programming.

#Advantages of OOP:
#Provides a clear structure to programs
#Makes code easier to maintain, reuse, and debug
#Helps keep your code DRY (Don't Repeat Yourself)
#Allows you to build reusable applications with less code

#Classes and objects
class MyClass:
  x = 5         #Create a class
p1 = MyClass()  #Create an object
print(p1.x)

#Multiple objects
p2 = MyClass()
p3 = MyClass()
print(p2.x)
print(p3.x)

#deleting objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1)
