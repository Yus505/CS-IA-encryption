import random

number1 = [1, 2, 3, 4 ,5 ,6 ,7, 8, 9]
number2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

number1_chosen = random.choice(number1)
number2_chosen = random.choice(number2)
print(f"What is {number1_chosen} * {number2_chosen}")
user_answer = int(input("Your answer:\n"))
actual_answer = int(number1_chosen * number2_chosen)
if user_answer == actual_answer:
    print("You are right")
else:
    print(f"You are wrong, the answer is {actual_answer}")
