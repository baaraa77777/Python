#To find the highest score of the students. 

student_scores = input("Input the list of scores of the students: ").split(', ')
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max = 0
for score in student_scores:
    if score < max:
        max= score
    #else:
     #   max= max

print (f'The highest score is {max}.')