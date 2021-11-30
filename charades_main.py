import pygame
import random

### Logic Flow (A, B, C are arbitrary)
# Startup (maybe give user the option to chose time limit and definition penalty)
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