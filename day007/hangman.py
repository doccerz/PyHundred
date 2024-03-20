# import modules
import hangman_art as ha
import hangman_words as hw
import random

# Display logo
print(ha.logo)

# Initialize game flag
quit_game = False

while not quit_game:
  # Initialize game variables
  lives = 6
  player_win = False
  # Get a random word
  chosen_word = random.choice(hw.word_list).upper()

  # Initialize display
  display = ["_" for i in range(0, len(chosen_word))]

  ## Show hint
  print(f"Hint: {chosen_word}")

  # While lives > 0, ask for a letter
  while lives > 0 and not player_win:
    # Clear
    # Display hangman art
    print(ha.stages[lives])
    # Display the number of blanks
    print(f"{' '.join(display)}")
    # Ask for a letter
    guess = input("Guess a letter: ").upper()

    # If letter is in the word,
    if guess in chosen_word:
      # If letter is already guessed,
      if guess in display:
        print("You have already guessed this letter.")
      # Else
      else:
        # Replace the blank with the letter
        for i in range(0, len(chosen_word)):
          display[
              i] = chosen_word[i] if chosen_word[i] == guess else display[i]

        # If all blanks are filled,
        player_win = "_" not in display

    # Else
    else:
      # Decrease lives by 1
      lives -= 1
      # Print minus lives
      print(f"You guessed {guess}, that's not in the word. You lose a life.")

  # Show final art
  print(ha.stages[lives])
  # Show the word
  print(f"{' '.join(display)}")
  # Show the result
  print("You lose." if lives == 0 else "You win.")

  # Ask if the player wants to play again
  quit_game = ("N" == input("Do you want to play again? (Y/N)").upper())
