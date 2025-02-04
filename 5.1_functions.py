"""In Python programming, functions are used to encapsulate code into reusable blocks. Here are some common functions and their uses:

1- Built-in Functions
Python provides many built-in functions that are always available for use:"""

#print(): Outputs text to the console.
print("Hello, World!")  # Output: "Hello, World!"

#len(): Returns the length of an object.
my_list = [1, 2, 3]
print(len(my_list))  # Output: 3

#type(): Returns the type of an object.
my_str = "Hello"
print(type(my_str))  # Output: <class 'str'>

#int(), float(), str(): Converts between types.
print(int("42"))  # Output: 42
print(float("3.14"))  # Output: 3.14
print(str(42))  # Output: "42"

#input(): Reads input from the user.
name = input("Enter your name: ")
print("Hello, " + name + "!")  # Output: "Hello, [user's input]!"

#range(): Generates a sequence of numbers.
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

#max(), min(): Returns the maximum or minimum value from a sequence.
numbers = [1, 2, 3, 4, 5]
print(max(numbers))  # Output: 5
print(min(numbers))  # Output: 1

#sum(): Returns the sum of a sequence of numbers.
print(sum(numbers))  # Output: 15

