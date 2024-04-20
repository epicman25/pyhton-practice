import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
args = ["--font","-f"]


def main():

    if len(sys.argv) > 2 and sys.argv[1] in args and sys.argv[2] in figlet.getFonts():
        font = sys.argv[2]
        convert_to_figlet("Input: ", font)
    elif len(sys.argv) < 2:
        font = random.choice(figlet.getFonts())
        convert_to_figlet("Input: ", font)
    else:
        sys.exit("Invalid usage")


def convert_to_figlet(prompt, font):
    txt = input(prompt)
    figlet.setFont(font=font)
    print(figlet.renderText(txt))


main()