import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Who will pay the bill
paying_bill = random.randint(0,4)

if paying_bill == 0:
    print("Alice")
elif paying_bill == 1:
    print("Bob")
elif paying_bill == 2:
    print("Charlie")
elif paying_bill == 3:
    print("David")
else:
    print("Emanuel")

print("......................................................................")

# Or like this

paying_guy = random.choice(friends)
print(paying_guy)









