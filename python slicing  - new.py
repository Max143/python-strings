'''
python program to form a new string by taking first 2 charcter from start and 2 charcter from
end.
'''




string=input("Enter string:")

count=0

for i in string:
      count=count+1

      
new=  string[0:2]  +  string[count-2:count]


print("Newly formed string is:")
print(new)

# another method
print("My method")

string = input("Enter the string: ")

print(string[0:2] + string[len(string)-2 : len(string
