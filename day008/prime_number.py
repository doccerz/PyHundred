import math

# Write your code below this line 👇
def prime_checker(number):
  is_prime = True
  if n <= 1:
      is_prime = False

  for i in range(2, int(math.sqrt(n)) + 1):
      if n % i == 0:
          is_prime = False

  print(f"It's{'' if is_prime else ' not'} a prime number.")



# Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)