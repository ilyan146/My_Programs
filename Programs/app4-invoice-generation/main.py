import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for i in filepaths:

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(i).stem
    invoice_nr = filename.split("-")[0][4:]
    inv_date = filename.split("-")[1]

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Date: {inv_date}", ln=1)

    pdf.ln(20)

    df = pd.read_excel(i, sheet_name="Sheet 1")

    column = df.columns
    headers = [item.replace("_"," ").title() for item in column]

    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=headers[0],border=1)
    pdf.cell(w=70, h=8, txt=headers[1],border=1)
    pdf.cell(w=35, h=8, txt=headers[2],border=1)
    pdf.cell(w=30, h=8, txt=headers[3],border=1)
    pdf.cell(w=30, h=8, txt=headers[4],border=1, ln=1)


    for index,row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=35, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=35, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # Total sum sentence
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=f"The total price is {total_sum}", ln=1)

    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=25, h=8, txt="PythonHow")
    pdf.image("004 pythonhow.png", w=10)


    output = pdf.output(f"PDFs/{filename[4:]}.pdf")
