#If the bill was $150.00, split between 5 people, with 12% tip.
bill = float(input("Total bill: "))
tip = float(input("Tip percentage: "))
pax = int(input("Number of people: "))

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
share = round(float(bill) * (1 + float(tip) / 100) / pax, 2)

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Share per person is {}".format(share))
