import random


# def get_valid_int_input(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("Error: Please enter a valid integer!")
#             continue
# try:
#     elements_selected = get_valid_int_input("Enter the index of the element you like: ")
#     # Roll dice
#     elementRoll = random.randint(1, 6)
#     totalNum = elements_selected + elementRoll


weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
print("Choose Your Weapons: ", weapons)

def get_wepon_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer!")
            continue

try:
    wepon_selected = get_wepon_input("Enter the index of the weapon you like: ")
    combatStrength = wepon_selected
    weaponRoll = random.randint(1, 6)
    totalNum = weaponRoll + combatStrength

    weaponRoll = int(input("Enter a weapon roll (1 to 6): "))

    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    elif weaponRoll <= 6:
        print("Nice weapon, friend!")
    else:
        print("Error: Weapon roll must be between 1 and 6.")

except IndexError:
    print("Error: Invalid element index!")  # This exception is not relevant for this context.
except ValueError:
    print("Error: Please enter a valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
