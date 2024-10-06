from fpdf import FPDF
import os

def create_shirtificate(name):
    # Check if the shirt image exists
    if not os.path.exists("shirtificate.png"):
        print("Error: 'shirtificate.png' not found.")
        return

    # Create a PDF document
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    # Set title
    pdf.set_font("Arial", 'B', 30)
    pdf.cell(0, 40, "CS50 Shirtificate", 0, 1, 'C')

    # Add the shirt image
    try:
        pdf.image("shirtificate.png", x = 15, y = 50, w = 180)
    except Exception as e:
        print(f"Error inserting image: {e}")
        return

    # Set name font and color
    pdf.set_font("Arial", 'I', 40)
    pdf.set_text_color(0, 0, 0)  # Black text

    # Calculate the width of the name to center it
    name_width = pdf.get_string_width(name)
    pdf.set_xy((210 - name_width) / 2, 100)  # Center horizontally on the shirt
    pdf.cell(name_width, 40, name)

    # Output the PDF to a file
    try:
        pdf.output("shirtificate.pdf")
        print("PDF generated successfully as 'shirtificate.pdf'.")
    except Exception as e:
        print(f"Error generating PDF: {e}")

def main():
    name = input("What is your name? ")
    create_shirtificate(name)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
