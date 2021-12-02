import pygame
import random
from dictionary_search import Dictionary

# Main game logic class
class MainGame():

    def __init__(self, time_limit=60, genre='genre1', definition_penalty=10):
        self.time_limit = time_limit
        self.genre = genre
        self.definition_penalty = definition_penalty
        # TODO: Set up dictionary language
        self.dictionary = Dictionary()
        # TODO: Add genres as keys to dictionary and populate the value list with words
        self.words = {
            'Tools':[
                "Hammer","Brush","nails", "Bolt", "Screwdriver", "Wrench", "Nail-gun", "Chainsaw", "Mallet", "Plunger",
                "Jackhammer", "Toolkit",
            ],

            'animals':["Baboon", "Buffalo", "Cobra", "Crane", "Crow",
            "Dolphin", "Dragonfly", "Elephant", "Frog",
            "Goose", "Horse",
            "Jaguar", "Koala",
            "Magpie", "Mole", "Monkey", "Mosquito",
            "Pelican", "Penguin", "Pigeon", "Pony", "Porcupine", "Rabbit", "Raccoon", "Reindeer",
            "Seahorse", "Sheep", "Snake", "Spider", "Squirrel", "Tiger", "Toad",
            "Walrus", "Whale", "Wolf", "Worm", "Zebra"],

            'Sports':["Football", "Soccer", "Cricket", "Hockey", "Tennis", "Baseball", "Volleyball", "Golf",
                "Badmitton", "Fishing", "Archery", "Fencing", "Boxing", "Fencing", "Polo"
            ],

            'Musical-Instruments':["Violin", "Guitar", "Drums", "Trumpet", "Flute", "Saxophone", "Tuba", "Piano", "Clarinet"]
            
        }

    def run(self):
        game_over = False

        print("To quit the game press q at any time\n")

        # main game loop
        while not game_over:
            timer_running = False
            word = self.get_random_word()

            # If word == none then there are no more words left in the list of words
            # for the specific genre key
            if word != None:
                print("Player, your word is: {}".format(word))
                definition_request = input("Would you like a definition for {}? Be warned, there is a {} second runoff on your timer if you get a definition (yes/no): ".format(word, self.definition_penalty))

                # Block of code to determine if the player wants a dictionary definition or not
                if definition_request[0].lower() == "y":
                    self.get_definition(word)
                    self.time_limit -= self.definition_penalty
                elif definition_request[0].lower() == "q":
                    break

                # This block of code determines when a player is ready to start
                # by monitoring events to see if they player has pressed "A".
                # If so, then the timer for their turn starts to run
                # There is an error here that causes the game to freeze after the
                # first turn is played, I think it has to do with pygame.event not
                # being used for a while, but I've tried to fix it to no avail
                print("Player, press \"A\" to begin your turn")
                while not timer_running:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                            timer_running = True
                            print("Begin!")
                            game_over = self.run_timer()
            else:
                game_over = True

        pygame.quit()

    # This function returns True or False based on if the player decides to end
    # The game or not.  I thought this would just make it a little more simple
    # for determining a quit action even if it doesn't make much sense
    def run_timer(self):
        # Variable to determine when the timer starts
        start = pygame.time.get_ticks()
        while True:
            seconds = (pygame.time.get_ticks() - start) / 1000

            if seconds > self.time_limit:
                #TODO: play timer end sound
                timer_sound = pygame.mixer.Sound('Buzzer.mp3')
                timer_sound.play()
                print("Bummer, you ran out of time!")
                return False

            else:
                # This block of code monitors events to see if a player has had their
                # word guessed.  If it has been and the player presses space, then the
                # function returns False.  If q is pressed on the other hand, then the
                # game has been quit
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        #TODO: play congrats sound
                        correct_sound = pygame.mixer.Sound('Congrats.mp3')
                        correct_sound.play()
                        print("Congratulations you earned a point!")
                        return False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                        return True

    # This function returns a random word from the list mapped to the genre key in the dictionary
    def get_random_word(self):
        # If there are words in the list mapped to the genre key in the dictionary, then the function
        # returns a random word from that list
        if len(self.words[self.genre]) > 0:
            word = self.words[self.genre][random.randint(0, len(self.words[self.genre]) - 1)]
            self.words[self.genre].remove(word)
            return word
        # If there are no words left in the list mapped to the genre key in the dictionary, then
        # the function returns False to indicate that there are no more words left in the list
        else:
            # TODO: Maybe add a feature to play with a different genre or restart the game?
            print("There are no more words for this genre!")
            return None

    def get_definition(self, word):
        self.dictionary.search(word)

    # Helper function to use outside of the class for when a player is choosing their genre
    def get_words(self):
        return self.words

### Logic Flow (A, B, C are arbitrary)
# Startup (maybe give user the option to chose time limit and definition penalty)
pygame.init()
screen = pygame.display.set_mode((200, 200))
main_game = MainGame()
print("Welcome to charades!")

# This block of code gets the genre for the player, if they player does not want to choose
# a random genre is chosen for them. Error checking is included
while True:
    genre = input("What genre would you like to play? If none is selected a random genre will be selected for you (list of genres here/n): ")

    if genre[0].lower() != "n":
        genre = genre.lower()
        genres = main_game.get_words()

        if genre not in genres:
            print("That is not an available genre")
        else:
            print("The genre you have chosen to play is: {}".format(genre))
            break
    else:
        # TODO: assign the genre variable a random genre
        pass

# This block of code determines if a player would like a custom time limit.  If not then
# the time limit is set to the default time limit of 60 seconds.  Error checking is included
while True:
    time_limit = input("Would you like a custom time limit?  Default time limit is 60 seconds. (time limit in seconds/n): ")
    default_time_limit = 60

    if time_limit[0].lower() != "n":
        try:
            time_limit = int(time_limit)
            if time_limit > 0:
                print("Time limit is {} seconds".format(time_limit))
                break
            else:
                print("Please pick a time limit that is greater than 0 seconds")
        except ValueError:
            print("Please enter a number in seconds")
    else:
        time_limit = default_time_limit
        print("Time limit is {} seconds".format(time_limit))

# This block of code determines if the player would like a custom definition penalty.  If not
# then the definition penalty is set to the default penalty of 10 seconds.  Error checking is
# included
while True:
    definition_penalty = input("Would you like a custom definition penalty?  Default definition penalty is 10 seconds. (definition penalty in seconds/n): ")
    default_penalty = 10

    if definition_penalty[0].lower() != "n":
        try:
            definition_penalty = int(definition_penalty)
            if definition_penalty > time_limit:
                print("Please choose a definition penalty that is less than the time limit")
            else:
                print("Definition penalty is {} seconds".format(definition_penalty))
                break
        except ValueError:
            print("Please enter a number in seconds")
    else:
        definition_penalty = default_penalty
        print("Definition penalty is {} seconds".format(definition_penalty))

main_game = MainGame(time_limit, genre, definition_penalty)
main_game.run()
print("Thank you for playing!")

# Ask user for genre?
# Tell user to press A when it is their turn
# Give the user a word from their chosen genre
# Give the user the option to look up the definition of their word; however, they will have 10 less seconds to act it out
### DEFINITION, we should have error handling for the case that there is an error
    # https://dictionaryapi.dev/
    # Example request: https://api.dictionaryapi.dev/api/v2/entries/en/<word>
        # https://api.dictionaryapi.dev/api/v2/entries/en/hello
# When the user is ready, they press B to start the timer
    # If guessed correctly before the timer ends, they press C to start the timer
    # If not guessed correctly, a timer goes off.