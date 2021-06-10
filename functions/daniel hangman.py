# user inputs word
# hidden word is generated "_____"
# whilst the user has lives left,
    # guess a letter
    # if letter is in word and has not been guessed before,
        # then reveal the letter "_e___"
    # else if letter not in word, then take away a life
word_to_guess = input("Please pick a word to guess...")
wrong_counter = 0
max_lives = 10
previous_letters = []
hidden_word = ""
for letter in word_to_guess: # generates underscore hidden word
    hidden_word = hidden_word + "_"
print(hidden_word)


def reveal_letter(letter_picked, word_to_guess, underscore_word):
    counter = 0
    underscore_word_list = list(underscore_word)
    for letter in word_to_guess:
        if letter == letter_picked:
            underscore_word_list[counter] = letter_picked
        counter += 1
    return ''.join(underscore_word_list)


while wrong_counter <= max_lives and not hidden_word.isalpha(): # whilst the user has lives left
    guessed_letter = input("Please guess a letter...")
    if guessed_letter in previous_letters: # letter already picked
        print("Silly, you have already guessed this letter...")
        wrong_counter += 1
    elif guessed_letter in word_to_guess: # user picked letter in word
        print("correct")
        hidden_word = reveal_letter(guessed_letter, word_to_guess, hidden_word)
        print(hidden_word)
        previous_letters.append(guessed_letter)
    else: # user picks letter not in word
        wrong_counter += 1
        previous_letters.append(guessed_letter)
        print("This letter was not in the word, try again...")