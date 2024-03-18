# Write your code here 👇
def decode(value, compare_value, result_if_match, result_if_no_match):
  return result_if_match if value == compare_value else result_if_no_match


def fizzbuzz(n):
  for i in range(1, n + 1):
    print((decode(i % 3, 0, "Fizz", "") + decode(i % 5, 0, "Buzz", "")) or i)


fizzbuzz(100)
"""
Instructions
You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

Your program should print each number from 1 to 100 in turn and include number 100.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

e.g. it might start off like this:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...etc

Hint
Remember your answer should start from 1 and go up to and including 100.

Each number/text should be printed on a separate line.
"""
