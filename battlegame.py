# Task 1
# declare variables for hitpoints
# The hp of a wizard is 70
# The hp of a elf is 100
# The hp of a human is 150
# Declare variables for damage points
# The damage of a Wizard is 150
# The damage of a elf is 100
# #The damage of a human is 20
# declare two variables that set the hp and damage for the Dragon - 300 hp and 50 damage.

wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 70
human_damage = 20

dragon_hp = 300
dragon_damage = 50

# Task 2
# Prompt the player to choose from a list of options
# Use the input() function to prompt the user with the String: "Choose your character: " and assign to the variable "character"
while True:
    print("1. wizard")
    print("2. elf")
    print("3. human")
    character = input("Choose your character: ")
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("unknow character")
print("You have chosen the character:", character)
print("Health:", my_hp)
print("Damage:", my_damage)

while True:
    dragon_hp -= my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now:", dragon_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    my_hp -= dragon_damage
    print("The Dragon strikes back at", character)
    print("The", character, "'s", "hitpoints are now:", my_hp)
    if my_hp <= 0:
        print("The", character, "has lost the battle")
        break
