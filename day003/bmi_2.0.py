"""
Instructions
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Equal to or over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.
"""

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height ** 2)
msg = "Your BMI is {}, you {}."


if bmi < 18.5:
  submsg = "are underweight"
elif 18.5 <= bmi < 25:
  submsg = "have a normal weight"
elif 25 <= bmi < 30:
  submsg = "are slightly overweight"
elif 30 <= bmi < 35:
  submsg = "are obese"
else:
  submsg = "are clinically obese"

print(msg.format(bmi,submsg))