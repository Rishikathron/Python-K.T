thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  #print(thisdict[x])
  pass

for x in thisdict.values():
  #print(x)
  pass

for x in thisdict.keys():
  #print(x)
  pass

for x,y in thisdict.items():
  #print(x, y)
  pass


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
#print(mydict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#print(myfamily)
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#print(myfamily["child2"]["name"])

'''
clear()	    #Removes all the elements from the dictionary
copy()	    #Returns a copy of the dictionary
fromkeys()	#Returns a dictionary with the specified keys and value
get()	    #Returns the value of the specified key
items()	    #Returns a list containing a tuple for each key value pair
keys()	    #Returns a list containing the dictionary's keys
pop()	    #Removes the element with the specified key
popitem()	#Removes the last inserted key-value pair
'''