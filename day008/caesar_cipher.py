import art
import caesar as c

# Show splash
print(art.logo)

# Ask for the word
word = input("Please enter the word to process: ")

# Ask for the process
process = input("Please enter the process to apply [E]ncrypt / [D]ecrypt: ")

# Ask for the shift
shift = int(input("Please enter the shift: "))

# Call function
print(f"The processed word is: {c.caesar(word, process, int(shift))}")
