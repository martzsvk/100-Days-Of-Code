import art

print(art.logo)
print("Welcome to my Secret Auction Program :)")


biders = {}


other_biders = "yes"
while other_biders == "yes":
    name = input("What's your name? ")
    bid = int(input("How much is your bid? €"))
    biders[name] = bid
    other_biders = input("Are there any other biders? 'yes' or 'no' ").lower()
    if other_biders == "yes":
        print("\n" * 20)

    elif other_biders == "no":
        print("\n" * 20)
        winner = max(biders, key=biders.get)
        print(f"The winner is {winner} with €{biders[winner]}")
        exit()




