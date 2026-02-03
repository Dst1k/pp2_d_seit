def my_function1(fname): #fname - parameter of a function
  print(fname + " Refsnes")
my_function1("Emil")
my_function1("Tobias")
my_function1("Linus") #names are arguments

#multiple arguments
def my_function2(fname, lname):
  print(fname + " " + lname)
my_function2("Emil", "Refsnes")

#assigning a value to a parameter
def my_function3(name = "friend"):
  print("Hello", name)
my_function3("Emil")
my_function3("Tobias")
my_function3() #name is assigned as "friend" - output "Hello, friend"
my_function3("Linus")

#Keyword arguments
def my_function4(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function4(animal = "dog", name = "Buddy") #order does not matter

#position arguments
def my_function5(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function5("Buddy", "dog") #Order matters

#Combining keyword and position arguments
def my_function6(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)
my_function6("dog", name = "Buddy", age = 5)

#list as an argument
def my_function7(fruits):
  for fruit in fruits:
    print(fruit)
my_fruits = ["apple", "banana", "cherry"]
my_function7(my_fruits)

#Dictionary as an argument
def my_function8(person):
  print("Name:", person["name"])
  print("Age:", person["age"])
my_person = {"name": "Emil", "age": 25}
my_function8(my_person)

def my_function9(name, /): # / - means ONLY positional arguments
  print("Hello", name)
my_function9("Emil")

def my_function10(*, name): # * - means ONLY keyword arguments
  print("Hello", name)
my_function10(name = "Emil")
