#Decorators
#Basic Decorators
def changecase(func):
  def myinner():
    return func().upper()
  return myinner
@changecase #Affects the function
def myfunction():
  return "Hello Sally"
print(myfunction())
#can be called multiple times
@changecase
def otherfunction():
  return "I am speed!"
print(myfunction())
print(otherfunction())

#Arguments in decorators
def changecase1(func):
  def myinner(x):
    return func(x).upper()
  return myinner
@changecase1
def myfunction1(nam):
  return "Hello " + nam
print(myfunction1("John"))

#*args and **kwargs
def changecase2(func):
  def myinner1(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner1
@changecase2
def myfunction2(nam):
  return "Hello " + nam
print(myfunction2("John"))

def changecase3(n):
  def changecase3(func):
    def myinner3():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner3
  return changecase3

@changecase3(1)
def myfunction3():
  return "Hello Linus"
print(myfunction3())

#multiple decorators
def changecase4(func):
  def myinner4():
    return func().upper()
  return myinner4
def addgreeting(func):
  def myinner4():
    return "Hello " + func() + " Have a good day!"
  return myinner4
@changecase4
@addgreeting
def myfunction4():
  return "Tobias"
print(myfunction4())

#Metadata
def myfunny():
  return "Have a great day!"
print(myfunny.__name__) #returns "myfunny"

def change(func):
  def myinner():
    return func().upper()
  return myinner
@change
def myfunni():
  return "Have a great day!"
print(myfunni.__name__) # returns "myinner" due to changecase

import functools
def changec(func):
  @functools.wraps(func) # .wraps fixes the previous problem
  def myinner():
    return func().upper()
  return myinner
@changec
def myfunct():
  return "Have a great day!"
print(myfunct.__name__)
