#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#tuples

tuples_declaration = ()
#Tuples are used to store multiple items in a single variable.
tuple_var1 = ("apple", "banana", "cherry")
tuple_var2 = (1, 2, "cherry")
tuple_var3 = ("apple", "banana", "cherry","apple") #duplicates are allowed
tuple_var4 = ("abc", 34.2, True, 40, "male") #multiple data types are allowed

tuple_var5 = ("apple",) # tuples should have multiple values
#print(type(tuple_var4))

#NOT a tuple
non_tuple = ("apple")
#print(type(non_tuple),non_tuple)

thistuple = tuple(("apple", "banana", "cherry","orange", "kiwi", "melon", "mango")) # note the double round-brackets
# print(thistuple)
# print(type(mytuple))
# print(thistuple[1])
# print(thistuple[-1])
# print(thistuple[2:5])
# print(thistuple[:4])
# print(thistuple[2:])
# print(thistuple[-4:-1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
#print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
#print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#print(thistuple)

del thistuple
#print(thistuple) #error occurs

#unpacking
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
# print(green)
# print(tropic)
# print(red)



