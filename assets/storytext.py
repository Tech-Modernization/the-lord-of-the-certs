import sys, time

# Define the scrolltext functions
def print_quick(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.7)

def intro_text():
    print_quick("\nIn a world of failed cloud migrations, Waterfall projects and unsecured S3 buckets...")
    print_slow("\n" + "...")
    print_quick("\nOne consultancy stands apart. It's mission: to save their clients from themselves, and from the pitfalls of bad digital transformations!")
    print_slow("\n" + "...")
    print_quick("\nEach Contino consultant is duty-bound to do battle with the forces of the cloud and cloud-native technologies, and to obtain the coveted certifications that mark them out among their peers as wise and all-knowing.")
    print_slow("\n" + "...")
    print_quick("\nOnly those who can defeat all the exams and obtain each one of the certifications can receive the coveted title of: 'Master Consultant'.")
    print_slow("\n" + "...")
    print_quick("\nDo YOU have what it takes, hero?")
    time.sleep(2) 

def quest_text():
    print_quick("\nIt's your first day at Contino.")
    print_slow("\n" + "...")
    print_quick("\nYou've completed your onboarding, setup your new equipment, checked in with PeopleOps and decided to relax...")
    print_slow("\n" + "...")
    print_quick("\nYou decide to walk through a grassy meadow, when you hear a rustle...")
    print_slow("\n" + "...")
    time.sleep(1)
