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

str4 = "Hello"
str5 = "ASG"
str7 = str4 + str5
str6 = "Hello"+"ASG"
print(str6)
print(str7)

# length of string
print(len(str4))
print(len(str7))

# length count every thing in string including spaces, special characters, and numbers.
# let see the example
str9 = "Hello"
str10 = "ASG"
print(len(str9), len(str10))
print(len(str9 + " " + str10)) # here we add space between two strings so it will count the space also.

# Indexing
'''
Indexing is kind of saying that character gets is postion number in string. In python, 
indexing starts from 0.
'''
str11 = "ASGBother"
print(str11[0])  # Output: A
print(str11[1])  # Output: S

# Slicing in strings
# Accessing parts of strings is called slicing. Slicing is done by using the colon operator(:) inside
# the square brackets. The syntax for slicing is: string[start:end:step]

Str12="ASGBother"

strtest1=Str12[0:3] # it will print the string from index 0 to 2
print(strtest1) # Output: ASG

strtest2=Str12[3:8] # it will print the string from index 3 to 7
print(strtest2) # Output: Bothe

strtest3 = Str12[0:5:2] # it will print the string from index 0 to 4 with step 2
print(strtest3) # Output: AGBte

strtest4=Str12[:8] # it will print the string from index 0 to end with step 2
print(strtest4) # Output: ASG

strtest5=Str12[1:4] # it will print the string from index 1 to 3
print(strtest5) # Output: SGB

#Slincing with negative index
strtest6=Str12[-8:-3] # it will print the string from index -8 to -4
print(strtest6) # Output: SGBot

strtest7=Str12[-1:-2] # it will print the string from index -1 to -2
print(strtest7) # Output: other