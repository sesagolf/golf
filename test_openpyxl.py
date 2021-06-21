import pandas as pd
import openpyxl
from openpyxl import load_workbook
import time
import datetime
import requests
from openpyxl.utils.dataframe import dataframe_to_rows
dt = datetime.datetime.now()
dt_real = dt.strftime('%d/%B/%Y')

all_row = int(input("Please input the all of data row: "))#ต้องการเก็บข้อมูลกี่แถว
all_row_for_count_int = all_row+1
all_row1 = list(range(1, all_row+2))
count_L1 = 'D'
count_time1 = 'C'
#def first_run() :
    #for i in range(1, all_row_for_count_int) :

        #workbook = load_workbook('https://github.com/sesagolf/golf/blob/b7e049df194ec9a7f9582d31a0a556c32a475b6b/Test_screw_data.xlsx')
df = pd.read_excel("https://github.com/sesagolf/golf/blob/b7e049df194ec9a7f9582d31a0a556c32a475b6b/Test_screw_data.xlsx?raw=true")
worksheet1 = df.to_excel("in_python.xlsx")
print(worksheet1)
        #เริ่มฝั่ง L
        #count_L2 = str(all_row1[i])
        #count_L_all = count_L1 + count_L2
        #L_start = worksheet[count_L_all]
        #add_new_L = float(input("input the values of L: "))
        #L_start.value = add_new_L
        #จบฝั่ง L

        #เริ่ม Time
        #Time_value = count_time1 + count_L2
        #worksheet[Time_value] = dt_real
        #จบ Time

        #workbook.save('Test_screw_data.xlsx')
        #old_data = pd.read_excel("Test_screw_data.xlsx")
        #print('This is lastest excel data')#ข้อมูลล่าสุดที่กรอก
        #print(old_data)
#first_run()

