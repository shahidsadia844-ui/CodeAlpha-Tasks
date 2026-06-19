import random

def play_hangman():
    # 1. Predefined 5 words ki list
    words_list = ["python", "coding", "laptop", "github", "program"]
    
    # Randomly ek word select karna
    secret_word = random.choice(words_list)
    guessed_letters = []
    attempts_left = 6  # Limit incorrect guesses to 6

    print("--- Welcome to Hangman Game! ---")
    print(f"Guess the word! It has {len(secret_word)} letters.")

    # Game Loop
    while attempts_left > 0:
        # Word ka display status check karna (jaise p _ t h _ n)
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\nWord: " + display_word.strip())
        print(f"Attempts left: {attempts_left}")
        
        # Agar saare letters guess ho gaye hain
        if "_" not in display_word:
            print("\n🎉 Congratulations! You won! You guessed the word correctly.")
            break

        # User se input letter lena
        guess = input("Guess a letter: ").lower().strip()

        # Input ki basic validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one!")
            continue

        # Letter ko guessed list mein add karna
        guessed_letters.append(guess)

        # Check karna ke letter secret word mein hai ya nahi
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Wrong guess! '{guess}' is not in the word.")
            attempts_left -= 1

    # Agar attempts khatam ho jayein
    if attempts_left == 0:
        print(f"\n💥 Game Over! You ran out of attempts. The secret word was: '{secret_word}'")

if __name__ == "__main__":
    play_hangman()
