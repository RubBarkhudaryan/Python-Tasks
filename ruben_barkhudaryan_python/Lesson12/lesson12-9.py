import random

print("\nData Types")
print("\nNumbers\n")

print(random.randrange(10, 20))

x = ["a", "b", "c", "d", "e"]

print(random.choice(x))

random.shuffle(x)

print(x)

print(random.random())
