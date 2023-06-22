#set
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

temp_declaration = {} # a dict
temp1_declation = {1,2,3} # set (non key value pair is set with "{}")
set_declaration = set() #using constructor to change other types to set
temp = [1,2,3,4]

set_var1 = set(temp)
print(set_var1)

set_var2 = set([1,2,2,3]) #set does not allow duplicates
print(set_var2)
