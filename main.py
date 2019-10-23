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


# # Print the prologue and logo
# intro_text()
# main_logo()

# Prompt user for name and then welcome
hero = "Paul"
# hero = input('Welcome Hero! Please tell me your name so I may record your noble deeds! : ')
# print(f'\nWelcome {hero}!\nThis is your story....\n')

# Print the initial quest text
# quest_text()

# Instantiate players
# To make the quiz more challenging and increase the number of correct answers needed to defeat each opponent, reduce the Hero's attack power
#                   Health Atk
player = Hero(hero, 1,  3000)

# Instantiate opponents
opponents = possible_opponents

quest = True

# quiz code
while quest:
    create_opponent = True
    while create_opponent:
        opponent_choice = random.randint(0, len(opponents) -1)
        opponent = opponents[opponent_choice]
        print(f'\n\n{bcolors.FAIL}{bcolors.BOLD}A wild {opponent.name} attacked!{bcolors.ENDC}')
        time.sleep(1)
        health_check()
        for question in opponent.questions:
            print(question.question)
            user_answer = input(question.choices).lower()
            if user_answer in question.correct:
                dmg = player.generate_damage()
                opponent.take_damage(dmg)
                print(f'\n{player.name} got the answer correct, and dealt {dmg} damage to {opponent.name}!')
            else:
                opponent_dmg = opponent.generate_damage()
                player.take_damage(opponent_dmg)
                print(f'\nOh dear! {player.name} got the answer wrong! The correct answer was {question.answer}. {opponent.name} dealt {opponent_dmg} damage to {player.name}!')
            health_check()
            if player.get_hp() == 0:
                print(f'\n{bcolors.FAIL}{bcolors.BOLD}{player.name} has been defeated!{bcolors.ENDC}')
                quest_succeeded = False
                create_opponent = False
                quest = False
                break
            if opponent.get_hp() == 0:
                print(f'\n{opponent.name} has been defeated!')
                opponents.remove(opponent)
                break
        if len(opponents) > 0:
            break
        elif len(opponents) == 0:
            quest_succeeded = True
            quest = False
            create_opponent = False
        else:
            print("Error: Length of 'opponents' neither 0 or > 0. How has this occurred?!")            

if quest_succeeded == True:
    time.sleep(1)
    print(f'''{bcolors.OKGREEN}{bcolors.BOLD}\nCongratulations, you have defeated all the certifications that opposed you!
        \nYou have obtained the title of ...{bcolors.ENDC}''')
    time.sleep(1)
    master_consultant()
elif quest_succeeded == False:
    time.sleep(1)
    print(f'''{bcolors.FAIL}{bcolors.BOLD}\nOh dear, you failed to answer enough questions correctly and the certifications have overwhelmed you!
            \nPlease study harder and try again!{bcolors.ENDC}''')
    time.sleep(1)
    game_over()
else:
    print("Error: Quest neither succeeded or failed, how have you managed this?!")