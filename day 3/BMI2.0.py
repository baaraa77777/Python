#Body Mass Index

height=input('Enter your height in meters: ')
weight=input('Enter your weight in kg: ')

BMI=float(weight)/float(height)**2

result=int(BMI)

if result<18.5:
    print(f"Your BMI is {result}, you're underweight. ")
elif result<25:
    print(f"Your BMI is {result}, you're normal weighted. ")
elif result <30:
    print(f"Your BMI is {result}, you're overweight. ")
elif result<35:
    print(f"Your BMI is {result}, you're obese. ")
else:
    print(f"Your BMI is {result}, you're clinically obese. ")


