import random

print("=" * 40)
print("Dice Simulator")
print("=" * 40)

while True:
    dice =random.randint(1,6)

    print("you rolled :",dice)

    choice=input("Roll Again? (yes/no):").lower()

    if choice!="yes":
        print("Game Over !")
        break