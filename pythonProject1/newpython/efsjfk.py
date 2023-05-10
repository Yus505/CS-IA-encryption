import random
int_money = 100
possible_slots = ["cherry", "diamond", "star", "seven", "bell"]
wheel_choice1 = random.randint(possible_slots,4)
wheel_choice2 = random.randint(0,4)
wheel_choice3 = random.randint(0,4)
wheel_choice4 = random.randint(0,4)

print(possible_slots[wheel_choice1], possible_slots[wheel_choice2], possible_slots[wheel_choice3], possible_slots[wheel_choice4])

if wheel_choice1 == wheel_choice2 and wheel_choice3 == wheel_choice4:
    print(f"Congratulations you just won ${int_money * 4}")
else:
    print(f"You just lost money, and now you have ${int_money/2}")