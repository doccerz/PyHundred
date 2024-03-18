rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random


def get_key_from_value(input_dict, search_value):
  """Return the key for a given value in a dictionary."""
  for key, value in input_dict.items():
    if value == search_value:
      return key
  # If the value is not found, return None or raise an exception as per your requirement
  return None  # or raise ValueError("Value not found")


rsp = {0: rock, 1: paper, 2: scissors}

# map all scenarios
vs = [["Draw", "You lose", "You win"], 
      ["You win", "Draw", "You lose"],
      ["You lose", "You win", "Draw"]]

# player phase
player = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))

print(rsp[player])

# computer phase
computer = random.randint(0, 2)
print("Computer chose:")
print(rsp[computer])

# match result
print(vs[player][computer])
