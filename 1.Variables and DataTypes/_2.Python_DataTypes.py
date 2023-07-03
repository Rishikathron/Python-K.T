
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
None Type:	NoneType
'''

#to get data type of the variable x:

string_var = "hello python"          #string or texttype
boolan_var = True or False           #boolean

#numeric data types
number_var = 1                       #numeric
float_var = 9.0                      #float
complex_var = 2j                     #complex

#sequence datatypes
var_list = ["apple", "banana", "cherry"]    #list
var_tuple = ("apple", "banana", "cherry")	#tuple	
var_range = range(6)	                    #range	

#mapping
x = {"name" : "John", "age" : 36}	    #dict	

#setTypes
x = {"apple", "banana", "cherry"}	    #set	(mutable) allows you to change its values 
x = frozenset({"apple", "banana", "cherry"})	#frozenset (immutable ) # an object that doesn’t allow changes in its value

x = None	#NoneType

x=5
y=x
print(id(x),y)

x= 'Geeks'
print(x,y)

y='Computer'
print(x,y)

#-----to set a specified data type using constructor
x = str("Hello World")	
x = int(20)	
x = float(20.5)		
x = complex(1j)		
x = list(("apple", "banana", "cherry"))		
x = tuple(("apple", "banana", "cherry"))		
x = range(6)		
x = dict(name="John", age=36)		
x = set(("apple", "banana", "cherry"))		
x = frozenset(("apple", "banana", "cherry"))		
x = bool(5)		


#python keywords
'''
False	    def	    if	        raise
None	    del	    import	    return
True	    elif	in	        try
and	        else	is	        while
as	        except	lambda	    with
assert	    finally	nonlocal	yield
break	    for	    not	
class	    from	or	
continue	global	pass
'''

a = "apple"
b = "banana"
a,b = b,a

print(type(a))
print(type(1))
print(type({}))





