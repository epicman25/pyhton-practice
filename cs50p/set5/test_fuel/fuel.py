import math


def convert(frac):
    x,y = frac.split("/")
    if int(x)/int(y)>1:
        raise ValueError
    if int(y)==0:
        raise ZeroDivisionError
    return int(x)/int(y)*100

def gauge(percent):
    try:
        if 0 <= percent <= 1:
            return "E"
        elif 99 <= percent <= 100:
            return "F"
        elif 1 <= percent <= 98:
            return str(math.ceil(percent)) + "%"
        else:
            raise TypeError
    except TypeError:
        pass
    
    
def main():
    fraction = input("Enter fraction:")
    res = convert(fraction)
    print(gauge(res))
    
if __name__ == "__main__":
    main()