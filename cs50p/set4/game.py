import random

while True:
    try:
        num = int(input("Level: "))
        target = random.randint(1, num)
        while True:
            guess = int(input("Guess: "))
            if guess > target:
                print("Too large!")
            elif guess < target:
                print("Too small!")
            elif guess == target:
                print("Just right!")
                raise EOFError
    except ValueError:
        pass
    except EOFError:
        break