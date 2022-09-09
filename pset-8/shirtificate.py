from fpdf import FPDF

def main():
    pdf = FPDF()
    pdf.add_page()
    # Set font
    pdf.set_font('Arial', 'B', 16)
    # Move to 8 cm to the right
    pdf.cell(80)
    # Centered text in a framed 20*10 mm cell and line break
    pdf.cell(20, 10, 'Title', 1, 1, 'C')
    pdf.output("shirtificate.pdf")
    
if __name__ == "__main__":
    main()
    
    # image
    # write
    # text
    # output