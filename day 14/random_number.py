import random

print("=" * 40)
print("Random Number Generator")
print("=" * 40)

number=random.randint(1,100)

colors =["Red","Blue","Green","Yellow","Black"]

color = random.choice(colors)

print("Random Number :", number)
print("Random Color  :", color)