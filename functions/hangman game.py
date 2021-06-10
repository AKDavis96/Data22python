word = input("Enter your word here ")
word = word.lower()
print(len(word) * "_")
lives = 10
list_correct = []
list_incorrect = []
hidden_word = len(word) * "_"


def reveal_letter(letter_picked, word_to_guess, underscore_word):
    counter = 0
    underscore_word_list = list(underscore_word)
    for letter in word_to_guess:
        if letter == letter_picked:
            underscore_word_list[counter] = letter_picked
        counter += 1
    return ''.join(underscore_word_list)


while lives > 0:
    guess = input("Guess a letter ")
    guess = guess.lower()
    if guess.isalpha() is False:
        print("You must guess a letter")
    elif guess in list_correct or guess in list_incorrect:
        print("You have already guessed this letter")
    elif len(guess.strip()) > 1:
        print("You can only guess one letter at a time")
    elif guess.strip() in word:
        print("correct")
        print(f"You have {lives} lives remaining")
        list_correct.append(guess)
        hidden_word = (reveal_letter(guess, word, hidden_word))
        print(hidden_word)
        if hidden_word == word:
            print(f"Well done you guessed it! The word was {word}")
            break
    else:
        print("incorrect")
        lives -= 1
        print(f"You have {lives} lives remaining")
        list_incorrect.append(guess)
if lives == 0:
    print("Out of lives, better luck next time!")





