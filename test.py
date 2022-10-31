from ast import Not
from re import T

name = input("please enter your name = ")

if len(name) < 3 :
    print("name must be at least 3 characters")
elif len(name) > 50 :
    print("name can be a maximum of 50 character")
else:
    print("name looks good!")