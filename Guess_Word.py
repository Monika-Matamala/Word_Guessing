import random
print("Welcome to the Word Guessing Game !")
name = input("What is your name ?")
print("Good Luck !", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'java', 'swift', 'kotlin',
         'javascript', 'apple','developer','learning','machine',
         'deep','intelligence','artificial','vision','meta','tesla',
         'automated','robots','application','services','rip,''web']

word = random.choice(words)
attempts = 10
print("You have 10 attempts to guess the word.")
print("The Length of the word is ",len(word))
print("Guess the characters")

guesses = ''

while attempts > 0:

    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_",end=" ")
            failed += 1

    if failed == 0:
        print("\nCongratulations! You guessed the word:", word)
        break

    print()
    guess = input("Guess a character:")
    if guess in guesses:
        print("Oops! You already guessed that letter.")
        continue
    guesses += guess
    if guess in word:
        print("Good job! That letter is in the word.")


    if guess not in word:
        attempts -= 1
        print("Sorry, That letter is not in the word")
        print("You have", + attempts, 'more guesses')

        if attempts == 0:
            print("You ran out of attempts. The word was:", word)

