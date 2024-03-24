student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
grades = {
    "Outstanding": [91, 100],
    "Exceeds Expectations": [81, 90],
    "Acceptable": [71, 80],
    "Fail": [0, 70],
}


def get_grade(score):
  for grade, score_range in grades.items():
    if score_range[0] <= score <= score_range[1]:
      return grade
  return 'Invalid Score'  # Handle cases outside the defined ranges


# TODO-1: Create an empty dictionary called student_grades.
# TODO-2: Write your code below to add the grades to student_grades.👇
student_grades = {
    key: get_grade(value)
    for key, value in student_scores.items()
}

# 🚨 Don't change the code below 👇
print(student_grades)
