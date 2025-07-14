import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Create a list of Excel filepaths
filepaths = glob.glob("invoices/*.xlsx")

# Go through each Excel file
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # Create one PDF file for each filepath
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    # Add a page to each PDF document per Excel file
    pdf.add_page()
    # Get the filename without extension
    # and separate the invoice number and date from filename
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date. {date}", ln=1)


    pdf.output(f"PDFs/{filename}.pdf")