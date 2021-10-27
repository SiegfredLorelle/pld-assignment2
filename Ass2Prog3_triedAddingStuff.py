"""Create a program which you will enter the amount of money you have, 
it will also ask for the price of an apple.
Display the maximum number of apples that you can buy and 
the remaining money that you will have.
Display the output in the following format.
You can buy ___ apples and your change is ___ pesos.
"""

#2nd try. 
#added centavos. avoided negative price n money

print()
print("Good Day!!")
MoneyStart = float(input("How much money do you have?  "))
PriceApple = float(input("And How much is the price for an apple?  "))

#prevent negatives and zero currencies
while MoneyStart <= 0 or PriceApple <= 0 or PriceApple > MoneyStart:
    print()

    if MoneyStart <= 0 and PriceApple > 0:
        if MoneyStart == 0:
            print("You cannot buy with a ZERO balance!")
        else:
            print ("You cannot buy with a NEGATIVE balance!")

    elif PriceApple <= 0 and MoneyStart > 0:
        if PriceApple == 0:
            print("Apples are not for FREE!!")
        else:
            print ("Apples cannot be sold for a NEGTIVE price!")

    elif MoneyStart <= 0 and PriceApple <= 0:
        if MoneyStart == 0 and PriceApple == 0:
            print("No ZEROS please")
        else:
            print ("No NEGATIVE numbers please!")   

    elif PriceApple > MoneyStart:
        print("Sorry, you are too broke to buy an apple.") 

    print() 
    print("Please try again :)")

    MoneyStart = float(input("How much money do you have?  "))
    PriceApple = float(input("And How much is the price for an apple?  "))

#to make sure na two decimal lng and centavos
MoneyStart = round(MoneyStart,2)
PriceApple = round(PriceApple,2)

BoughtApple = MoneyStart // PriceApple
MoneyLeftNoDeci = int(MoneyStart % PriceApple) #int para d makuha ung centavo
MoneyLeftWithDeci = (MoneyStart % PriceApple)

#Final Ans
MoneyLeftCentavo = (MoneyLeftWithDeci - MoneyLeftNoDeci) * 100
MoneyLeftPesos = MoneyLeftNoDeci

print()
print(f"You can buy {BoughtApple:.0f} apples and your change is {MoneyLeftPesos} pesos and {MoneyLeftCentavo:.0f} centavos.")
print()
