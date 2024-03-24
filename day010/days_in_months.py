def is_leap(year):
  return (0 == year % 4) and ((not (0 == year % 100)) or (0 == year % 400))


# TODO: Add more code here 👇
def days_in_month(year, month):
  days = 0
  if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
  elif month in [4, 6, 9, 11]:
    days = 30
  else:
    days = (29 if is_leap(year) else 28)

  return days


#🚨 Do NOT change any of the code below
year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)
