paper1 = int(input("What was your Paper 1 grade?"))
paper2 = int(input("What was your Paper 2 grade?"))
IA = int(input("What was your IA grade?"))

final_grade = (paper1 * 0.45) + (paper2 * 0.25) + (IA * 0.3)
print(f"Your final grade will be {round(final_grade)}")
if final_grade < 3:
    print("You failed")
elif final_grade >=6:
    print("Excellent work")
else:
    print("Good job")w w