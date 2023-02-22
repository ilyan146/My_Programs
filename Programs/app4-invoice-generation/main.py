import pandas as pd
import openpyxl
import glob

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for i in filepaths:
    df = pd.read_excel(i)
    print(df)
