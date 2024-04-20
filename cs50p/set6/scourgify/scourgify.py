import sys
import csv
# from tabulate import tabulate

def clean_names(input_file,output_file):
    try:
        with open(input_file,'r') as input:
            reader = csv.DictReader(input)
            with open(output_file,"w") as output:
                header = ["first", "last", "house"]
                writer = csv.DictWriter(output,fieldnames = header)
                writer.writeheader()
                for pupil in reader:
                    last_name,first_name = pupil["name"].split(", ")
                    house = pupil["house"]
                    writer.writerow({"first":first_name,"last":last_name,"house":house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")
        
        
def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else: 
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            print(clean_names(sys.argv[1],sys.argv[2]))
            

if __name__ == '__main__':
    main()
        