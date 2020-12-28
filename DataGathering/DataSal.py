from OpenModule import lstData, Num
'''Write water salinity (=31,=32,=33) and 
   dencity (=41,=42,=43) data to lists'''
from Functions import IsData
lstDataSal, lstDataDen = [], []
for x in range(0,Num,1):
    lstDataSal.append('-')
    lstDataDen.append('-')
for i in range(0,len(lstData),1):
    if type(lstData[i]) == str and (lstData[i] == '=31' or lstData[i] == '=41' or
                                    lstData[i] == '=32' or lstData[i] == '=42' or
                                    lstData[i] == '=33' or lstData[i] == '=43'):
        n = (int(lstData[i][-1])-1)*10 
        if int(lstData[i][-2]) == 3 and type(lstData[i+1]) == int:                                       #Check for short block like =31,-,
            i+=2
            while IsData(lstData[i]) == True and n < Num:
                lstDataSal[n] = lstData[i] 
                i+=1
                n+=1                                
        elif int(lstData[i][-2]) == 4:                                      #Same route for dencity (=41...)
            i+=1
            while IsData(lstData[i]) == True and n < Num:
                lstDataDen[n] = lstData[i] 
                i+=1
                n+=1            