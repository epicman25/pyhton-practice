from PIL import Image, ImageOps
import sys
import os



def replace_tshirt(input_file, output_file):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input_file) as input:
            cropped_input = ImageOps.fit(input, shirt.size)
            cropped_input.paste(shirt, mask = shirt)
            cropped_input.save(output_file)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        format = [".jpg", ".jpeg", ".png"]
        inp = os.path.splitext(sys.argv[1])
        outp = os.path.splitext(sys.argv[2])
        if outp[1].lower() not in format:
            sys.exit("Invalid output")
        elif inp[1].lower() != outp[1].lower():
            sys.exit("Input and output have different extensions")
        else:
            replace_tshirt(sys.argv[1], sys.argv[2])




if __name__ == "__main__":
    main()