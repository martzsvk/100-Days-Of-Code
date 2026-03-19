print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What's your age? "))

if height >= 120:
    print("You can ride the rollercoaster")
    if age > 18:
        print("You need to pay 12$ ")
    elif age >= 12 and age <= 18:
        print("You need to pay 7$")
    else:
        print("You need to pay 5$ ")
else:
    print("Sorry you have to grow taller before you can ride.")
