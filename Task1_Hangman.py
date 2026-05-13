import random

# simple word list for the task
words = ['python', 'codealpha', 'internship', 'computer', 'programming']
secret_word = random.choice(words)
guesses = []
lives = 6

print("Welcome to my Hangman Game!")

while lives > 0:
    # showing the word with underscores
    output = ""
    for char in secret_word:
        if char in guesses:
            output += char + " "
        else:
            output += "_ "
    
    print("\nWord: " + output)
    print("Mistakes left:", lives)
    
    if "_" not in output:
        print("Nice! You won.")
        break

    char_input = input("Enter a letter: ").lower()

    if char_input in guesses:
        print("You already tried that one.")
    elif char_input in secret_word:
        print("Yes! It's in there.")
        guesses.append(char_input)
    else:
        print("Nope, not in the word.")
        guesses.append(char_input)
        lives -= 1

if lives == 0:
    print("\nYou ran out of lives. The word was:", secret_word)