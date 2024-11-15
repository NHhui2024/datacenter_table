import openpyxl

wb = openpyxl.load_workbook('modified_excel_file.xlsx')

sheet = wb['Sheet1']

column_letter = 'B'

for cell in sheet[column_letter]:
    if cell.value:
        cell.value = f"-{cell.value}"

wb.save('modified_excel_file2.xlsx')
