# figlet.py
import sys
import random
import pyfiglet

def main():
    # Check the number of command-line arguments
    if len(sys.argv) == 1:
        # No font specified, use a random font
        font = random.choice(pyfiglet.FigletFont.getFonts())
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        # Check if the font is valid
        font = sys.argv[2]
        if font not in pyfiglet.FigletFont.getFonts():
            sys.exit("Error: Invalid font name.")
    else:
        sys.exit("Usage: figlet.py [-f font_name]")

    # Prompt the user for input text
    text = input("Input: ")

    # Generate ASCII art using the specified or random font
    figlet = pyfiglet.Figlet(font=font)
    output = figlet.renderText(text)

    # Output the ASCII art text
    print(output)

if __name__ == "__main__":
    main()
