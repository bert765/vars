import os
from Functions import emptyTest, NumberOfDays
'''Open, read and parsing data from file separate by commas.
   Delete all empty values in list.'''
os.chdir(r'D:\BEREGWIN\ISX')
flmne = "mpo89039.220"
Fl = open(flmne, "r")
strFile=Fl.read()
Fl.close
lstLines=strFile.splitlines()
lstData=[]
for i in lstLines:
    lstData=lstData+i.split(',')        #Splitting by ','
for i in lstData:
    if emptyTest(i)==True:              #Delete empty values
        lstData.remove(i)
for i in range(0,len(lstData),1):       #Change str to int if possible
    try:
        lstData[i]=int(lstData[i])
    except Exception:
        pass
Num = NumberOfDays(lstData[3],lstData[2])      #Calculate amount of days in month