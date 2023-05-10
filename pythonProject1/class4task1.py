kg = 56
m = 1.76
bmi = (kg / (m * m))
if bmi > 35:
    print("Your BMI is", bmi, "so you are obese")
elif bmi > 25:
    print("Your BMI is" , bmi , "so you are overweight")
elif bmi < 18.5:
    print("Your BMI is" , bmi , "so you are underweight")
else:
    print("Your BMI is", bmi, "so you are healthy")
