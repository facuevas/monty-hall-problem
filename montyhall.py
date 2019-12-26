'''
Proving the Monty Hall Problem with Python.

Assumptions for Monty Hall problem (based on https://en.wikipedia.org/wiki/Monty_Hall_problem):
1) The host must always open a door that was not picked by the contestant
2) The host must always open a door to reveal a got and never the car
3) The host must always offer the chance to switch between the originally chosen door and the remaining closed door
'''
import random

def main():
    i = 0
    num_of_trials = 1000000
    num_of_wins_when_switched = 0
    num_of_wins_when_stay = 0
    while i <= num_of_trials:
        if (trail(True)):
            num_of_wins_when_switched += 1
        i += 1

    while i <= num_of_trials:
        if (trail(False)):
            num_of_wins_when_stay += 1
        i += 1
    
    print("% of winning when we switch doors: ", (num_of_wins_when_switched / num_of_trials))
    print("% of winning when we switch doors: ", (num_of_wins_when_stay / num_of_trials))

def trail(switch_doors):
    '''
    Let the gamehost know that the car will always be behind door number 1
    '''

    # select a random door:
    guest_choice = random.randint(1, 3)
    
    # if we are switching doors:
    if switch_doors:
        door_revealed = 3 if guest_choice == 2 else 2 # if guest chose door 2, return 3 else they chose 3, therefore return 2
        
        # find remaining doors avaiable for the switch
        doors_available = [doornum for doornum in range(1, 4)
                            if doornum not in (guest_choice, door_revealed)]
        guest_choice = random.choice(doors_available)

    return guest_choice == 1


if __name__ == "__main__":
    main()