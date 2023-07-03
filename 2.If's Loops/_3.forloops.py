# for _item_ in _itemCollections_:
#       --- conditions or algorithms or block of code-------

#basic for loops
for i in "PythonPrgramming":
  print(i)
  #print(i,end="")
  



#Using the range() function:
for x in range(6):
  #print(x)
  pass

for x in range(2, 6):
  #print(x)
    pass

for x in range(2, 30, 3):
  #print(x)
  pass

for x in range(6): #else without an if 
  # print(x)
  pass
else:
  # print("Finally finished!")
  pass

for x in range(6):
  if x == 3: break
  #print(x)
else:
  #print("Finally finished!")
  pass

#The pass Statement
for x in [0, 1, 2]:
  pass

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  #print(x)
   pass

for x in "banana":
  #print(x)
  pass

#loops with if condition
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  #print(x)
  if x == "banana":
    break

#With the break statement we can stop the loop before it has looped through all the items:
#will exit the loop if element matches with banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  #print(x)
  if x == "banana":
    break

#nested for loops
colors = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in colors:
  for y in fruits:
    #print(x, y)
    pass





