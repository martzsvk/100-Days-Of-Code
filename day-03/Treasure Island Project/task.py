print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You came to a mysterious island.")

first_choice = input("You see a cave and a shipwreck. Do you want to go to the 'cave' or the 'shipwreck'? ")

if first_choice == "cave".capitalize():
    print("You found hidden paths in the cave.")
else:
    print("A skeleton pirate killed you. Game over.")

second_choice = input("Do you want to go left or right? Please write 'left' or 'right'. ")

if second_choice == "right".capitalize():
    print("You found a room in the cave.")
else:
    print("There was a hidden trap. Game over.")

third_choice = input("There's a button and a lever which one do you want to try? Please write 'button' or 'lever'. ")

if third_choice == "lever".capitalize():
    print("The lever opened a secret wall. You found the treasure!!")
else:
    print("The button drop rocks on you. Game over.")



