class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Emil", 36)
print(p1.name)
print(p1.age)

#without __init__
class Person1:
  pass
p1 = Person1()
p1.name = "Tobias"
p1.age = 25
print(p1.name)
print(p1.age)

#default values in __init__
class Person2:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age
p1 = Person2("Emil")
p2 = Person2("Tobias", 25)
print(p1.name, p1.age)
print(p2.name, p2.age)

#Multiple parameters
class Person3:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person3("Linus", 30, "Oslo", "Norway")
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)