'''
Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

''''

# using built in functions
str1 = input("Enter a word: ")
str2 = input("Enter another word: ")

char1 = 0
char2 = 0

for char in str1:
  char1 += 1

for char in str2:
  char2 += 1


print("First word character count: ",char1)
print("Second word character count: ",char2)

if char1 > char2:
  print("Bigger string: ", str1)
else:
  print("Bigger string: ", str2)

print("Modified Program - write a program above program and exclude whitespace and only count characters")

# Without using built in function to find the solution 
# Removing whitespace from both string 

str1 = input("Enter the first string: ")
new1 = str1.replace(" ", "")


str2 = input("Enter the second string : ")
new2 = str2.replace(" ", "")


char1 = 0
char2 = 0

for i in new1:
    char1 += 1

for i in new2:
    char2 += 1

print("The largest character word is: ")
if char1 > char2:
    print(str1)
else:
    print(str2)

print("---------------------------------")
print("Without Using Built-in function")




    
































