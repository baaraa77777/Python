#ROLLERCOASTER.2.O

height=int(input("What is your height in cm? "))

if height >=120:
    print("You can ride the rollercoaster. ")

    age=int(input("Enter your age: "))
    if age<12:
        print("You have to pay $5. ")
    elif age<=18:
        print("You have to pay $7. ")
    else:
        print("You have to pay $12. ")

else:
    print("Sorry! you have to grow taller to ride a rollercoaster. ")