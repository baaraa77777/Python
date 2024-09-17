#WAP to find the remaining days, weeks and months in your life.

your_age=input('Enter your age: ')
remaining_age=90-int(your_age)

days_left=remaining_age*365
weeks_left=remaining_age*52
months_left=remaining_age*12

print(f"You have {days_left}days, {weeks_left}weeks and {months_left}months left.")