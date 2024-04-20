from datetime import date
import inflect
import sys
import operator

eng = inflect.engine()





def convert(time):
    minutes = time * 24 * 60
    return f"{(eng.number_to_words(minutes, andword='')).capitalize()} minutes"

def main():
    try:
        dob = input("Date of Birth: ")
        difference = operator.sub(date.today(), date.fromisoformat(dob))
        print(convert(difference.days))
    except ValueError:
        sys.exit("Invalid date")
        
if __name__ == "__main__":
    main()