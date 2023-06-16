student_heights = input("Enter the heights of the students: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

total_student = 0
for student in student_heights:
    total_student += 1

average_height = round(total_height/total_student)

print("The average height of the students in the class is:" , average_height)



