#basic for loops
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
  print(x)
  if x == "banana":
    break

#Using the range() function:
for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)


#nested for loops
colors = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in colors:
  for y in fruits:
    print(x, y)


