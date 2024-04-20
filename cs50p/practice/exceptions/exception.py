def get_int():
    while True:
        try:
            x = int(input("Whats x ? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x

def main():
    x = get_int()
    print(x)
    
    
main()
