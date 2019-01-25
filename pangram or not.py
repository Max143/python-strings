'''
Python Program to Check if a String is a Pangram or Not
'''


import string

string = input("Enter a sentence: ")

for char in string:
  if char not in strings.ascii_letters:
    print("Pangram")
  else:
    print("Not pangram")

