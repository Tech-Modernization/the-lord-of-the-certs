from classes.colours import bcolors
from classes.hero import Hero
from classes.opponent import *
from assets.storytext import intro_text, quest_text, epilogue_text
from assets.logos import *
import random
import sys

# # Print the prologue 
# intro_text()

# # Print the logo
# main_logo()

# Prompt user for name and then welcome
hero = "Paul"
# hero = input('Welcome Hero! Please tell me your name so I may record your noble deeds! : ')
print(f'\nWelcome {hero}!\nThis is your story....\n')

# Print the initial quest text
# quest_text()

# Instantiate players
player1 = Hero(str(hero.ljust(40, ' ')), 9999, 500)
players = [player1]
total_players = len(players)

# Set the defeated player and enemy variables to zero
defeated_enemies = 0
defeated_players = 0



# Print opening quiz text
print(f'\n\n{bcolors.FAIL}{bcolors.BOLD}A VICIOUS CLOUD CERTIFICATION ATTACKS!!!{bcolors.ENDC}')
time.sleep(1)

def health_check():
    print(f'\n\n============================================================\n')
    # Print the health bars of all participants
    print(f'NAME                                                     HP                                      ')
    for player in players:
        player.get_stats()
    print(f'\n')
    for enemy in enemies:
        enemy.get_stats()

quiz = True

# quiz code
while quest:
    opponent_choice = random.randint(0, len(possible_enemies))
    opponent = opponent_choice[possible_enemies]
    health_check()
    ask_question()

