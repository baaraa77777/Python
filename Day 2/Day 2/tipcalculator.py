
print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))


total_bill=total_bill+(tip*total_bill/100)
each_person_bill=total_bill/5

final_bill="{:.2f}".format(each_person_bill)

print(f"Each person should pay ${final_bill}")