import random

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

weaponRoll = random.randint(1, 6)
print("Weapon Roll: ", weaponRoll)

combat_strength = weaponRoll

if 0 <= weaponRoll - 1 < len(weapons):
    hero_weapon = weapons[weaponRoll - 1]
else:
    raise IndexError("Weapon roll is out of valid range")
    print(f"Hero's weapon: {hero_weapon}")


    weaponRoll = int(input("Enter a weapon roll (1 to 6): "))

try:
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    if hero_weapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")

except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except IndexError:
    print("Error: Invalid roll. The roll must be between 1 and 6.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
