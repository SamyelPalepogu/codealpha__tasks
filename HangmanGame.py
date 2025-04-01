import random

def get_word():
    word_list = [
        "python", "hangman", "programming", "internship", "developer",
        "algorithm", "function", "variable", "exception", "inheritance",
        "polymorphism", "encapsulation", "abstraction", "recursion", "iteration",
        "syntax", "debugging", "compilation", "interpreter", "compiler"
    ]
    return random.choice(word_list)

def display_state(guessed_word, guessed_letters, attempts_left):
    print("\nWord: " + " ".join(guessed_word))
    print("Guessed Letters:", ", ".join(guessed_letters))
    print(f"Attempts Left: {attempts_left}")

def play_game():
    word = get_word()
    guessed_word = ["_"] * len(word)
    max_attempts = 6
    attempts = 0
    guessed_letters = []

    print("Welcome to Hangman!")

    while attempts < max_attempts and "_" in guessed_word:
        display_state(guessed_word, guessed_letters, max_attempts - attempts)
        
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input! Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed_word[idx] = guess
            print("Good guess!")
        else:
            attempts += 1
            print("Wrong guess!")
        guessed_letters.append(guess)

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()