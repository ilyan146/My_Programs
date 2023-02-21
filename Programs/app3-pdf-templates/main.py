from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read_csv("003 topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", size=24, style="B")
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, align="L", ln=1, txt=row["Topic"], border=0)
    pdf.line(10,21,200,21)


pdf.output("output.pdf")

