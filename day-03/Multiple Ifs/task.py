print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Under 12 tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Under 18 tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12
    photos = input("Do you want photos? yes/no ")
    if photos == "yes":
        bill += 3
        print(f"The total is {bill}$ ")
    else:
        print (f"The total is {bill}$ ")


else:
    print("Sorry you have to grow taller before you can ride.")
