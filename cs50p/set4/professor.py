import random

def main():
    equation_count = 10
    total_score = 0
    attempts_left = 3
    difficulty_level = get_level()
    while equation_count != 0:
        if attempts_left == 3: 
            # New equation generated only when attempts_left is 3
            num1, num2 = generate_integer(difficulty_level)
        try:
            user_response = int(input(f"{num1} + {num2} = "))
            correct_answer = num1 + num2
            if user_response == correct_answer:
                equation_count -= 1
                total_score += 1
                attempts_left = 3 
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            attempts_left -= 1
            pass
        if attempts_left == 0:
            print((f"{num1} + {num2} = {correct_answer}"))
            attempts_left = 3 
            equation_count -= 1
            continue
    print(f"Score: {total_score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except:
            pass

def generate_integer(level):
    if level == 1:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    elif level == 2:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    elif level == 3:
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)
    return num1, num2

if __name__ == "__main__":
    main()
