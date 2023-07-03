
# 1. Write a program to find a letter in a word: 
# eamplex:1 
# target = 'Z'
# value = "Zebra"
# o/p : True
# explanation:
# program should return true if target is in the value else it should return false

word = "Python Programming"
value = 'Z'

if value in word:
    print(True)
else:
    print(False)

# 2. Write a program to find first 'N' letters are in upper case
# ex 1:
N = 3
value = "PYThon"
# o/p : False

if value[0:N].isupper() == True:
    print(True)
else:
    print(False)

# ex2:
N = 4
value = "HELLO WORLD"
# o/P: True
# explanation : if the first 3 letters in the word is in upper case return true
if value[0:N].isupper() == True:
    print(True)
else:
    print(False)

#none
#0,False,None = False
if None:
    print("Hai")
else:
    print("None")