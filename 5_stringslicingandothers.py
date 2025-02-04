import string
mystr = "deemis is a good boy"
print(mystr) # This will print "deemi"
print(mystr[0]) # This will print "d"
print(mystr[1]) # This will print "e"
print(mystr[2]) # This will print "e"
print(mystr[3]) # This will print "m"
print(mystr[4]) # This will print "i"
print(mystr[5]) # This will print "s"
print(mystr[6]) # This will print " "
print(mystr[7]) # This will print "i"
print(mystr[8]) # This will print "s"
print(mystr[9]) # This will print " "
print(mystr[10]) # This will print "a"
print(mystr[11]) # This will print " "
print(mystr[12]) # This will print "g"
print(mystr[13]) # This will print "o"
print(mystr[14]) # This will print "o"
print(mystr[15]) # This will print "d"
print(mystr[16]) # This will print " "
print(mystr[17]) # This will print "b"
print(mystr[18]) # This will print "o"
print(mystr[19]) # This will print "y"
# This is called string slicing. We can get a single character from a string using its index.
# We can also get a range of characters from a string using slicing.
print(mystr[0:5]) # This will print "deemi"
print(mystr[0:6]) # This will print "deemis"
print(mystr[0:7]) # This will print "deemis "
print(mystr[0:8]) # This will print "deemis i"
print(mystr[0:9]) # This will print "deemis is"
print(mystr[0:10]) # This will print "deemis is "
print(mystr[0:11]) # This will print "deemis is a"
print(mystr[0:12]) # This will print "deemis is a "
print(mystr[0:13]) # This will print "deemis is a g"
print(mystr[0:14]) # This will print "deemis is a go"
print(mystr[0:15]) # This will print "deemis is a goo"
print(mystr[0:16]) # This will print "deemis is a good"
print(mystr[0:17]) # This will print "deemis is a good "
print(mystr[0:18]) # This will print "deemis is a good b"
print(mystr[0:19]) # This will print "deemis is a good bo"
print(mystr[0:20]) # This will print "deemis is a good boy"

"""Note: in the above example, we are using the slicing operator [a:b] to get the characters from index a to index b-1. The slicing operator [a:b] will return the substring starting from index a and ending at index b-1. If a is not specified, it will start from the beginning of the string. If b is not specified, it will go to the end of the string and in colons, the first number is inclusive and the second number is exclusive."""

# We can also use negative indexing to get the characters from the end of the string.
print(mystr[-1]) # This will print "y"
print(mystr[-2]) # This will print "o"
print(mystr[-3]) # This will print "b"
print(mystr[-4]) # This will print " "
print(mystr[-5]) # This will print "d"
print(mystr[-6]) # This will print "o"
print(mystr[-7]) # This will print "o"
print(mystr[-8]) # This will print "g"
print(mystr[-9]) # This will print " "
print(mystr[-10]) # This will print "a"
print(mystr[-11]) # This will print " "
print(mystr[-12]) # This will print "s"
print(mystr[-13]) # This will print "i"
print(mystr[-14]) # This will print " "
print(mystr[-15]) # This will print "s"
print(mystr[-16]) # This will print " "
print(mystr[-17]) # This will print "m"
print(mystr[-18]) # This will print "i"
print(mystr[-19]) # This will print "e"
print(mystr[-20]) # This will print "d"

#note: short example to understand negative indexing
mystr = "Hello, World!"
print(mystr[-1])  # Output: "!"
print(mystr[-2])  # Output: "d"

# We can also use slicing with negative indexing.
print(mystr[-5:-1]) # This will print "doob" (from index -5 to -2)
print(mystr[-5:-2]) # This will print "doob" (from index -5 to -3)
print(mystr[-5:-3]) # This will print "doo" (from index -5 to -4)
print(mystr[-5:-4]) # This will print "d" (from index -5 to -5)

#note: short example to understand negative slicing
mystr = "Hello, World!"
print(mystr[-6:-1])  # Output: "World"
print(mystr[-5:])    # Output: "orld!"

#Negative slicing in Python allows you to access elements of a sequence (like a string, list, or tuple) from the end rather than the beginning. Negative indices start from -1 for the last element, -2 for the second last, and so on.
"""In negative slicing, the start index should be less than the end index when both are negative. If the start index is greater than or equal to the end index, the result will be an empty string."""

# Quick Quiz
nm = "Harry"
print(nm[-4:-2]) # This will print "ar"
print(nm[-4:4]) # This will print "arr"
print(nm[-4:5]) # This will print "arry"
print(nm[-4:6]) # This will print "arry"
print(nm[-4:7]) # This will print "arry"

