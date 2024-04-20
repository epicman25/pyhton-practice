def value(greeting):
    greeting = greeting.lower().strip()
    if (greeting.startswith("hello")):
        return 0
    elif(greeting[0] == 'h'):
        return 20
    else:
        return 100

def main():
    greeting = input("Greeting : ")
    res = value(greeting.lower().strip())
    print(f"${res}")

if __name__ == "__main__":
    main()
