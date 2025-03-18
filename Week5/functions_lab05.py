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
