'''
Python Program to Remove the Characters of Odd Index Values in a String
'''

print(range(len("Manish")))

def modify(string):  
  final = ""   
  for i in range(len(string)):  
    if i % 2 == 0:  
      final = final + string[i]  
  return final
string=input("Enter string:")
print("Modified string is:")
print(modify(string))


# Alternate method


  
