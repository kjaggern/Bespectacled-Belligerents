from openpyxl import load_workbook

data1 = ['class', 'conduct', 'ph', 'rgb']
data2 = [0, 3, 2, 4]

wb = load_workbook("book2.xlsx")
ws = wb.worksheets[0]

ws.append(data1)
ws.append(data2)

wb.save("book2.xlsx")
