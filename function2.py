#FUNTIONS 
'''
a= "lmao"
print(a.capitalize()) # .capitalize() function makes the FIRST LETTER CAPITAL


b = " Lmao rofl lol"
print(b.find("rofl")) # .find() tells the starting index(position) of substring in string


print(b.find("lol",8,10)) #arguments to find a substring between two index, if it is *not present* it gives -1*

print(a.isalnum()) #To check whether a string is alpha/numeric or not

str = "36373"
print(str.isdigit()) #CHECKS WHETHER A STRING HAS ONLY DIGITS

a = "lmao"
print(a.islower()) #TELLS WHETHER A STRING HAS LOWER CASE CHARACTERS ONLY OR NOT
print(a.isupper())
a = "LMAO rofl"
print(a.lower()) # print all characters in lower case
print(a.upper())
b = "b" # But not in "" ****
print(b.isspace()) #CHECKS WHETHER STRING HAS ONLY SPACES OR NOT 
'''


'''
•  title() : The title() method returns a string where the first character in every word is upper case. Like a header, or a title
If the word contains a number or a symbol, the first letter after that will be converted to upper case.
Syntax: string.title()
'''
'''
txt = "lol ro3fl lmao"
print(txt.title()
'''
'''
• isalpha() : The isalpha() method returns True if all the characters are alphabet letters (a-z).

Example of characters that are not alphabet letters: **(space)**!#%&? etc.
'''
'''
a = "Vegetapride"
print(a.isalpha())
'''


'''
• partition() : The partition() method searches for a specified string, and splits the string into a tuple containing three elements.

The first element contains the part before the specified string.

The second element contains the specified string.

The third element contains the part after the string.

**If the specified value is not found, the partition() method returns a tuple containing: 1 - the whole string, 2 - an empty string, 3 - an empty string
EXAMPLE: 
'''
'''
a = " Vegeta Lmao lol rofl"
print(a.partition("lol"))
print(a.partition("lmaorofl"))
'''
'''
•STRIP(): The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)

Syntax:
string.strip(characters)
**Optional.We a se(randomlyt of characters to remove as leading/trailing characters
'''
'''
a = "     lmao     "
b = "abcd.,..LMAO..,"
print(a.strip())
#print(a)
#print(b.strip("bacd.,"))
#print(a.lstrip())



••The* rstrip() *method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.

Syntax:
string.rstrip(characters)
**Optional: A set of characters to remove as trailing characters
'''
#a= "abc.......aaaaa"
#print(a.rstrip("a."))

'''
••The replace() method replaces a specified phrase with another specified phrase.

Note: All occurrences of the specified phrase will be replaced, if nothing else is specified.

Syntax:
**string.replace(oldvalue, newvalue, count)
oldvalue	
Required:The string to search for
newvalue.	
Required:The string to replace the old value with
count	
**Optional: A number specifying how many occurrences of the old value you want to replace. Default is all occurrences
'''
#a= "Lmao hello hello world"
#print(a.replace("hello", "lol",1))
#print(a.replace("hello", "lol"))