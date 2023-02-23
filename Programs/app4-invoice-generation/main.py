import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for i in filepaths:
    df = pd.read_excel(i, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(i).stem
    invoice_nr = filename.split("-")[0][4:]
    inv_date = filename.split("-")[1]

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Date: {inv_date}", ln=2)

    output = pdf.output(f"PDFs/{filename[4:]}.pdf")
