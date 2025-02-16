import random

word_bank = ['apple', 'banana', 'rasberry', 'blueberry', 'strawberry']

word = random.choice(word_bank)

guessed_word = ['_'] * len(word)

attempts = 10

while attempts > 0:
   
    print('\nCurrent word: ' + ' '.join(guessed_word))

    guess = input('Guess a letter: ').lower()

    if len(guess) != 1 or not guess.isalpha():
        print('Invalid output. Please guess a single letter.')
        continue
   
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in guessed_word:
        print('\nCongratulations!! You guessed the word: ' + word)
        break
else:
    print('\nYou\'ve run out of attempts! The word was: ' + word)

