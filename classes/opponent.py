import random
from collections import namedtuple
from .colours import bcolors
 
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

    def get_stats(self):
        # All the code related to HP bar control
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

# Set the object type "Question" as a named Tuple
Question = namedtuple("Question", "question answer choices correct")

# Create the Question objects and ensure each one has a different variable name so they can be referenced by the Opponent objects
saa_questions =  [Question("What is 1 + 1?", "1 + 1 is 2.", "a) 1\nb) 2\nc) 3\nd) 4\nAnswer: ", "b"), 
                    Question("What is 2 + 2?", "2 + 2 is 4.", "a) 1\nb) 4\nc) 3\nd) 4\nAnswer: ", "b"),
                    Question("What is 3 + 3?", "3 + 3 is 6.", "a) 1\nb) 6\nc) 3\nd) 4\nAnswer: ", "b"),
                    Question("What is 4 + 4?", "4 + 4 is 8.", "a) 1\nb) 8\nc) 3\nd) 4\nAnswer: ", "b")]

af_questions =  [Question("What is a + a?", "a + a is aa.", "a) aa\nb) ab\nc) ac\nd) zz\nAnswer: ", "a"), 
                    Question("What is c + a?", "c + a is ca.", "a) 1\nb) ca\nc) zz\nd) xx\nAnswer: ", "b"),
                    Question("What is x + y?", "x + y is xy.", "a) 1\nb) 6\nc) xy\nd) 4\nAnswer: ", "c"),
                    Question("What is z + z?", "z + z is zz.", "a) 1\nb) 8\nc) 3\nd) zz\nAnswer: ", "d")]

gca_questions =  [Question("What is a + a?", "a + a is aa.", "a) aa\nb) ab\nc) ac\nd) zz\nAnswer: ", "a"), 
                    Question("What is c + a?", "c + a is ca.", "a) 1\nb) ca\nc) zz\nd) xx\nAnswer: ", "b"),
                    Question("What is x + y?", "x + y is xy.", "a) 1\nb) 6\nc) xy\nd) 4\nAnswer: ", "c"),
                    Question("What is z + z?", "z + z is zz.", "a) 1\nb) 8\nc) 3\nd) zz\nAnswer: ", "d")]

cka_questions =  [Question("What is a + a?", "a + a is aa.", "a) aa\nb) ab\nc) ac\nd) zz\nAnswer: ", "a"), 
                    Question("What is c + a?", "c + a is ca.", "a) 1\nb) ca\nc) zz\nd) xx\nAnswer: ", "b"),
                    Question("What is x + y?", "x + y is xy.", "a) 1\nb) 6\nc) xy\nd) 4\nAnswer: ", "c"),
                    Question("What is z + z?", "z + z is zz.", "a) 1\nb) 8\nc) 3\nd) zz\nAnswer: ", "d")]

# List possible opponents that can be randomly selected from
possible_opponents = [Opponent("AWS Solutions Architect Associate", 2000, 1000, saa_questions),
                      Opponent("Google Cloud Associate", 1000, 1000, af_questions),
                      Opponent("Azure Fundamentals", 1000, 1000, gca_questions),
                      Opponent("Certified Kubernetes Administrator", 1000, 1000, cka_questions)]

