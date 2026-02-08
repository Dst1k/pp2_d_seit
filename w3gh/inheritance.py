#Inheritance
#Create a parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()

#Create a child class
class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()

#Add the __init__ function
class Student1(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
x = Student1("Mikey", "Olsen2")
x.printname()

#The super() function
class Person2:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname2(self):
    print(self.firstname, self.lastname)
class Student2(Person):
  def __init__(self, fname, lname,year):
    super().__init__(fname, lname)
    self.graduationyear = year
x = Student2("Mike", "Super",2019)
x.printname()
print(x.graduationyear)

#Add Methods
class Person3:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname3(self):
    print(self.firstname, self.lastname)
class Student3(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student3("Mike", "Olsen", 2024)
x.welcome()
