import openpyxl
import set_methods as sm
from openpyxl import load_workbook

wb = load_workbook(filename = "two_tables.xlsx")
ws1 = wb['Sheet1']
ws2 = wb['Sheet2']

cell_range1 = ws1['A1:D19']
cell_range2 = ws2['A1:D19']

my_tuples = sm.tuple_tables(cell_range1, cell_range2)

print(sm.differences_between_tuples(my_tuples))
# defined_excel_ranges = [cell_range1, cell_range2]
