#self Parameter
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person("Emil", 25)
p1.greet()
# self is used to access class properties and methods
# it basically specifies the object in class

#self Does Not Have to Be Named "self"
class Person1:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age
  def greet(abc):
    print("Hello, my name is " + abc.name)
p1 = Person1("Emil", 36)
p1.greet()

#Accessing properties with self
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")
car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

#Calling methods with self
class Person2:
  def __init__(self, name):
    self.name = name

  def greet2(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet2()
    print(message + "! Welcome to our website.")

p1 = Person2("Tobias")
p1.welcome()
