print("Hi and welcome to money converter! Remember, this is a beta, some features might not work! Right now, we only have, ron, euro and dollars.")
print("Made by @ImYinNoYang")
print("Please select one of the following services:")
print("1. Euro to ron")
print("2. Ron to euro")
print("3. Dollars to ron")
print("4. Ron to dollars")
print("5. Euro to dollars")
print("6. Dollars to euro")
print("7. Pounds Sterling in Ron")
print("8. Ron in Pounds Sterling")
print("9. Pounds Sterling in Euro")
print("10. Euro in Pounds Sterling")
print("11. Pounds Sterling in Dollars")
print("12. Dollars in Pounds Stering")
inp=int(input("Type here the number of your selection: "))

if inp == 1:
    inp=int(input("Type the amount of money to convert, only natural numbers: "))
    print(inp * 4.93, "Ron")
elif inp == 2:
    inp=int(input("Type the amount of money to convert, only natural numbers: "))
    print(inp * 0.20, "Euro")
elif inp == 3:
    inp=int(input("Type the amount of money to convert, only natural numbers: "))
    print(inp * 4.09, "Ron")
elif inp == 4:
    inp=int(input("Type the amount of money to convert, only natural numbers: "))
    print(inp * 0.24, "Dollars")
elif inp == 5:
    inp=int(input("Type the amount of money to convert, only natural numbers: "))
    print(inp * 1.20, "Dollars")
elif inp == 6:
    inp=int(input("Type the amount of money to convert, only natural numbers: "))
    print(inp * 0.83, "Euro")
elif inp == 7:
    inp=int(input("Type the amount of money to convert, only natural numbers: "))
    print(inp * 5.66, "Ron")
elif inp == 8:
    inp=int(input("Type the amount of money to convert, only natural numbers: "))
    print(inp * 0.18, "Pounds Sterling")
elif inp == 9:
    inp=int(input("Type the amount of money to convert, only natural numbers: "))
    print(inp * 1.15, "Euro")
elif inp == 10:
    inp=int(input("Type the amount of money to convert, only natural numbers: "))
    print(inp * 0.87, "Pounds Sterling")
elif inp == 11:
    inp=int(input("Type the amount of money to convert, only natural numbers: "))
    print(inp * 1.38, "Dollars")
elif inp == 12:
    inp=int(input("Type the amount of money to convert, only natural numbers: "))
    print(inp * 0.72, "Pounds Sterling")
else:
    print("Error! Please select one of the options above!")

#MADE BY ImYinNoYang