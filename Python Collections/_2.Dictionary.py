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
#dict will be in the concept of hash storage
print(dic_var2)
print(type(dict_declaration))
