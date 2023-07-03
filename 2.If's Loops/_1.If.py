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
if (b > a):
  #print("a is greater")
  pass

a = 33
b = 200
if b > a: #example without indentation
  #print("b is greater than a") # you will get an error
  pass

#elif as else if
a = 33
b = 33
if b > a:
  #print("b is greater than a")
  pass
elif a == b:
  #print("a and b are equal")
  pass


#else
a = 200
b = 33
if b > a:
  #print("b is greater than a")
  pass
elif a == b:
  #print("a and b are equal")
  pass
else:
  #print("a is greater than b")
  pass

#else without elseif
a = 200
b = 33
if b > a:
  #print("b is greater than a")
  pass
else:
  #print("b is not greater than a")
  pass


#short hand if or ternary operators
if a > b: pass



#short hand if else
# a = 2
# b = 330

# print("A") if a > b else print("B") 



# a = 2
# b = 330
# print('a') if a>b else print('c') if a==b else print("in else")



#condition with "and"
a = 200
b = 33
c = 500
if a > b and c > a:
  #print("Both conditions are True")
  pass
#condition with "or"
a = 200
b = 33
c = 500
if a > b or a > c:
  #print("At least one of the conditions is True")
  pass



# if 1:
#   print("inside if")
# else:
#   print("else")

# 0 or False

# if -0:
#   print(True)
# if 0 or False:
#   print(False)
# else:
#   print(True)

# if 'A'
# if -1 or -2 or -999 or 999 or 'a' or 'Z' or "hello" #returns true

#details to be noted

while False:
  pass
else:
  pass

if True:
  while True:
    pass
else:
  pass

while True:
  pass
else:
  pass



# 1. Write a program to find a letter in a word: 
# eamplex:1 
# target = 'Z'
# value = "Zebra"
# o/p : True
# explanation:
# program should return true if target is in the value else it should return false



# 2. Write a program to find first 'N' letters are in upper case
# ex 1:
# N = 3
# value = "Upper"
# o/p : False

# ex2:
# N = 4
# value = "HELLO WORLD"
# o/P: True
# explanation : if the first 3 letters in the word is in upper case return true




