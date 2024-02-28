wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
wizard_damage = 150

elf_hp = 100
elf_damage = 100

human_hp = 150
human_damage = 20

dragon_hp = 300
dragon_damage = 50

print("1) Wizard\n" "2) Elf\n" "3) Human")
while True:
    character = input("Chose your character!  ")
    
    if character == ("Wizard").lower() or character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        print("Your character is: ", character)
        print("Your HP is: ", my_hp)
        print("Your damage is: ", my_damage)
        break

    elif character == ("Elf").lower() or character == "2":
        character = elf 
        my_hp = elf_hp
        my_damage = elf_damage
        print("Your character is: ", character)
        print("Your HP is: ", my_hp)
        print("Your damage is: ", my_damage)
        break

    elif character == ("Human").lower() or character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        print("Your character is: ", character)
        print("Your HP is: ", my_hp)
        print("Your damage is: ", my_damage)
        break

    else:
        print("Please input one of the options given")
        
print("{}, your first opponent is a fierce dragon!".format(character))
import random 
choice_options = ["dragon", "you"]
randomized_choice = random.choice(choice_options)
print("The fickle fingers of fate have chosen {} to go first".format(randomized_choice))

if randomized_choice == "you":    
    while my_hp > 0 or dragon_hp > 0:
        if dragon_hp > 0:
            dragon_hp = dragon_hp - my_damage
            if dragon_hp > 0:
                print("You dealt ", my_damage, " damage! The dragon has ", dragon_hp, " left.")
                print("Now it's the dragon's turn, watch out!")
        if my_hp > 0:
            my_hp = my_hp - dragon_damage
            if my_hp > 0:
                print("You recieved", dragon_damage, " damage! You have ", my_hp, " left.")
                
        if dragon_hp <= 0:
            print("You are victorious! The dragon has been defeated!")
            break
        if my_hp <= 0:
            print("The dragon has killed you, RIP")
            break
                

if randomized_choice == "dragon":
    
    while my_hp > 0 or dragon_hp > 0:
        if my_hp > 0:
            my_hp = my_hp - dragon_damage
            if my_hp > 0:
                print("You received ", dragon_damage, " damage! You have ", my_hp, " left.")
                print("Now it's your turn, aren't you lucky the dragon patiently waits!")
        if dragon_hp > 0:
            dragon_hp = dragon_hp - my_damage
            if dragon_hp > 0:
                print("You did ", my_damage, " damage to the dragon! It has ", dragon_hp, " left.")
                
        if dragon_hp <= 0:
            print("You are victorious! The dragon has been defeated!")
            break
        if my_hp <= 0:
            print("The dragon has killed you, RIP")
            break
