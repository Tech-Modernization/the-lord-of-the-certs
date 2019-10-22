import sys, time

# Define the scrolltext functions
def print_quick(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.7)

def intro_text():
    print_quick("In a world of failed cloud migrations, Waterfall projects and unsecured S3 buckets...")
    print_slow("\n" + "..." + "\n")
    print_quick("One consultancy stands apart. It's mission: to save our clients from themselves, and from the pitfalls of bad digital transformations!")
    print_slow("\n" + "..." + "\n")
    print_quick("Each Contini consultant chooses to do battle with the forces of the cloud, and to obtain the coveted cloud certifications that mark them as wise and all-knowing.")
    print_slow("\n" + "..." + "\n")
    print_quick("Only those who can defeat all the exams and obtain each one of the certifications can receive the title of 'Master Consultant'.")
    print_slow("\n" + "..." + "\n")
    print_quick("Do YOU have what it takes?")
    time.sleep(2)

def fillspace():
    print_quick("..." + "\n\n" + "..." + "\n\n" + "..." + "\n\n")

def quest_text():
    print_quick("\nOur hero is new to Contino.")
    print_slow("\n" + "..." + "\n")
    print_quick("They have completed the onboarding, setup their new equipment and have decided to upskill!")
    print_slow("\n" + "..." + "\n")
    print_quick("They start to look for something to study...")
    print_slow("\n" + "..." + "\n")
    print_quick("Oh no! It's an ambush!\n")
    time.sleep(2)

def epilogue_text():
    print_quick("And so our hero's journey ends here.")
    print_slow("\n" + "..." + "\n")
    print_quick("I hope this journey taught you some of the amazing capabilities of Python!")
    print_slow("\n" + "..." + "\n")
    print_quick("And if you weren't able to become a 'Master Consultant', on this attempt, study up and try again!")
    print_slow("\n" + "..." + "\n")
    print_quick("Until then, go and be awesome!")
    time.sleep(2)
