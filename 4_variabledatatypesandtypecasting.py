#Tutorial 1 (Hello World)

#variable and datatypes
var1 = "Hello World" #string
var2 = 4 #integer
var3 = 36.7 #float
var4 = "Deepak" #string
var5 = "32" #string
var6 = "45" #string
print(var1)
print(type(var1)) #type() is used to find the type of the variable.
print(type(var2))
print(type(var3))
print(var2 + var3) #it will add the two variables.
print(var1 + var4) #it will add the two variables.
print(var2 + var3) #it will add the two variables.
print(var5 + var6) #it will add the two variables.
print(int(var5) + int(var6)) #it will add the two variables.
print(10 * "Hello World\n") #it will print the string 10 times.
print(10 * str(int(var5) + int(var6))) #it will print the string 10 times.
print(10 * "Hello World\n") #it will print the string 10 times.
print(10 * str(int(var5) + int(var6))) #it will print the string 10 times.

#Tutorial 2 (Calculator)

#typecasting
var1 = "Hello World" #string
print("Hello World")
print("Hello World 6")
import flask
import itertools as it
print(20*20)
print(10*5+5*30+40*5)
print(45/7+20/4)

#Tutorial 3 ( Comment, Escape Sequence & Print Statement)

print("Hello World")
#input function
print("Enter your number")
#please do not remove this line 
"""
this is a 
multiline comment
"""
#above wroted line is showing that when you use multiline comment then you can write any thing in it with three double quotes.
print("please subscribe my channel", end=" ") #end is used to print the next line in the same line, if you remove end then it will print in the next line.
print("please subscribe my channel", end=" ")
print("because i will post all videos regadrding my channel here")
#if i write anaything between end=" " then it will print between the two lines.
print("please subscribe my channel", end=", ")
print("because i will post all videos regadrding my channel here")
#\n #this is used to print the next line in the same line.
print("please subscribe my channel", end="\n")
print("c:\deemis")
#\n this line is used to print the next line in the same line.
print("please subscribe my channel", end="\n")
#escape sequences in python are used to print the next line in the same line. example is given below.
print("please subscribe my channel", end="\n")
print("deepak is a \n good boy \t") #\n is used to print the next line in the same line and \t is used to give a tab space.

#Tutorial 4 (Variable, Datatypes and Typecasting)

#variable and datatypes
var1 = "Hello World" #string
# variable is a container which is used to store the data. like in the above line var1 is a variable which is used to store the string "Hello World" so that we can use it later in the program to print it.
print(var1)
# variable do not have any fixed data type, it can store any type of data like in the above line var1 is storing the string "Hello World" and in the below line var2 is storing the integer 4 so it is not necessary that the variable should have the same data type.
var1 = "Hello World" #string
var2 = 4 #integer
var3 = 36.7 #float
var4 = "Deepak" #string
var5 = "32" #string
var6 = "45" #string

#let's check that python can identify the data type of the variable or not.

print(type(var1)) #type() is used to find the type of the variable.
print(type(var2)) #type() is used to find the type of the variable.
print(type(var3)) #type() is used to find the type of the variable.
print(var2 + var3) #it will add the two variables.
print(var1 + var4) #it will add the two variables.
print(var2 + var3) #it will add the two variables.
print(var5 + var6) #it will add the two variables.
print(int(var5) + int(var6)) #it will add the two variables.
print(10 * "Hello World\n") #it will print the string 10 times.
print(10 * str(int(var5) + int(var6))) #it will print the string 10 times.

#concatination of two strings in python is done by using + operator.
print(var1 + var4) #it will add the two variables and print the string "Hello WorldDeepak" in the output.

#typecasting
var1 = "Hello World" #string

#when you want to convert string in integer then you can use int() function.
#when you want to convert string in float then you can use float() function.
#when you want to convert integer in string then you can use str() function.
#when you want to convert float in string then you can use str() function.
#when you want to convert float in integer then you can use int() function.
#when you want to convert integer in float then you can use float() function.

print("20")
print("10" + "5")
print(int("10") + int("5"))
print(10 * "Hello World\n")
print(10 * str(int("10") + int("5")))

""" str() function is used to convert the integer into string. """
""" int() function is used to convert the string into integer. """
""" float() function is used to convert the string into float. """
""" float() function is used to convert the integer into float. """
""" int() function is used to convert the float into integer. """
""" str() function is used to convert the float into string. """
""" print() function is used to print the output on the screen. """
""" input() function is used to take the input from the user. """

#below mentioned lines have little bit confusing concept so take care of it and below mentioned lines are used to take the input from the user and print it on the screen.

inpnum = input("27",) #input() function is used to take the input from the user.
print(inpnum) #it will print the input taken from the user.
print(type(inpnum)) #type() is used to find the type of the variable.
print(int(inpnum) + 10) #it will add the two variables and print the output on the screen.

#emample to make a calculator using input function.
print("Enter First number")
n1 = input() #input() function is used to take the input from the user.
print(" Enter second number")
n2 = input() #input() function is used to take the input from the user.
print("The sum of these two numbers is", int(n1) + int(n2)) #it will add the two variables and print the output on the screen.

#take an example to make first calcualtor using input function.
print("enter first number")
n1 = input()
print("enter second number")
n2 = input()
print("the sum of these two numbers is", int(n1) + int(n2))

