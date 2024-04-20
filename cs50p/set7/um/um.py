import re



def count(s):
    regex_patt = "(^|\W)um($|\W)"
    match_bool = re.findall(regex_patt, s, re.IGNORECASE)
    if match_bool:
        return(len(match_bool))



def main():
    print(count(input("Text: ")))
    
    
if __name__ == "__main__":
    main()