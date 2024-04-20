import sys


def count_lines_in_a_file(file_name):
    try:
        line_count = 0
        with open(file_name,'r') as file:
            lines = file.readlines()
            for line in lines:
                if  not (line.lstrip().startswith("#") or line.strip()==""):
                    line_count+=1
        return line_count
    except FileNotFoundError:
        sys.exit("File does not exist")
        
        
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a python file")
        else:
            print(count_lines_in_a_file(sys.argv[1]))
            

if __name__ == '__main__':
    main()
        