#to know about the length of the string
mystr = "deemis is a good boy"
print(len(mystr)) # This will print 20
# The len() function is used to get the length of a string. It returns the number of characters in the string.
print(mystr[0:20]) # This will print "deemis is a good boy"
"""when you use more than the string length in slicing, it will not give you an error, it will give you the whole string but if you use more than the string length in indexing, it will give you an error because indexing is used to get the single character from the string."""

"""if you want to skip a middle character, you can use the skip value in the slicing operator."""

mystr = "deemis is a good boy"
print(mystr[0:20:2]) # This will print "dmsaog" (skipping every second character)
print(mystr[0:20:3]) # This will print "disg y" (skipping every third character)

"""Note: if you want to give blank value to the skip value, it will print the whole string."""

mystr = "deemis is a good boy"
print(mystr[0:20: ]) # This will print "deemis is a good boy
print(mystr[ : : 2]) # This will print "dmsaog" (skipping every second character)
print(mystr[ : : 3]) # This will print "disg y" (skipping every third character)
print(mystr[ : : ]) # This will print "deemis is a good boy" (skipping every character)
print(mystr[ : : 1]) # The statement print(mystr[::1]) will print the entire string mystr as it is and can not print skipping every character
print(mystr[ : : -1]) # This will print "yob doog a si sihmed" (reversing the string)

"""Note: The statement print(mystr[0:20:3]) is using Python's slicing syntax to extract a substring from mystr and then print it. Here's a breakdown of the slicing syntax [start:stop:step]:

start (0): The starting index of the slice. In this case, it starts from the beginning of the string.
stop (20): The ending index of the slice (exclusive). It attempts to go up to the 20th character, but if mystr is shorter than 20 characters, it will stop at the end of the string.
step (3): The step size, which means it will take every 3rd character from the start index to the stop index.
Example:"""
mystr = "Hello, World!"
print(mystr[0:20:3])  # Output: "Hl r!"
#In this example, it starts at index 0, goes up to (but not including) index 20, and takes every 3rd character. The characters at indices 0, 3, 6, 9, etc., are included in the result.

#Advanced Slicing or Extended Slicing
"""Extended slicing in Python refers to the use of the slicing syntax [start:stop:step] to extract elements from a sequence (like a string, list, or tuple) with a specified step size. This allows for more flexible and powerful ways to access and manipulate sequences."""

#Here's a detailed explanation with examples:

#Syntax:
#sequence[start:stop:step]
#start: #The starting index of the slice. Defaults to the beginning of the sequence if omitted.
#stop: #The ending index of the slice (exclusive). Defaults to the end of the sequence if omitted.
#step: #The step size, which determines the increment between each index. Defaults to 1 if omitted.
#Examples
#Basic Slicing:
mystr = "Hello, World!"
print(mystr[0:5])  # Output: "Hello"

#Extended Slicing with Step:

mystr = "Hello, World!"
print(mystr[0:12:2])  # Output: "Hlo ol"

#Negative Step (Reversing):
mystr = "Hello, World!"
print(mystr[::-1])  # Output: "!dlroW ,olleH"

#Negative Indices:
mystr = "Hello, World!"
print(mystr[-5:-1])  # Output: "orld"

#Combining Negative Indices and Step:
mystr = "Hello, World!"
print(mystr[-1:-6:-1])  # Output: "!dlro"

#Example from mentioned Code
mystr = "Hello, World!"
print(mystr[0:20:3])  # Output: "Hl r!"

#start (0): #Starts from the beginning of the string.
#stop (20): #Attempts to go up to the 20th character, but stops at the end of the string if it's shorter.
#step (3): #Takes every 3rd character.
#This results in the characters at indices 0, 3, 6, 9, etc., being included in the output.

"""Summary:
Extended slicing provides a powerful way to access and manipulate sequences by allowing you to specify a start, stop, and step size. This can be used for various tasks such as reversing a sequence, skipping elements, or extracting specific patterns."""
# to reverse the string using slicing
mystr = "Hello, World!" 
print(mystr[::-1]) # This will print "!dlroW ,olleH"
# to skip the middle character using slicing
mystr = "Hello, World!"
print(mystr[0:20:2]) # This will print "Hlo ol!"
print(mystr[ : : 2]) # This will print "Hlo ol!"])

print(mystr[ : : -1]) # This will print "!dlroW ,olleH"
print(mystr[ : : -2]) # This will print "!dl oWl,oeH"

