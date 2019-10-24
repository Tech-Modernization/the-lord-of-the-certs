from classes.colours import bcolors
from classes.hero import Hero
from classes.opponent import *
from assets.storytext import intro_text, quest_text, print_slow, print_quick
from assets.logos import *
import random, sys, string

# Define the health check on both player and opponent so it can be called repeatedly
def health_check():
    print(f'\n\n===========================================================================================================\n')
    # Print the health bars of all participants
    print(f'NAME                                                     HP                                      ')
    player.get_stats()
    print(f'\n')
    opponent.get_stats()
    print(f'\n===========================================================================================================\n')

# # Print the prologue and logo
intro_text()
main_logo()

# Prompt user for name and then welcome
hero = input('Welcome Hero! Please tell me your name so I may record your noble deeds! : ')
time.sleep(0.05)
print_quick("\nWelcome " + hero + "!\n")

# Print the initial quest text
quest_text()

# Create our hero
player = Hero(hero, 2500,  1000)

# Add all possible_opponents from class file into the opponents list
opponents = possible_opponents

# Set the quest loop to start the quest
quest = True

# The actual program encased in a while loop that is broken either when player is defeated or no opponents remain
while quest:
    # Assumes quest is still running unless loop broken below.
    create_opponent = True
    while create_opponent:
        # Randonly selects opponent from list 
        opponent_choice = random.randint(0, len(opponents) -1)
        opponent = opponents[opponent_choice]
        print(f'\n\n{bcolors.FAIL}{bcolors.BOLD}A wild {opponent.name} attacked!{bcolors.ENDC}')
        time.sleep(1)
        print(f'\n\n{bcolors.FAIL}{bcolors.BOLD}To defeat it, answer the questions!{bcolors.ENDC}')
        time.sleep(1)
        # Display health bars and "set the scene"
        health_check()
        # Loop over all questions set for this opponent until opponent or player is defeated
        # Need to code an outcome if questions are exhausted but neither of the above has occurred
        random.shuffle(opponent.questions)
        for question in opponent.questions:
            print("\nYour opponent, " + opponent.name + " asks:\n\n") 
            time.sleep(0.5)
            print(question.question + "\n")
            # Will neatly print out the choices from the question on a newline each preeded with some formatting
            for line in zip(string.ascii_lowercase, question.choices):
                print(") ".join(line))
            print("\n")
            user_answer = input().lower()
            time.sleep(1)
            # Player answered successfully and causes damage to opponent
            if user_answer in question.correct:
                dmg = player.generate_damage()
                opponent.take_damage(dmg)
                print(f'\n{bcolors.OKGREEN}{bcolors.BOLD}{player.name} got the answer correct, and dealt {dmg} damage to {opponent.name}!{bcolors.ENDC}')
                time.sleep(1)
            # If player doesn't answer correctly, code assumes incorrect answer and causes damage to player
            else:
                opponent_dmg = opponent.generate_damage()
                player.take_damage(opponent_dmg)
                print(f'\n{bcolors.FAIL}{bcolors.BOLD}Oh dear! {player.name} got the answer wrong! The correct answer was {question.correct}! {opponent.name} dealt {opponent_dmg} damage to {player.name}!{bcolors.ENDC}')
                time.sleep(1)
            # Check the status of both players after each question, otherwise players will answer questions when dead (or opponent defeated)
            # Check is player HP is zero, if so break all loops and fail the questi
            if player.get_hp() == 0:
                print(f'\n{bcolors.FAIL}{bcolors.BOLD}{player.name} has been defeated!{bcolors.ENDC}')
                quest_succeeded = False
                create_opponent = False
                quest = False
                break
            # Check if opponent HP is zero, if so break question loop and program moves back to selecting a new opponent
            if opponent.get_hp() == 0:
                print(f'\n{opponent.name} has been defeated!')
                # Delete the opponent from the list so the same opponent is not generated multiple times
                opponents.remove(opponent)
                break
            # Ensures health bars are displayed after each question, to allow player to track progress.
            health_check()
            time.sleep(1)
        # If there are still opponents remaining, print message and break loop, goes back to generate a new opponent
        if len(opponents) > 0 and player.get_hp() > 0:
            time.sleep(1)
            print("\nOh no, something else is coming...\n")
            break
        elif len(opponents) > 0 and player.get_hp() == 0:
            time.sleep(1)
            print("\nEverything fades to black...\n")
            break
        # If all opponents defeated, mark quest as succeeded, break quest loop
        elif len(opponents) == 0:
            print("\nIs that all of them? Are we safe?\n")
            quest_succeeded = True
            quest = False
            create_opponent = False
        else:
            print("Error: Length of 'opponents' neither 0 or > 0. How has this occurred?!")            

# Conditional output depending on result of quest
if quest_succeeded == True:
    time.sleep(1)
    print(f'''{bcolors.OKGREEN}{bcolors.BOLD}\nCongratulations, you have defeated all the certifications that opposed you!
        \nYou have obtained the title of ...{bcolors.ENDC}''')
    time.sleep(1)
    master_consultant()
    print(f'{bcolors.OKGREEN}{bcolors.BOLD}\nPlease feel free to contribute more questions, or even add a new opponent to this program via a pull request!{bcolors.ENDC}')
elif quest_succeeded == False:
    time.sleep(1)
    print(f'''{bcolors.FAIL}{bcolors.BOLD}\nOh dear, you failed to answer enough questions correctly and the certifications have overwhelmed you!
            \nPlease study harder and try again!{bcolors.ENDC}''')
    time.sleep(1)
    game_over()
else:
    print("Error: Quest neither succeeded or failed, how have you managed this?!")
