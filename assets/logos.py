from classes.colours import bcolors
import time

def main_logo():
   print(f'''\n\n{bcolors.OKGREEN}{bcolors.BOLD} 
  ________            ______          __  _ _____            __          _____ __                     
 /_  __/ /_  ___     / ____/__  _____/ /_(_) __(_)________ _/ /____     / ___// /___ ___  _____  _____
  / / / __ \/ _ \   / /   / _ \/ ___/ __/ / /_/ / ___/ __ `/ __/ _ \    \__ \/ / __ `/ / / / _ \/ ___/
 / / / / / /  __/  / /___/  __/ /  / /_/ / __/ / /__/ /_/ / /_/  __/   ___/ / / /_/ / /_/ /  __/ /    
/_/ /_/ /_/\___/   \____/\___/_/   \__/_/_/ /_/\___/\__,_/\__/\___/   /____/_/\__,_/\__, /\___/_/     
                                                                                   /____/             

   {bcolors.ENDC}\n\n''')
   time.sleep(5)

def game_over():
   print(f'''\n\n{bcolors.FAIL}{bcolors.BOLD} 

      ______                        ____                 
     / ____/___ _____ ___  ___     / __ \_   _____  _____
    / / __/ __ `/ __ `__ \/ _ \   / / / / | / / _ \/ ___/
   / /_/ / /_/ / / / / / /  __/  / /_/ /| |/ /  __/ /    
   \____/\__,_/_/ /_/ /_/\___/   \____/ |___/\___/_/     
                                                      

   {bcolors.ENDC}\n\n''')

def master_consultant():
   print(f'''\n\n{bcolors.OKBLUE}{bcolors.BOLD} 

    __  ______   _____________________     __________  _   _______ __  ____  _________    _   ________
   /  |/  /   | / ___/_  __/ ____/ __ \   / ____/ __ \/ | / / ___// / / / / /_  __/   |  / | / /_  __/
  / /|_/ / /| | \__ \ / / / __/ / /_/ /  / /   / / / /  |/ /\__ \/ / / / /   / / / /| | /  |/ / / /   
 / /  / / ___ |___/ // / / /___/ _, _/  / /___/ /_/ / /|  /___/ / /_/ / /___/ / / ___ |/ /|  / / /    
/_/  /_/_/  |_/____//_/ /_____/_/ |_|   \____/\____/_/ |_//____/\____/_____/_/ /_/  |_/_/ |_/ /_/     
                                                                                                      
                                                      
   {bcolors.ENDC}\n\n''')



