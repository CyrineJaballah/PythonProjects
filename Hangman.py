import random

def hangman():
    words = ['python', 'hangman', 'computer', 'programming', 'game', 'developer']
    secret_word = random.choice(words)
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")
    print("Guess the secret word.")
    print("_ " * len(secret_word))

    while True:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            attempts += 1
            print("Wrong guess!")
            print_hangman(attempts)

        word_progress = ''
        for letter in secret_word:
            if letter in guessed_letters:
                word_progress += letter + ' '
            else:
                word_progress += '_ '

        print(word_progress)

        if "_" not in word_progress:
            print("Congratulations! You guessed the word.")
            break

        if attempts >= max_attempts:
            print("You have reached the maximum number of attempts.")
            print(f"The secret word was: {secret_word}")
            break

def print_hangman(attempts):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |
           |
           |
          ---
        ''',
        '''
           --------
           |      |
           |
           |
           |
           |
          ---
        '''
    ]
    print(stages[attempts])

hangman()
