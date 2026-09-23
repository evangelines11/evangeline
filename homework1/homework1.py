# File: homework1.py
# --- Variables and Data Types --- 
a = 10
print (a)
print(type(a)) # a is an integer, a whole number with no decimals
b = 1.5
print (b)
print(type(b)) # b is a float, a number with a decimal
c = 3j
print (c)
print(type(c)) # c is a complex, a number with an imaginary part
d = "hello"
print (d)
print(type(d)) # d is a string, words or text
e = [1, 2, 3]
print (e)
print(type(e)) # e is a list, an ordered collection of items
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print (f)
print(type(f)) # f is a dictionary, key-value pairs
g = (1, 2)
print (g)
print(type(g)) # g is a tuple, an immutable collection
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, an ordered collection of items
i = True
print (i)
print(type(i)) # i is a boolean, representing true or false
j = None
print(j)
print(type(j)) # j is a NoneType, a null value or no value at all
k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, an ordered collection of items
l = str(14)
print(l)
print(type(l)) # l is a string, words or text
m = 1e4
print(m)
print(type(m)) # m is a float, fractional numbers or numbers with decimals
# Question 1: I found 9 different data types
# Question 2: Datatypes: list, float, integer, nonetype, boolean, string, dictionary, complex, and tuple.
# Question 3: Variables b and m, d and l, and e,h, and k have the same data types.
# Question 4: The data type of l was a string because str() is a functio that converts the value 14 into a string data type.
# Question 5: Set data type
n = {2, 12, 6}
print(n)
print(type(n)) # n is a set, a collection of unique items
# --- 3.2 Booleans ---
print (10 >9) # True, 10 is greater than 9
print (10 == 9) # False, 10 does not equal 9
print (10 <= 9) # False, 10 is not less than or equal to 9
print (bool("abc")) # True, abc is a non-empty string
print (bool(123)) # True, 123 is a non-zero number
print(bool(["apple", "cherry", "banana"])) # True, the list has content
print(bool(True)) # True, true is defined as true
print(bool(False)) # False, false evaluates to false
print(bool(0)) # False, the number 0 is an empty value
print(bool('')) # False, it is an empty value
print(bool(" ")) # True, the space adds content
print(bool(())) # False, it is an empty value
print(bool([])) # False, it is an empty value
print(bool({})) # False, it is an empty value
print(bool(True and False)) # False, if false is on one side it is all false
print(bool(True and True)) # True, it is all true
print(bool(False and False)) # False, it is all false
print(bool(True or False)) # True, if one side is true then it is all true
print(bool(True or True)) # True, it is all true
print(bool(False or False)) # False, it is all false
print(bool(not(False))) # True, it is not false
print(bool(not(True))) # False, it is not true
# Question 1: If True is in it, then the entire thing is true.
# Question 2: I didn't think the empty space in bool(" ") would count as content.
# Question 3: False or True is an expression that is true because when it says "or" the response is true if true is included.
# Question 4: False and True will return as false because when it says "and" the response is false if false is included.
# --- 3.3 Operators ---
# --- Arithmetic Operators ---
print(10+5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print(6 / 3) # 2, / performs division
print(5 % 2) # 1, % returns the remainder of a division
print (3 ** 2) # 9, ** performs exponents
print(15 // 2) # 7, // performs floor division
# --- Comparison Operators ---
print(5 == 2) # False, == means "equal to"
print(10 != 10) # False, != means "not equal to"
print(2 < 5) # True, < means less than
print(12>5) # True, > means greater than
print(5 <= 6) # True, <= means less than or equal to
print(1 >= 10) # False, >= means greater than or equal to
# --- Assignments Operators ---
x = 5
x += 5
print (x) # 10, += adds 5
x = 5
x -= 4
print (x) # 1, -= subtracts 4
x = 5
x *= 3
print (x) # 15, *= multiplies 5 by 3
# --- Logical Operators ---
# Question 1: The operator and evaluates two expressions. The result is only true if both expressions are true. True and True will result in True. True and False will result in False.
# Question 2: The operator or evaluates two expressions. The result is only false if both expressions are false. True or false results in true. False or False results in false.
# Question 3: The operator not turns True into False and False into True. 2 != 3 results in True because it is true that 2 does not equal 3. 2 != 2 results in False because it is not true that 2 does not equal 2.
# --- More Questions ---
# Question 1: / refers to divison while // refers to floor division which means it rounds the result.
# Question 2: % gives a remainder in division while // rounds.
# Question 3: I would use the % operator. Ex. 10 % 4 = 2
# Question 4: Assignment operators assign a value to a variable.
# --- 3.4 Strings ---
my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # Prints: h
print(my_string[1]) # Prints: e
print(my_string[2]) # Prints: l
print(my_string[3]) # Prints: l
print(my_string[4]) # Prints: o
print(my_string[-1]) # Prints: o
print(my_string[1:3]) # Prints: el
print(my_string[0:5:2]) # Prints: hlo
print(len(my_string)) # Prints: 5
print(my_string + "goodbye") # Prints: hellogoodbye
print(my_string * 7) # Prints: hellohellohellohellohellohellohello
# Question 1: Slicing means to access specific portions of a string. I sliced the string in the 8th and 9th manipulation.
# Question 2:
name = "Oski"
print("Hello, my name is", name) # Prints: Hello, my name is Oski
# Question 3:
name = "Oski"
print(f"Hello, my name is {name}") # Prints: Hello, my name is Oski
# Question 4: The first print statement included the name=Oski variable manually while the second print statement used f-strings to include the variable. 
# --- 3.5 Terminal Commands ---
# cd
# Changes directories. Use it to move from one folder to another
# Example: cd Desktop
# ls
# list: lists files inside your current folder
# Example: ls /python_decal_fa26/
# ls -a
# Lists all files and folders in directory including hidden files
# Example: ls -a
# mkdir
# Make directory. Used to make new directories.
# Example: mkdir pythonhomework
# cat
# Concatenate: It displays the contents of a file.
# Example: cat file.png
# pwd
# Print working directory. It displays the entire path of your current working directory from the root directory.
# Example: pwd
# cd ..
# It moves up one to a parent directory.
# Example: If you want to move one level up: cd .. 
# cd .
# It keeps you in your current working directory.
# Example: cd .
# cd ~
# It changes you to the home directory.
# Example: If your're in a different directory and want to go to your home directory just type cd ~
# cp
# copy a file or directory
# Example: cp file1.png file2.png
# mv
# It is used to move or rename files and directories.
# Example: mv screenshot1.png hw2.png
# rm
# It removes or deletes files and directories.
# Example: rm screenshot.png
# clear
# It is used to clear the terminal screen.
# Example: type clear and then press enter
# grep
# Global regular expression print. It is used to search for specific text such as words inside of files.
# Example:  grep "decal" python.txt
# Question 1: round command: used to round digits. len command: used to get the number of items in an object. find () command is used to search for a substring in a string.
# Question 2: ls lists the files in your current directory and ls -a lists all files even hidden ones.
# Question 3: Hidden files are files not shown by default and they are usually system files.
# Question 4: python -c: used to run a single python command. python -m: used to run a module as a script. python -x: used to ignore first line of a script.
