from portfolio_project_pkg import word_dictionaries, account_creation 
import random

#GUI
def show_homepage():
    print("""
     === Competitive WordJumble  ===
    -------------------------------------
    |         1. Login to PLAY!          |
    -------------------------------------  
    | 2. Register   | 3. Record holders |
    -------------------------------------  
    | 4. How to play | 5. Exit          |
    -------------------------------------  
 """)
    
#variables
database = {}
gamers_scores = {}

class Winner_Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, name, score):
        # Add the new score to the queue
        self.items.append((name, score))
        # Sort the queue based on scores in descending order
        self.items.sort(key=lambda x: x[1], reverse=True)
        # Keep only the top 10 scores
        self.items = self.items[:10]

    def show_queue(self):
        print("Top 10 Players:")
        for i, (name, score) in enumerate(self.items[:10], start=1):
            print(f"{i}th Place: {name} - Score: {score}")

wq = Winner_Queue()

#Word Jumble
class_based_word_lists = [word_dictionaries.level_one, word_dictionaries.level_two, word_dictionaries.level_three, word_dictionaries.level_four, word_dictionaries.level_five]
from random import shuffle     
class JumbleGame:
    def __init__(self, word_list):
        self.word_list = word_list
        
    def user_guess(self):
        word = random.choice(self.word_list)
        word_characters = list(word)
        random.shuffle(word_characters)
        shuffled_word = ''.join(word_characters)
        print(shuffled_word)
        print("You have three guesses to unjumble the word. Type 'exit' to quit.") 
        attempts = 0
        while attempts < 3:
            guess = input("Your guess is: ").lower()
            if guess == "exit":
                return None 
            elif guess == word:
                print(f"Congratulations! You guessed '{word}' correctly!")
                return True
            else:
                print("Sorry, you got it wrong")
                attempts += 1
        return False

def game_progression():
    index = 0
    level = 1
    while index < len(class_based_word_lists):
        JG_instance = JumbleGame(class_based_word_lists[index])
        result = JG_instance.user_guess()
        if result is None:  
            print("Exiting the game.")
            break
        elif result:
            index += 1
            level += 1
            if index == len(class_based_word_lists):
                print("YOU BEAT THE GAME!!!")
            elif index == 1:
                print("You completed Level One!!!")
            elif index == 2:
                print("You completed Level Two!!")
            elif index == 3:
                print("You completed Level Three!!!")
            elif index == 4:
                print("You completed Level Four!!!")
        else:
            print("You failed to guess the word correctly three times. You'll have to start over.")
            if index > 0:
                index -= 1
            if index < 0:
                index = 0
            break  #

    gamers_scores[username] = level  




#GUI interaction code
while True:
    show_homepage()
    choose_option = (input("Input your selection from the Homepage:  ")).lower() 
    if choose_option == "1" or choose_option == "login":
        while True:
            username = input("Please enter your username:  ")
            if username.isalpha():
                break  
            else:
                print("Please enter letters only for your username.")
        
        password = input("Please enter your password:  ")
        if account_creation.login(database, username, password):
            game_progression()
            break  
            
    elif choose_option == "2" or choose_option == "register":
        while True:
            username = input("Please enter your username:  ")
            if username.isalpha():        
                password = input("Please enter your password:  ")
                account_creation.register(database, username, password)
                game_progression()
                break  
            else:
                print("Please enter letters only for your username.")
     
    elif choose_option == "3" or choose_option == "record holders":
        if gamers_scores:  # Check if gamers_scores dictionary is not empty
            for username, score in gamers_scores.items():
                wq.enqueue(username, score)
                wq.show_queue()
        else:
            print("No records available. Play the game to be listed!")

    elif choose_option == "4" or choose_option == "how to play":
        print(f'''
        The object of this game is to get to the top of the leader board by unscrambling the most words and advancing to the next level. 
        There are 5 levels. You start at level 1. After you get three scrambled words...unscrambled, you move to the next level.
        You get three tries for each word. If you get three words incorrect, you have to return to the previous level.
        If you finish all 5 levels you will be added to the Winner's Board. Note: You can enter "exit" to exit the game at any time.      
''')
    elif choose_option == "5" or choose_option == "exit":
            print("Goodbye.")
            break
    else:
        print("Please select an option from the homepage.")





