# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

leap_year_divide_4 = (year / 4) % 2
leap_year_divide_100 = (year / 100) % 2
leap_year_divide_400 = (year / 400) % 2

if leap_year_divide_4 == 0:
    if leap_year_divide_100:
        if leap_year_divide_400:
            print("Leap Year.")
        else:
            print("Not Leap Year.")
    else:
        print("Leap Year.")
else:
    print("Not Leap Year.")