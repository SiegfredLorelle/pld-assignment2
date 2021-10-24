
"""Create a program that will ask for name, age and address. 
Display those details in the following format.
Hi, my name is _____. I am ____ years old and I live in _____ .
"""
#2nd try. tried using while and if
#tried to avoid negative age

print ()
name    = input("Please enter your NAME:  ")
age     = int(input("Please enter your AGE:  "))


while age > 120 or age <= 0:   
    print()
    print(age, "is NOT a VALID AGE!!")                  
    age = int(input("Please enter your TRUE AGE:   "))
    print()

address = input("Please enter you address:  ")

print ()

if age == 1:                                    
    print (f"Hi, my name is {name}. I am {age} year old and I live in {address}. ")    
else: 
    print (f"Hi, my name is {name}. I am {age} years old and I live in {address}. ")
    
print ()