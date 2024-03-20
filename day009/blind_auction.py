import art
from replit import clear


# Initialize variables
bidders = {}
continue_bid = True

# Show splash
print(art.logo)
print("Welcome to the Toph the blind auction!!!")

while continue_bid:
  # Ask for name
  bidder_name = input("What is your name? ")

  # Ask for bid
  bid_amount = int(input("What is your bid? $"))

  # Add bidder to dictionary
  bidders[bidder_name] = bid_amount

  # Ask if more bidders
  continue_bid = input("Are there any other bidders? [Y]es or type any key to end: ").upper() in ['Y', 'YES']

# Get highest bidder
winner = max(bidders, key=bidders.get)
print(f"The item goes to: {winner}")
