import random

import hangman_words
chosen_word = random.choice(hangman_words.word_list)

import hangman_art 
print(hangman_art.logo)
lives =  6

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}.")
        
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -=1
        if lives ==0:
                end_of_game = True
                print('You lose.')
                print(f"The word is {chosen_word}.")
    print(hangman_art.stages[lives])
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
       
    
