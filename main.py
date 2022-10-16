import random


def number_guesser(x):
    secret_number = random.randint(1, x)
    guess = 0
    chances = 3
    while guess != secret_number:
        while chances + 0 and guess != secret_number:
            guess = int(input(f"Guess a random number between 1 and {x}. You have {chances} tries left. "))
            if guess < secret_number:
                print("The secret number is higher...")
                chances = chances - 1
                print(f"Chances = {chances}")
            elif guess > secret_number:
                print("The secret number is lower...")
                chances = chances - 1
                print(f"Chances = {chances}")
        if guess != secret_number and chances == 0:
            print(f"""You have no more chances left. The number was {secret_number}""")
            break
    if guess == secret_number:
        print(f"You won. The secret number was {secret_number}")


number_guesser(20)
