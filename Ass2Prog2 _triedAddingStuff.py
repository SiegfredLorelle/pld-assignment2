"""Create a program that will ask how many apples and oranges you want to buy.
Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
Display the output in the following format.
The total amount is ______.
"""
#2nd try. tried to avoid negative inputs

print()
print ("Good Day!!")
print ("An APPLE cost 20php and an ORANGE cost 25php.")
print()

NumApple = int(input("How many APPLES would you like to buy?  "))
NumOrange = int(input("How many ORANGES would you like to buy?  "))
print()

TotalApple = NumApple * 20
TotalOrange = NumOrange * 25
TotalAmount = TotalApple + TotalOrange

while NumApple < 0 or NumOrange < 0:
    print("You cannot buy NEGATIVE fruits.")
    print("Please try again.")
    print()
    
    NumApple = int(input("How many APPLES would you like to buy?  "))
    NumOrange = int(input("How many ORANGES would you like to buy?  "))
    print()
    TotalApple = NumApple * 20
    TotalOrange = NumOrange * 25
    TotalAmount = TotalApple + TotalOrange

print (f"An APPLE cost 20 php & you want x{NumApple} apple(s) then it would cost {TotalApple} php for the apple(s).")
print (f"An ORANGE cost 25 php & you want x{NumOrange} orange(s) then it would cost {TotalOrange} php for the orange(s).")
print()
print (f"The total amount is {TotalAmount} php.")
print()
