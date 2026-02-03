#Arbitrary arguments - *args
def my_function(*kids): #If you do not know how many arguments will be passed into your function, add a * before the parameter name.
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def my_function1(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)
my_function1("Emil", "Tobias", "Linus")

#*args and regular arguments
def my_function2(greeting, *names):
  for name in names:
    print(greeting, name)
my_function2("Hello", "Emil", "Tobias", "Linus")

def my_function3(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total
print(my_function3(1, 2, 3))
print(my_function3(10, 20, 30, 40))
print(my_function3(5))

#Arbitrary Keyword arguments - **kwargs
def my_function4(**kid):
  print("His last name is " + kid["lname"])
my_function4(fname = "Tobias", lname = "Refsnes")

def my_function5(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)
my_function5(name = "Tobias", age = 30, city = "Bergen")

# **kwargs and regular arguments
def my_function6(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)
my_function6("emil123", age = 25, city = "Oslo", hobby = "coding")

# *args and **kwargs
def my_function7(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)
my_function7("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

#Unpacking args and kwargs
def my_function8(a, b, c):
  return a + b + c
numbs = [1, 2, 3]
result = my_function8(*numbs) # Same as: my_function(1, 2, 3)
print(result)

def my_function9(fname, lname):
  print("Hello", fname, lname)
person = {"fname": "Emil", "lname": "Refsnes"}
my_function9(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

#Scopes
#Local Scope
def myfunc():
  x = 300 #inside of a function
  print(x)
myfunc()

def myfunc1():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc1()

#Global Scope
v = 300
def myfunc2():
  print(v)
myfunc2()
print(v)

x1 = 300
def myfunc3():
  x1 = 200
  print(x1)
myfunc3()
print(x1)

#Global Keyword
def myfunc4():
  global u
  u = 300
myfunc4()
print(u)

t = 300
def myfunc5():
  global t
  t = 200
myfunc5()
print(t)

#Nonlocal Keyword
def myfunct1():
  x = "Jane"
  def myfunct2():
    nonlocal x
    x = "hello"
  myfunct2()
  return x
print(myfunct1())

#LEGB rule - Local Enclosin Global Built-in
d = "global"
def outer():
  d = "enclosing"
  def inner():
    d = "local"
    print("Inner:", d)
  inner()
  print("Outer:", d)
outer()
print("Global:", d)
