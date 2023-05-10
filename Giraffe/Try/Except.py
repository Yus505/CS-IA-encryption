

try:
    number = int(input("Enter a number: ")
    print(number)
except ZeroDivisionError as err:
    print("Invalid Input")
except ValueError:
    print("Invalid input")