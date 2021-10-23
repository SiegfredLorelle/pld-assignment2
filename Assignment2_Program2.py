"""Create a program that will ask how many apples and oranges you want to buy.
Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
Display the output in the following format.
The total amount is ______.
"""
import sys

print ("Good Day!")
NumApple = int(input("How many APPLES would you like to buy?  "))
NumOrange = int(input("How many ORANGES would you like to buy?  "))

TotalPrice = ((NumApple * 20) +
                (NumOrange * 25))

print (f"The total amount is {TotalPrice} pesos.")


