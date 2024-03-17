"""
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

Warning. Do not change the code on line 1. Your program should work for different inputs. e.g. any two-digit number.

The last line of your program should print the result.
"""

two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
i = str(two_digit_number)
print(int(i[0]) + int(i[1]))
