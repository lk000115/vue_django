import pandas as pd
df = pd.read_excel('gz.xlsx')

# from openpyxl  import load_workbook 

# wb = load_workbook(filename='gz.xlsx')
# st = wb.sheetnames[0]    # 获取表格的第一个工作表名
# sheet = wb[st]

print(df)

