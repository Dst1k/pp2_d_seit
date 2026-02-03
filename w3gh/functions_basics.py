#How a simple function is done
def my_function():
  print("Hello from a function")
my_function() #calling a function
my_function() #can be called multiple times

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)
temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)
temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)
#simplifying it into a function
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#returning values
def get_greeting():
  return "Hello from a function"
message = get_greeting()
print(message)
def get_greeting2():
  return "Hello from a function"
print(get_greeting2())

def MyFu():
  pass #functions cannot be empty

def my_function1():
  return ["apple", "banana", "cherry"]
fruits = my_function1()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def my_function2():
  return (10, 20)
x, y = my_function2()
print("x:", x)
print("y:", y)