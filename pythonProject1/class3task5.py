money_earned = 200
food_price = 100
entertainment =  50
price_of_2_shirts = 80
money = (money_earned - food_price - entertainment - price_of_2_shirts)
if money < 0:
    print("You are broke, you are in debt for" , money , "$")
else:
    print("You saved enough money, you have extra" , money , "$")
