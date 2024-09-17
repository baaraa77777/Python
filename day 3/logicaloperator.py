#ROLLERCOASTER.4.O

height=int(input("What is your height in cm? "))

if height >=120:
    print("You can ride the rollercoaster. ")

    age=int(input("Enter your age: "))
    if age<12:
        bill = 5
        print(f"Child tickets are ${bill}. ")

    elif age<=18:
        bill = 7
        print(f"Youth tickets are ${bill}. ")

    elif age >=45 and age <= 55:
        print("You get a free ticket. ")    

    else:
        bill = 12
        print(f"Adults tickets are ${bill}. ")

    photo=input("Do you want to take photo? Y or N. ")

    if photo == "Y":
        bill +=3

    print(f"Your final bill is ${bill}.")

           
else:
    print("Sorry! you have to grow taller to ride a rollercoaster. ")