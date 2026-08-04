import random
print("=" * 40)
print("Advanced Number Guessing Game")
print("=" * 40)
secret = random.randint(1,100)

attempt=0
while True:
    guess =int(input("Enter your guess (1-100):"))

    attempt+=1
    if guess >secret:
        print("Too High")

    elif guess<secret:
        print("Too Low")

    else:
        print("\nCongratulations!")
        print("You guessed the correct number.")
        print("Total Attempts:", attempts)
        break