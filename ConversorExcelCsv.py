import pandas as pd
import csv
import os

for excelFile in os.listdir('.'):
    if not excelFile.endswith('.xlsx'):
        continue
    df = pd.read_excel(excelFile)  # sheetname is optional
    df.to_csv(excelFile, index=False)  # index=False prevents pandas to write row index   
    


