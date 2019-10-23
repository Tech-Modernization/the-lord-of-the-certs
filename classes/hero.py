import random
from .colours import bcolors
 
class Hero:
    def __init__(self, name, hp, atk):
        self.maxhp = hp
        self.hp = hp
        self.atk = atk
        self.name = name

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
            current_hp.ljust(11, " ") + "  |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + "|    ")


