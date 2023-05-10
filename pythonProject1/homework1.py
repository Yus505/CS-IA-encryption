imported_amount = float(input("Enter the cost of the product: "))
if imported_amount > 300:
    print("The total amount you will spend is " , imported_amount * 1.32 ,"$")
else:
    print("The total amount you will spend is" , imported_amount ,"$")

print("And you get" , imported_amount * 0.18 * 0.15 ,"$" , "of VAT in return")