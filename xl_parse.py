import xlrd

path = "data.xlsx"

input_workbook = xlrd.open_workbook(path)
worksheet = input_workbook.sheet_by_index(0)

print(worksheet.nrows)  # number of populated rows
print(worksheet.ncols)  # number of populated cols

table = {}
for i in range(1, worksheet.nrows):
    for j in range(0, worksheet.ncols):
        print(worksheet.cell_value(i, j))  # accesses table cell

print(table)
