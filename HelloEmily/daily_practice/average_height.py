student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = sum(student_heights)
num_of_student = len(student_heights)

average_height = round(total_height / num_of_student)
print(average_height)