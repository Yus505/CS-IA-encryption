age_as_int = int(input("How old are you?"))
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days to live , {weeks_remaining} weeks to live, {months_remaining} months to live and {years_remaining} years to live")