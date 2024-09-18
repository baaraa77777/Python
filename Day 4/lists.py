#Who will pay the bill??
import random

names_var = input("Give me everybody's name, separated by comma. ")

names = names_var.split(", ")

#get the total numbers from the list.
length = len(names)
print(names)

#Generate the numbers between  0 to last index
choice = random.randint(0, length-1)
print(choice)
person_who_will_pay = names[choice]

#person_who_will_pay = random.choice(names)
print(person_who_will_pay + " will pay the bill.")
