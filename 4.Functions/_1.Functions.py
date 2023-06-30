#function definition

'''
syntax : def __funcion_name__():
            ----***code block***----
'''
def my_function():
  #print("Hello from a function")
  pass  
my_function()


#funcion with arguments:
def my_function(fname):
  #print(fname + " Refsnes")
  pass
my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(fname, lname):
  #print(fname + " " + lname)
  pass
my_function("Emil", "Refsnes")

def my_function(*kids):
  #print("The youngest child is " + kids[2])
  pass
my_function("Emil", "Tobias", "Linus")


def my_function(child3, child2, child1):
  #print("The youngest child is " + child3)
  pass
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function(country = "Norway"):
  print("I am from " + country)
  pass  
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#function with looping
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)


#function returning values:
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))