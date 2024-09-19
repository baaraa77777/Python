#To find the even numbers from 1 to 100 including 1 and 100.

#total_sum = 0
#for num in range(2, 101, 2):
#    total_sum += num


total_sum = 0
for num in range(1, 101):
    if num % 2 == 0:
        total_sum += num

print(f"The total sum of even numbers from 1 to 100 is: {total_sum}")