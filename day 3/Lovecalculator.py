print("Welcome to the love calculator.")

name1 = input("Enter your name: ")
name2 = input("Enter their name: ")

combined_name = name1 + name2
lower_str = combined_name.lower()

t = lower_str.count("t")
r = lower_str.count("r")
u = lower_str.count("u")
e = lower_str.count("e")

true = t + r + u + e

l = lower_str.count("l")
o = lower_str.count("o")
v = lower_str.count("v")
e = lower_str.count("e")

love = l + o + v + e

love_score = int(str(true)+ str(love))

if love_score <10 or love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos. ")

elif love_score >=40 and love_score <=50:
    print(f"Your love score is {love_score}, you are alright together. ")

else:
    print(f"Your love score is {love_score}.")