#set
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

temp_declaration = {} # a dict
temp1_declation = {1,2,3} # set (non key value pair is set with "{}")
set_declaration = set() #using constructor to change other types to set
temp = [1,2,3,4]

set_var1 = set(temp)
#print(set_var1)
#print(type(set_var1))

set_var2 = set([1,2,2,3]) #set does not allow duplicates
#print(set_var2)

set_var3 = {"apple", "banana", "cherry", True, 1, 2} #true and 1 are same
#print(set_var3)

#print(len(set_var3))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# print(set1)
# print(set2)
# print(set3)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  #print(x)
   pass
#print("banana" in thisset)

thisset.add("orange")
#print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
#print(thisset)


set_1   = {"apple", "banana", "cherry"}
list_1  = ["kiwi", "orange"]

set_1.update(list_1)
#print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
#print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
#print(thisset)

x = thisset.pop()
#print(x)
thisset.clear()
#print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset) #throws error

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  #print(x)
  pass

'''
add()	            #Adds an element to the set
clear()	            #Removes all the elements from the set
copy()	            #Returns a copy of the set
difference()	    #Returns a set containing the difference between two or more sets
discard()	        #Remove the specified item
intersection()	    #Returns a set, that is the intersection of two other
union()	            #Return a set containing the union of sets
update()	        #Update the set with the union of this set and others
'''




