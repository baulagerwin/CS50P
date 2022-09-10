from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("Times", "", 40)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 40, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        self.ln(20)

def main():
    name = input("Name: ").strip().title()
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=26)
    pdf.set_text_color(255, 255, 255)
    pdf.image("shirtificate.png", 15, 60, 180)
    pdf.cell(80)
    pdf.cell(30, 200, f"{name} took CS50", border=0, align="C")
    pdf.output("shirtificate.pdf")
    
if __name__ == "__main__":
    main()