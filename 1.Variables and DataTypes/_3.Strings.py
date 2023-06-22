#
# Strings

print("Hello")
print('Hello')

multiline_variable_doublequotes = """Python is a dynamic, interpreted (bytecode-compiled) language.
                        There are no type declarations of variables, parameters, functions, 
                        or methods in source code. This makes the code short and flexible, and
                        you lose the compile-time type checking of the source code."""

print(multiline_variable_doublequotes)

multiline_variable_singlequotes = ''''Python is a dynamic, interpreted (bytecode-compiled) language.
                        There are no type declarations of variables, parameters, functions, 
                        or methods in source code. This makes the code short and flexible, and
                        you lose the compile-time type checking of the source code.'''
print(multiline_variable_singlequotes)

#string Slicinig
word = "Hello, python!"

#indexing starts from 0

#syntax for slicing str_varname[starting_index : endingIndex-1]
print(word[2:5])

index = "0123456789"
print(index[2:6])

print(index[2:])
print(index[:8])

rev_index = "0123456789" #considering "-10-9-8-7-6-5-4-3-2-1"
print(rev_index[-5:-2])


#string Modification
variable = "Sriram"
variable.upper()           #converts to upper case
variable.lower()           #converts to lower case
split_var = "Hai, python"   #split returns ['hai', 'python']       
split_var.split(',')        # splits the string into substrings if it finds instances of the separator
variable.replace('S','s')  #replaces a string with another string


#String Formating

#ex-1
age = 23
txt = "My name is Sriram, I am {}"
print(txt.format(age))

#ex-2
Student_Name = "Sriram"
Student_age = 23
Student_Dept = "CSE"
statement = "Hi this is {}, I'm {} years old from {} Department"
print(statement.format(Student_Name,Student_age,Student_Dept))

#string methods

capitalize()
count()
isalpha()
isnumeric()
islower()
isupper()
#and more...





