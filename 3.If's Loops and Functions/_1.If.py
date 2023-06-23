'''
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''
a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 33
b = 200
if b > a: #example without indentation
#print("b is greater than a") # you will get an error
    pass

#elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#else without elseif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#short hand if
if a > b: print("a is greater than b")

#short hand if else
a = 2
b = 330
print("A") if a > b else print("B")

#condition with "and"
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#condition with "or"
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
