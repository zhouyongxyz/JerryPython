# -*- coding: utf-8 -*-
import os;
import  xdrlib ,sys
import xlrd

def open_excel(file= 'HSAE_AutoTest_TestCase_Linux_zhouyong.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

def excel_table_byname(file= 'HSAE_AutoTest_TestCase_Linux_zhouyong.xlsx',colnameindex=0,by_name=u'Bluetooth'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数
    colnames =  table.row_values(colnameindex) #某一行数据
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             app[1] = row[1];
             app[3] = row[3];
             list.append(app)
    return list

def main():
   moudleName = "TestLibBluetooth" #moudle name to generator moudle.robot
   excelName = "HSAE_AutoTest_TestCase_Linux_zhouyong.xlsx" #excel source file
   file = open(moudleName+".robot", "w+");
   bin = "bluetooth_test"
   header = '''*** Settings ***
Suite Setup       Run Keywords    Connect To Device SSH
...               AND    PrepareTest    ${CURDIR}${/}%s.xml
Suite Teardown    Disconnect Device SSH
Variables         ..${/}..${/}..${/}config.py
Library           HSAELinuxTestLibrary

*** Test Cases ***\n''' % moudleName

   file.write(header)
   tables = excel_table_byname(excelName)
   for row in tables:
       print row[1]+" "+row[3]
       file.write(row[3]+"\n")
       file.write("    Run Gtest    "+bin+"    "+row[1]+"    "+row[3]+"\n\n")
   file.close()

if __name__=="__main__":
    main()