import sys
import os
from PIL import Image, ImageOps

def main():
    # Check if exactly two command-line arguments are provided
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if input and output file extensions are valid
    valid_extensions = (".jpg", ".jpeg", ".png")

    if not (input_file.lower().endswith(valid_extensions) and output_file.lower().endswith(valid_extensions)):
        sys.exit("Error: Both input and output files must be in .jpg, .jpeg, or .png format")

    # Ensure input and output have the same extension
    if os.path.splitext(input_file)[1].lower() != os.path.splitext(output_file)[1].lower():
        sys.exit("Error: Input and output file extensions must match")

    # Check if the input file exists
    if not os.path.exists(input_file):
        sys.exit(f"Error: Input file '{input_file}' does not exist")

    try:
        # Open the input image
        input_image = Image.open(input_file)

        # Open the shirt image
        shirt_image = Image.open("shirt.png")

        # Resize and crop the input image to match the size of the shirt image
        input_image = ImageOps.fit(input_image, shirt_image.size)

        # Overlay the shirt image on top of the input image
        input_image.paste(shirt_image, (0, 0), shirt_image)

        # Save the result to the output file
        input_image.save(output_file)

    except Exception as e:
        sys.exit(f"Error processing the image: {e}")

if __name__ == "__main__":
    main()
