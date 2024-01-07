from openpyxl import load_workbook
from color_recog import color_bgr
import numpy as np

data1 = ['b','g','r']
data2 = color_bgr().tolist()

wb = load_workbook("book2.xlsx")
ws = wb.worksheets[0]

ws.append(data1)
ws.append(data2)

wb.save("book2.xlsx")
