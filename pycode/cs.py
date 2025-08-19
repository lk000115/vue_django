# import pandas as pd
# df = pd.read_excel('gz.xlsx')

# from openpyxl  import load_workbook 

# wb = load_workbook(filename='gz.xlsx')
# st = wb.sheetnames[0]    # 获取表格的第一个工作表名
# sheet = wb[st]

# print(df)

# 形参前面的*表示把传入的多个位置参数打包成一个元组
def fn(*args):
    for i in args:
        print(i)

lt = [1, 2, 3, 4, 5]
# 实参前面的*表示把列表打散成多个位置参数
fn(*lt)    

