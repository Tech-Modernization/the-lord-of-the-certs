import random
from .colours import bcolors
from assets.af_questions import af_questions
from assets.saa_questions import saa_questions
from assets.gca_questions import gca_questions
from assets.cka_questions import cka_questions
 
class Opponent:
    def __init__(self, name, hp, atk, questions):
        self.maxhp = hp
        self.hp = hp
        self.atk = atk
        self.name = name
        self.questions = questions

    def generate_damage(self):
        return self.atk

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    # This function is used in the "health_check" function in main program. Beware changes!
    def get_stats(self):
        hp_bar = ""
        hp_bar_ticks = ((self.hp / self.maxhp) * 100) /2
        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += " "     
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string
        print("                                                         __________________________________________________ ")
        print(bcolors.BOLD + str(self.name.ljust(40, ' ')) + ":  " +
            current_hp.ljust(11, " ") + "  |" + bcolors.FAIL + hp_bar + bcolors.ENDC + bcolors.BOLD)

class Question:
    def __init__(self, question, answer, choices, correct):
        self.question = question
        self.answer = answer
        self.choices = choices
        self.correct = correct

# List possible opponents that can be randomly selected from
possible_opponents = [Opponent("AWS Solutions Architect Associate", 5000, 1000, saa_questions),
                      Opponent("Azure Fundamentals", 2000, 1000, af_questions),
                      Opponent("Google Cloud Associate", 3000, 1000, gca_questions),
                      Opponent("Certified Kubernetes Administrator", 4000, 1000, cka_questions)]