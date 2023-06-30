# Strings

# print("Hello")
# print('Hello')

multiline_variable_doublequotes = """Python is a dynamic, interpreted (bytecode-compiled) language.
                        There are no type declarations of variables, parameters, functions, 
                        or methods in source code. This makes the code short and flexible, and
                        you lose the compile-time type checking of the source code."""

#print(multiline_variable_doublequotes)

multiline_variable_singlequotes = '''Python is a dynamic, interpreted (bytecode-compiled) language.
                        There are no type declarations of variables, parameters, functions, 
                        or methods in source code. This makes the code short and flexible, and
                        you lose the compile-time type checking of the source code.'''

#print(multiline_variable_singlequotes)

#Square brackets can be used to access elements of the string.
a = "Hello, World!"
#print(a[1])

#To get the length of a string, use the len() function.
a = "Hello, World!"
#print(len(a))

#string Slicinig
word = "Hello, python!"

#indexing starts from 0

#syntax for slicing str_varname[starting_index : endingIndex-1]
# print(word[2:5])

index = "0123456789"
# print(index[2:6])

# print(index[2:])
# print(index[:8])

rev_index = "0123456789" #considering "-10-9-8-7-6-5-4-3-2-1"
# print(rev_index[-5:-2])
# print(rev_index[:-1]) # exclude last character
# print(rev_index[-1:]) # prints only last character

s = "0123456789"
print(s[::-1]) #reverse the string
# print(s[::2])  # print characters at second position from start 02468
# print(s[::-2])  # print characters at second position from end 97531
# print(s[::]) # print whole string - copy of original string 0123456789
# print(s[:])  # print whole string - copy of original string 0123456789
# print(s[6::-1]) # reverse string from 6 th position 6543210
# print(s[3::]) # print string starting from index 3 3456789
# print(s[1::2]) # starting from index 1 intervals of 2 13579
# print(s[2::2]) #starting from index 2 intervals of 2 2468

# strings are immutable

somestr= 'Random'
# somestr[0]='u'
# print(somestr)

stringtype= 'Helo?'
#print(stringtype[:2]+'l'+stringtype[2:]) # 'he'+l+'lo'


#But you can reassign whole new value to the variable

#we can delete the string also
#del somestr
#print(stringtype[:1]+stringtype[2:]) # hlo



#comparing two strings
str1='Hi'
str2='Hi'
str3='Hello'

# print(str1 == str2)
# print(str1 == str3)
# print(1 == '1')

# in not in

#print('am' in 'This is a program')
#print('am' not in 'This is a program')

# print("hello"*4)

#string Modification
variable = "Anzu"
variable.upper()           #converts to upper case
variable.lower()           #converts to lower case
split_var = "learn, python,ki"   #split returns ['hai', 'python']       
split_var.split(',')        # splits the string into substrings if it finds instances of the separator
variable.replace('A','a')  #replaces a string with another string
print(split_var.split(',') )

#String Formating
#concatenate strings
# print('My name is ' + 'Manasa')

#ex-0

age = 23

txt = "My name is luffy, My age is "
# print(txt+age) #will not concat int and string
# print(txt+str(age))


#ex-1
age = 23
txt = "My name is Anzu, I am {}"
# print(txt.format(age))
# print("my age is "+age+"and my name is lufyy")

#ex-2
Student_Name = "Anzu"
Student_age = 23
Student_Dept = "CSE"
statement = "Hi this is {}, I'm {} years old from {} Department"
# print(statement.format(Student_Name,Student_age,Student_Dept))
statement = "Hi this is {2}, I'm {1} years old from {0} Department"
# print(statement.format(Student_Name,Student_age,Student_Dept))
statement = "Hi this is {a}, I'm {b} years old from {} Department"
print(statement.format(Student_Name,b=Student_age,a=Student_Dept))
#another syntax
# print("Hi my name is {}".format("virat"))

# print(f"Hi this is {Student_Name}, I'm {Student_age} years old from {Student_Dept} Department")

#txt = "We are the so-called "Pirates" from sea."
#print(txt)
txt = "We are the so-called \"Pirates\" from sea."
print(txt)

# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \t	Tab	
# \b	Backspace

#string methods

# capitalize()
# count()
# isalpha()
# isnumeric()
# islower()
# isupper()
#and more...

# write a program to reverse a string
# write a program to find whether a string is palindrome or not - madam,mom,noon,level
# write a program to print letters at odd/even index.








