import math
def fuel():
    while True:
        try:
            f = input("Fraction:")
            if '.' in f:
                raise ValueError
            x,y = map(int,f.split("/"))
            if x > y:
                raise ValueError
            result = float(x)/float(y)
            if result <= 0.1:
                return "E"
            elif result >=0.9:
                return "F"
            else:
                # print(result)
                # print(math.ceil(result,2))
                return ("{:.0%}".format(result))
        
        except ValueError or ZeroDivisionError:
            pass

    
    
def main():
    res = fuel()
    print(res)
    
if __name__ == "__main__":
    main()