import random

# List of random syllables to generate nonsense words
syllables = ['bli', 'blu', 'bra', 'cri', 'cro', 'dra', 'dro', 'fla', 'flo', 'gra', 'gro', 'pli', 'plo', 'sli', 'slo', 'tra', 'tro']

def generate_nonsense_word():
    return random.choice(syllables) + random.choice(syllables) + random.choice(syllables)

def play_game():
    print("Welcome to the Silly Word Generator Game!")
    print("In this game, you'll have to guess the magic word.")
    print("But beware... it's complete nonsense!")

    # Generate a list of nonsense words
    words = [generate_nonsense_word() for _ in range(5)]
    
    # Randomly select one word as the "magic word"
    magic_word = random.choice(words)
    
    print("\nHere are your nonsense words:")
    for i, word in enumerate(words):
        print(f"{i + 1}. {word}")
    
    # Get the player's guess
    guess = input("\nWhich word do you think is the magic word? (Enter the number): ")
    
    try:
        guess_index = int(guess) - 1
        if words[guess_index] == magic_word:
            print(f"\nCongratulations! {words[guess_index]} was the magic word! You win!")
        else:
            print(f"\nOops! The magic word was actually {magic_word}. Better luck next time!")
    except:
        print("\nThat's not a valid number. Game over!")

if __name__ == "__main__":
    play_game()
