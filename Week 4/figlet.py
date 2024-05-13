

import sys
from pyfiglet import Figlet
figlet = Figlet()


def main():

    if len(sys.argv) not in (1, 3) or \
       len(sys.argv) == 3 and (sys.argv[1] not in ("-f", "--font")) or \
       len(sys.argv) == 3 and (sys.argv[2] not in (figlet.getFonts())):
        sys.exit("""Usage:  Random font: python figlet.py
        Choose font: python figlet.py [-f, --font] font_name""")

    # Set font to font specified as command line argument
    if len(sys.argv) == 3:
        figlet.setFont(font=sys.argv[2])

    # Figlicize input
    figlicize("Input: ")


def figlicize(prompt):
    print(f"""Output:
{figlet.renderText(input(prompt))}""")


if __name__ == "__main__":
    main()