import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Rock: 0 Paper: 1 Scissors: 2\n"))

if choice == 0:
    print(f"You chose:\n {rock} ")
elif choice == 1:
    print(f"You chose:\n {paper} ")
elif choice == 2:
    print(f"You chose:\n {scissors}")

computer_choice = random.randint(0,2)

if computer_choice == 0:
    print(f"Computer chose:\n {rock} ")
elif computer_choice == 1:
    print(f"Computer chose:\n {paper} ")
elif computer_choice == 2:
    print(f"Computer chose:\n {scissors}")

#decide who won
if choice == computer_choice:
    print("Tie")
elif choice == 0 and computer_choice == 1:
    print("You lose")
elif choice == 1 and computer_choice == 2:
    print("You lose")
elif choice == 2 and computer_choice == 0:
    print("You lose")
elif choice != [0,1,2]:
    print("You typed invalid number")
else:
    print("You win")









