def camel(s):
    res = ""
    for i in s:
        if i.islower():
            res += i
        else:
            res+= "_"+i.lower()
    return res

def main():
    s = input("camelCase: ")
    print(camel(s))
    
if __name__ == "__main__":
    main()