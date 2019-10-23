from classes.colours import bcolors
from classes.hero import Hero
from classes.opponent import *
from assets.storytext import intro_text, quest_text, epilogue_text
from assets.logos import *
import random
import sys

def health_check():
    print(f'\n\n============================================================\n')
    # Print the health bars of all participants
    print(f'NAME                                                     HP                                      ')
    player.get_stats()
    print(f'\n')
    opponent.get_stats()

# # Print the prologue 
# intro_text()

# # Print the logo
# main_logo()

# Prompt user for name and then welcome
hero = "Paul"
# hero = input('Welcome Hero! Please tell me your name so I may record your noble deeds! : ')
# print(f'\nWelcome {hero}!\nThis is your story....\n')

# Print the initial quest text
# quest_text()

# Instantiate players
player = Hero(hero, 9999, 500)

# Print opening quiz text
# print(f'\n\n{bcolors.FAIL}{bcolors.BOLD}A wild Cloud Certification attacked!{bcolors.ENDC}')
# time.sleep(1)

quest = True
defeated_opponents = 0

# quiz code
while quest:
    choose_opponent = True
    while choose_opponent:
        opponent_choice = random.randint(0, len(possible_opponents) -1)
        opponent = possible_opponents[opponent_choice]
        print(f'\n\n{bcolors.FAIL}{bcolors.BOLD}A wild {opponent.name} attacked!{bcolors.ENDC}')
        time.sleep(1)
        health_check()
        choose_opponent = False
        quest = False

