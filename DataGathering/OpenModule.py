import os
from Functions import emptyTest, NumberOfDays
'''Open, read and parsing data from file separate by commas.
   Delete all empty values in list.'''


os.chdir(r'C:\BEREGWIN\ISX')
flmne = "mpo89024.820"
Fl = open(flmne, "r")
strFile = Fl.read()
lstLines = strFile.splitlines()
lstData = []
for i in lstLines:
    lstData = lstData + i.split(',')        # Splitting by ','
for i in lstData:
    if emptyTest(i):              # Delete empty values
        lstData.remove(i)
for i in range(0, len(lstData), 1):       # Change str to int if possible
    try:
        lstData[i] = int(lstData[i])
    except Exception:
        pass
Num = NumberOfDays(lstData[3], lstData[2])      # Calculate amount of days in month
