student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum = 0
for height in student_heights:
    sum += height

count = 0
for student in student_heights:
    count += 1

average_height = round(sum / count)
print(average_height)


