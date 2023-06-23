#List is a collection which is ordered and changeable. Allows duplicate members.

#list and its properties 
list_declaration1 = [] #empty list
list_declaration2 = list() #empty list with constructor
print(type(list_declaration1))

list_var1 = [1,2,3,4]
list_var2 = [1,"string",True,4.0,[5,6,"multiple_data_types",8]]
list_var3 = [1,"string",True,4.0,{1:"sriram"},(2,3)]
#print("listvar3 ",list_var3)

list_var = ["apple", "banana", "cherry"]
#print(len(list_var))

#Accessing the list items
list_var = ["apple", "banana", "cherry"]
# print(list_var[1])
# print(list_var[-1])
# print(list_var[2:5])
# print(list_var[:4])
# print(list_var[2:])

var1 = list(("Sriram","Tamil","Test","orange", "kiwi", "mango")) #using costructor
# print(var1,type(var1))

#changing the list items
var1[2] = "blackcurrant"
# print(var1)

var1[2:4] = ["sample", "watermelon"]
# print(var1)

var1[2:4] = ["changed"]
# print(var1)

#Changing list items using methods
var1.insert(2,"Jashwanth") 
# print(var1)
#insert to specify where the value must go through indexing
#append will always insert the value at the end
var1.append("Rohit")
# print(var1)

#extend is for combining 2 lists or combining values into a list
list1 = ["zoro","luffy"]
list2 = ["ironman","spiderman"] 
list1.extend(list2) #extending the list1 with list2 contents
# print(list1)

list_modified = ["flash", "arrow", "superwomen"]
tuple_modified = ("Xmen", "Ymen")
list_modified.extend(tuple_modified)
#print(list_modified)

#with dictionary the key's are considered into an extend for list
list_modified = ["flash", "arrow", "superwomen"]
dict_modified = {"frozen" : 'aana',"disney" : "mickey"}
list_modified.extend(dict_modified)
#print(list_modified)

list_variables = ["flash", "arrow", "superwomen","daredevil","mydiag"]
list_variables.remove("arrow")
#print(list_variables)
list_variables.pop()
#print(list_variables)
list_variables.pop(2)
#print(list_variables)
list_variables.clear()
#print(list_variables)




