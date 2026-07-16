''' String is data types that stores a sequence of characters. In Python, strings are 
represented as sequences of Unicode characters. Strings can be created by enclosing 
characters in either single quotes (' ') or double quotes (" "), and also in triple 
quotes (''' ''' or """ """).'''

str1='Hello ASG'
str2="Hello ASG"
str3='''Hello ASG'''
print(str1 + "\n" + str2 + "\n" + str3)

# 'this is ASG's tutorial' 

''' In above line python get confused because here we use the sindle quotes and also we
 have use the single apostrophe symbol so the python interpreter will think the single 
 quotes starded and end in betwwen ASG and s wheir we use the apostrophe symboland will 
not understanded what to do with "s tutorial" this part of string '''

"this is ASG's tutorial" # this is the right way to write when we have to use apostrophe symbol

# Basic Operations on Strings
# 1. Concatenation 
# we can concatenate two or more strings using the + operator.

str1 = "Hello"
str2 = "ASG"
str3 = str1 + str2
str4 = "Hello"+"ASG"
print(str3)
print(str4)

# length of string
print(len(str1))
print(len(str3))

# length count every thing in string including spaces, special characters, and numbers.
# let see the example
str1 = "Hello"
str2 = "ASG"
print(len(str1), len(str2))
print(len(str1 + " " + str2)) # here we add space between two strings so it will count the space also.

# Indexing
'''
Indexing is kind of saying that character gets is postion number in string. In python, 
indexing starts from 0.
'''
str1= "ASGBother"
print(str1[0])  # Output: A
print(str1[1])  # Output: S

# Slicing in strings
# Accessing parts of strings is called slicing. Slicing is done by using the colon operator(:) inside
# the square brackets. The syntax for slicing is: string[start:end:step]
Str="ASGBother"
str=Str[0:3] # it will print the string from index 0 to 2
print(str) # Output: ASG
str=Str[3:8] # it will print the string from index 3 to 7
print(str) # Output: Bother
str10 = Str[0:5:2] # it will print the string from index 0 to 7 with step 2
print(str10) # Output: AGBte
str=Str[:2] # it will print the string from index 0 to end with step 2
print(str) # Output: ASG