from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("003 topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    #Set header
    pdf.set_font(family="Times", size=24, style="B")
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, align="L", ln=1, txt=row["Topic"], border=0)
    pdf.line(10,21,200,21)

    #Set footer
    pdf.ln(265)
    pdf.set_font(family="Times", size=8, style="I")
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, align="R", ln=1, txt=row["Topic"], border=0)



    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set footer
        pdf.ln(277)
        pdf.set_font(family="Times", size=8, style="I")
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, align="R", ln=1, txt=row["Topic"], border=0)


pdf.output("output.pdf")

