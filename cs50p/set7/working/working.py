import re




def convert(s):
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match_time = re.search(r"^" + regex + " to " + regex + "$", s)
    if match_time:
        from_time = standardize_time(match_time.group(1), match_time.group(2), match_time.group(3))
        time = standardize_time(match_time.group(4), match_time.group(5), match_time.group(6))
        return f"{from_time} to {time}"
    else:
        raise ValueError


def standardize_time(hr, min, x):
    if hr == "12":
        if x == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        if x == "AM":
            hour = f"{int(hr):02}"
        else:
            hour = f"{int(hr)+12}"
    if min == None:
        minute = "00"
    else:
        minute = f"{int(min):02}"
    return f"{hour}:{minute}"



def main():
    print(convert(input("Hours: ")))

if __name__ == "__main__":
    main()