import random
from openpyxl import Workbook

wb = Workbook()
dest_filename = 'order.xlsx'

ws1 = wb.active
ws1.title = 'test'

# 生成随机数
def create_num():
    num = random.randint(1000000, 9999999)
    return num

# 将生成的随机数写在excel 中
for i in range(1, 1000):
    ws1.cell(column=1, row = i).value = create_num()

wb.save(filename = dest_filename)