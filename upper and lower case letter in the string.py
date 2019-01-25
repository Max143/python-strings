'''
Python Program to Count Number of Lowercase and upper Characters in a String
'''

# without using any built in function
small = 'abcdefghijklmnopqrstuvwxyz'
capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

string = input("Enter the string with mix of case-letters: ")

countsmall = 0
countcapital = 0

for i in string:
  if i in small:
    countsmall += 1
  elif i in capital:
    countcapital += 1
  else:
    pass


print("Small: ", countsmall)
print("capital: ", countcapital)

# same program with using built in function 

import string

string = input("Enter the string: ")
small = 0
capital = 0

for char in string:
  if (char.islower()):
    small = small + 1
  elif (char.isupper()):
    capital = capital + 1
  else:
    pass
print("Small: ", countsmall)
print("capital: ", countcapital)


    

