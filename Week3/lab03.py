import random

# Dice options using list() and range()
diceOptions = list(range(1, 7))

# Weapons array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

print("Available Weapons:", ', '.join(weapons)) 

# Inputs combat strength hero
combatStrength = int(input("Enter your combat strength (1-6): "))
if combatStrength < 1 or combatStrength > 6:
    print("Invalid input! Combat strength should be between 1 and 6.")
    combatStrength = 1 # Default value for invalid input

# Inpunt combat strength for moster
mCombatStrength = int(input("Enter moster's combat stregth (1-6)"))
if mCombatStrength < 1 or mCombatStrength > 6:
    print("Invalid input! Monster combat strength should be between 1 and 6.")
    mCombatStrength = 1 # Default value for invalid input

# Simulate Battle rounds
for j in range(1, 21, 2): # Simulation of 20 ranouds, stepping by 2
    # Dice rolls for hero and monster
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    # Calculate the weapons
    heroWeapom = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    # Calculate total stregth
    heroTotal = combatStrength + heroRoll
    monsterTotal = combatStrength + monsterRoll
     

    # Print round details
    print(f"\nRound {j} Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print(f"Hero selected: {heroWeapom}, Monster selected: {monsterWeapon}")
    print(f"Hero total stregth: {heroRoll}, Monster total stregth: {monsterTotal}")

    # Determine winner
    if heroTotal > monsterTotal:
        print("Hero wins the round!")
    elif heroTotal < monsterTotal:
        print("Monster wins the round")
    else:
        print("It's a tie!")         
    
    if j == 11:
        print("\n Battle Truce declread in Round 11. Game Over!")
        break
if j != 11:
    print("\n Battle conluded after 20 rounds!")
