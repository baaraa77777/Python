#Prime number checker

def prime_check(num):
    count = 0
    for i in range (2, num + 1):
        if num % i == 0 :
             count += 1
    if count == 1:
        print(f"{num} is a prime number.")
    else :
        print(f"{num} isn't a prime number. ")

n= int(input("Check this number: "))
prime_check(num=n)