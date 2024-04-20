import re




def validate(ip):
    regex = "([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)"
    match_bool = re.search(r"^" + regex + "\." + regex + "\." + regex + "\." + regex + "$", ip)
    if match_bool:
        return "True"
    else:
        return "False"


def main():
    print(validate(input("IPv4 Address: ")))

if __name__ == "__main__":
    main()