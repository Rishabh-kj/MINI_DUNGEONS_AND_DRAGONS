print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


import random

L = ["L", "R", "S", "W", "C"]

random.shuffle(L)

print("\n\n\nWelcome to the MINI DUNGEONS AND DRAGONS!")
print("Your mission is to find the treasure!")

left_right = input("Do you want to go left or right? Enter L for left and R for right: ")
if(left_right not in "LR"):
    print("Game over! Dumb people shouldn't survive! You entered an invalid choice!")
    exit(1)
else:
    if(L.index(left_right)%2 == 0):
        print("You fell into a hole! Game over!")
        exit(1)
    else:
        print("You survived for now!")
        swim_wait = input("You have now reached a river. Do you want to swim or wait? Enter S to swim or W to wait: ")
        if(swim_wait not in "SW"):
            print("Game over! Dumb people shouldn't survive! You entered an invalid choice!")
            exit(1)
        else:
            if(L.index(swim_wait) % 2 == 0):
                if(swim_wait == "S"):
                    print("You have become a meal for the Kracken! Game over!")
                else:
                    print("The ghost caught up to you! You are now possessed! Game over!")
                exit(1)
            else:
                print("You have survived for now!")
                print("You have now reached the dungeon that hides the treasure within. You have three options.")
                door_choice = input("Enter C to enter via the cellar, enter L to enter via the gate to the left, or enter R to enter via the gate to the right: ")
                if(door_choice not in "CLR"):
                    print("Game over! Dumb people shouldn't survive! You entered an invalid choice!")
                    exit(1)
                else:
                    if(L.index(door_choice) % 2 == 0):
                        if(door_choice == "L"):
                            print("You have been burned by fire! Game over!")
                        elif(door_choice == "C"):
                            print("You have become a dragon's feast! Game over!")
                        else:
                            print("You are trapped! Game over!")
                        exit(1)
                    else:
                        print("You win! Claim your treasure! Woohooo!")
                        exit(1)