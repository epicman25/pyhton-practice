def twttr(s):
    vowels = "aeiou"
    res = ""
    for i in s:
        if i.lower() in vowels:
            pass
        else:
            res+=i
    return res

def main():
    s = input("Input: ")
    print(twttr(s))
    
if __name__ == "__main__":
    main()