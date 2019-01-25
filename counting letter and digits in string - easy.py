'''
Python program to chceck the number of digits and letters in the string
'''
import string

from string import ascii_lowercase as asc_lower
from string import ascii_uppercase as asc_upper

test = input("Enter the string: ")

import string  


alpha = 0
num = 0

for char in test:
  if char in set(asc_lower) or char in set(asc_upper):
    alpha += 1
  elif char in string.digits:
    num += 1
  else:
    pass
  
print("alphbets: ",alpha)
print("number: ",num)



