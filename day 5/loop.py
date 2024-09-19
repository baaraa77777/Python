#To find the average of the heights of the students.

student_heights = input("Input a list of student heights ").split(", ")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

total_heights = 0
for height in student_heights:
    total_heights += height
print(total_heights)

avg = round(total_heights / len(student_heights))
print (avg)
