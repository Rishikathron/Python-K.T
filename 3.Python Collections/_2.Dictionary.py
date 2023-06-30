#Dictionary is a collection which is ordered** and changeable. No duplicate members.
#dictionaries and its properties

dict_declaration = {} #empty dictionary

#keys and values can be of any datatypes but keys has to be hashable 
dict_var = {"Key" : "value"} 
dic_var1 = {1,12}
dic_var2 = {1:"student_name"}
dic_var3 = {1 : [2,"sriram","sriram@gmail.com"]}
#nested dictionary
dict_var4 = {
                1 : {
                    1.1 : "sriram",
                    1.2 : "Tamil"
                },
                2 : {
                    2.1 : [1,2,"other types"]
                }
            } 
#Dictionaries cannot have two items with the same key:
#dict will be in the concept of hash storage
print(dic_var2)
print(type(dict_declaration))

#dict using constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#accessing the dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["model"])
print(thisdict.get("model"))

#keys dict
print(thisdict.keys())

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

print(car.keys())#before the change
car["color"] = "white"
print(car.keys()) #after the change
print(car)

#values
print(car.values())

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#items

print(car.items())

#changing the items in the dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
#deleting
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model") #removes the spcified key
print(thisdict)
#----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem() #removes the last item
print(thisdict)
#--------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#-----------------
del thisdict #deletes the entire dict
print(thisdict) #throws error
thisdict.clear()#clears all the items 
print(thisdict)


