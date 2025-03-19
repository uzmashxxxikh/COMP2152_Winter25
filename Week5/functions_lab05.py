# functions_lab05.py
import random


# Question 3
def collect_loot(loot_options, belt):
    print("Random loot process:")
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    print("    |    Your belt: ", belt)
    return loot_options, belt

# Question 4 Use Loot
def use_loot(belt, health_options):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]    

    print("You see a monster! So you quickly use your first item:")

    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_options = min(20, (health_options + 2))
        print("You used " + first_item + "and your health is " + str(health_options))
    elif first_item in bad_loot_options:
        health_options = max(20, (health_options - 2))
        print("You used " + first_item + "and your health is " + str(health_options))
    else:
        print("You used " + first_item + " but it's not helpful")
    return belt, health_options


# Recursion
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    if num_dream_lvls == 1 :
        print("You are in the deepest dream level now")
    else:
        return 1 + int(inception_dream(num_dream_lvls -1 ))            


def collect_loot(belt, loot_options):
    print("Collecting loot...")
    if loot_options:  # Check if there is any loot available
        loot_item = loot_options.pop(0)  # Take the first available item
        belt.append(loot_item)  # Add it to the player's belt
        print(f"Collected: {loot_item}")
    else:
        print("No loot available!")
    return belt


def use_loot(belt, health_points):
    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    
    if belt:  # Check if the belt has any loot
        first_item = belt.pop(0)  # Use the first item in the belt
        
        good_loot_options = ["Health Potion", "Leather Boots"]
        bad_loot_options = ["Poison Potion"]

        if first_item in good_loot_options:
            health_points += 10  # Example: Increase health
            print(f"    |    You used {first_item} to increase your health to {health_points}")
        elif first_item in bad_loot_options:
            health_points -= 10  # Example: Decrease health
            print(f"    |    You used {first_item} which decreased your health to {health_points}")
        else:
            print(f"    |    You used {first_item} but nothing happened")
    else:
        print("No loot available to use!")

    return health_points

