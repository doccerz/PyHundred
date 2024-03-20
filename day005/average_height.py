# Input a Python list of student heights
student_heights = input().split()

# print(student_heights)

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# print(student_heights)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height = 0
num_students = 0
average = 0
iter_list = iter(student_heights)

try:
  while True:
    element = next(iter_list)
    # Process each element
    total_height += element
    num_students += 1
except StopIteration:
  None

average = round(total_height / num_students)

print(f"total height = {total_height}")
print(f"number of students = {num_students}")
print(f"average height = {average}")
"""
Instructions
You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

Example Input 1
156 178 165 171 187
In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

Example Output 1
total height = 857
number of students = 5
average height = 171
Example Input 2
151 145 179
Example Output 2
total height = 475
number of students = 3
average height = 158

"""
