import art as a
import random

from game_data import data

# Print splash
print(a.logo)

# Ask if play
play = (input("Would you like to play a game of Higher Lower? 'y' or  any? ").
        lower() == 'y')

# If play, set data1 and data2
if play:
    random.shuffle(data)
    data1 = data.pop()
    data2 = data.pop()

# Loop if play
num_guess = 0
while play:
    # data1 has x followers vs data2 has higher/lower followers than data1
    print(data1['name'] + ", a/an " + data1['description'] + " from " +
          data1['country'] + " has " + str(data1['follower_count']) +
          " followers.")
    print(a.vs)

    # Ask the user to guess which one has the higher follower
    guess = input(data2['name'] + ", a/an " + data2['description'] + " from " +
                  data2['country'] +
                  " has [h]igher / [l]ower followers? ").lower()

    if ((guess == 'h' and data2['follower_count'] > data1['follower_count']) or
        (guess == 'l' and data2['follower_count'] < data1['follower_count'])):
        print("Correct!")
        num_guess += 1
    else:  # guess == 'l' and data2['follower_count'] < data1['follower_count']:
        print("Incorrect! " + data2['name'] + " has " +
              str(data2['follower_count']) + " followers! Game over.")
        play = False

    # New round data
    data1 = data2

    try:
        data2 = data.pop()
    except IndexError as e:
        print("No more data to play with! Game over.")
        play = False

# Show results
print(f"You guessed {num_guess} correctly!")
