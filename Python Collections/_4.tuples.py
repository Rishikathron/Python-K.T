#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#tuples

tuples_declaration = ()
#Tuples are used to store multiple items in a single variable.
tuple_var1 = ("apple", "banana", "cherry")
tuple_var2 = (1, 2, "cherry")
tuple_var3 = ("apple", "banana", "cherry","apple") #duplicates are allowed
tuple_var4 = ("abc", 34.2, True, 40, "male") #multiple data types are allowed

tuple_var5 = ("apple",) # tuples should have multiple values
print(type(tuple_var4))

#NOT a tuple
non_tuple = ("apple")
print(type(non_tuple),non_tuple)