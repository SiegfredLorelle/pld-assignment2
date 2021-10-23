"""Create a program which you will enter the amount of money you have, 
it will also ask for the price of an apple.
Display the maximum number of apples that you can buy and 
the remaining money that you will have.
Display the output in the following format.
You can buy ___ apples and your change is ___ pesos.
"""


print("Good Day!!")
MoneyStart = int(input("How much money do you have?  "))
PriceApple = int(input("And How much is the price for an apple?  "))

BoughtApple = MoneyStart // PriceApple
MoneyLeft = MoneyStart % PriceApple

print(f"You can buy {BoughtApple} apples and your change is {MoneyLeft} pesos.")


