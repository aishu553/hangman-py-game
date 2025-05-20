import random
import time
import sys
from colorama import Fore, Style, init
from playsound import playsound

init(autoreset=True)

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def rainbow_text(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    result = ''
    for i, char in enumerate(text):
        result += colors[i % len(colors)] + char
    return result + Style.RESET_ALL

def get_random_word():
    word_categories = {
        'Life':['happy','sad','disappoinment','excitement','betrayal'],
        'Technology': ['python', 'computer', 'internet', 'programming', 'developer'],
        'Space': ['galaxy', 'nebula', 'planet', 'comet', 'astronaut'],
        'Animals': ['elephant', 'kangaroo', 'dolphin', 'penguin', 'giraffe']
    }
    category = random.choice(list(word_categories.keys()))
    word = random.choice(word_categories[category])
    return word, category

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def print_hangman(tries):
    stages = [
        '''
        😵  You hanged him...
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ''',
        '''
        😨  He’s barely hanging on!
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        ''',
        '''
        😟  He's in danger!
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        ''',
        '''
        😬  This is getting serious.
           ------
           |    |
           |    O
           |   /|
           |    
           |
        ''',
        '''
        😧  He’s worried...
           ------
           |    |
           |    O
           |    |
           |    
           |
        ''',
        '''
        😐  Just started...
           ------
           |    |
           |    O
           |    
           |    
           |
        ''',
        '''
        🙂  All good for now!
           ------
           |    |
           |    
           |    
           |    
           |
        '''
    ]
    print(Fore.YELLOW + stages[6 - tries])

def hangman():
    word, category = get_random_word()
    guessed_letters = set()
    attempts_left = 6

    print(Fore.CYAN + Style.BRIGHT + "\n🎮 WELCOME TO THE LEGENDARY HANGMAN GAME\n")
    slow_print("Choosing a secret word", 0.1)
    for _ in range(3):
        slow_print(".", 0.4)

    print(Fore.MAGENTA + f"\n📂 Category: {category}")
    print(Fore.CYAN + f"🔍 Your mission: Guess the {len(word)}-letter word.")

    while attempts_left > 0:
        print_hangman(attempts_left)
        print("\n" + Fore.GREEN + "Word: " + display_word(word, guessed_letters))
        print(Fore.MAGENTA + f"✨ Guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None yet'}")
        print(Fore.BLUE + f"❤️ Attempts Left: {attempts_left}\n")
        
        guess = input(Fore.CYAN + "👉 Your Guess: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            slow_print(Fore.RED + "⚠️ Please enter a single alphabet letter.", 0.02)
            continue

        if guess in guessed_letters:
            slow_print(Fore.YELLOW + "🔁 You already guessed that. Try something else!", 0.02)
            continue

        guessed_letters.add(guess)

        if guess in word:
            playsound('correct.wav')
            slow_print(Fore.GREEN + "✅ Great guess!", 0.02)
        else:
            playsound('wrong.wav')
            attempts_left -= 1
            slow_print(Fore.RED + "❌ Nope, that’s not in the word.", 0.02)

        if all(letter in guessed_letters for letter in word):
            playsound('win.wav')
            print_hangman(attempts_left)
            slow_print("\n🎉 YOU WON!", 0.06)
            print(rainbow_text(f"🥳 The word was: {word.upper()}"))
            return

    # Game Over
    playsound('lose.wav')
    print_hangman(attempts_left)
    slow_print(Fore.RED + Style.BRIGHT + "\n💀 GAME OVER! The word was: " + word.upper(), 0.05)
    slow_print("Better luck next time!", 0.05)

if __name__ == "__main__":
    hangman()
