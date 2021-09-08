import pandas as pd
import glob
import os
from openpyxl.workbook import Workbook
from openpyxl.styles import  Border, Side, Alignment, Font

location = 'E:\\MAGESH\\12 Anna University\\2nd Sem\\Dlab\\*.xlsx'
excel_files = glob.glob(location)

writer = pd.ExcelWriter('E:\\MAGESH\\12 Anna University\\2nd Sem\\combine\\multi_sheet.xlsx')

for excel in excel_files:
    sheet = (os.path.basename(excel).split('-')[0].split(' ')[1])
    df1 = pd.read_excel(excel)
    df1.to_excel(writer,sheet_name=sheet)
writer.save()