import random

#Number Guessing Game Objectives:

# Include an ASCII art logo.
art = """
 _______               ___.                              
 \      \  __ __  _____\_ |__   ___________              
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \             
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/             
\____|__  /____/|__|_|  /___  /\___  >__|                
        \/            \/    \/     \/                    
  ________                            .__                
 /  _____/ __ __   ____   ______ _____|__| ____    ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\ 
\    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  >
 \______  /____/  \___  >____  >____  >__|___|  /\___  / 
        \/            \/     \/     \/        \//_____/  
  ________                                               
 /  _____/_____    _____   ____                          
/   \  ___\__  \  /     \_/ __ \                         
\    \_\  \/ __ \|  Y Y  \  ___/                         
 \______  (____  /__|_|  /\___  >                        
        \/     \/      \/     \/                         
"""

print(art)
print("Welcome to the number guessing game!!!!")

play_again = True

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
difficulty = input("Please choose difficulty level: 'easy' or 'hard'? ")
turns = (10 if difficulty == "easy" else 5)

while (play_again):
    print("I'm thinking of a number between 1 and 100.")
    num = random.randint(1, 100)

    for turn in range(1, turns + 1):
        # Allow the player to submit a guess for a number between 1 and 100.
        guess = int(input(f"Make a guess ({turn}/{turns}): "))

        # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
        if guess == num:
            # If they got the answer correct, show the actual answer to the player.
            print(f"You guessed correctly: {num}")
            break
        else:
            # Track the number of turns remaining.
            if guess > num:
                print("Too high.")
            else:  #if guess < num
                print("Too low")

    # If they run out of turns, provide feedback to the player.
    if turn >= turns:
        print("You've run out of guesses, you lose.")

    play_again = input(
        "Do you want to play again? 'y' or 'n'? ").lower() == 'y'
