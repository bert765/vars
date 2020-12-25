from OpenModule import lstData, Num
from Functions import DayHour24, BlockIdx, DataToLists
'''Extracting hour-levels'''
lstHourLvls = []
lstMaxTime, lstMaxLvl, lstMinTime, lstMinLvl = [], [], [], []
lstHiUpTime, lstHiUpLvl, lstHiDwTime, lstHiDwLvl, lstLowHiTime, \
lstLowHiLvl, lstLowDwTime, lstLowDwLvl = [], [], [], [], [], [], [], []    
for n in range(0,24*Num,1):                                                                #create list exclusivly for hour-levels 
    lstHourLvls.append('-')
for L in (lstMaxTime, lstMaxLvl, lstMinTime, lstMinLvl,lstHiUpTime, \
          lstHiUpLvl, lstHiDwTime, lstHiDwLvl, lstLowHiTime, \
          lstLowHiLvl, lstLowDwTime, lstLowDwLvl):    
    for n in range(0,Num,1):
        L.append('-')
for i in range(0,len(lstData),1):                                                          #Searching cycle begins
    if type(lstData[i]) == str:                                                            #Needed numbers are next to string
        if BlockIdx(lstData[i]) == 7:                                                       #Hour-levels search
            z=0
            while z < 24:
                if str(lstData[i+z+1])[0:2] == '((':
                    break
                if type(lstData[i+z+1]) == int: 
                    lstHourLvls[DayHour24(lstData,i)+z] = lstData[i+z+1]
                z+=1
        if BlockIdx(lstData[i]) == 8:                                                       #Max and min for a day
            DataToLists(lstData, i, lstMaxTime, lstMaxLvl, lstMinTime, lstMinLvl)
        if BlockIdx(lstData[i]) == 9:                                                       #Extremums of daily sea levels
            DataToLists(lstData, i, lstHiUpTime, lstHiUpLvl, \
                        lstHiDwTime, lstHiDwLvl, lstLowHiTime, \
                        lstLowHiLvl, lstLowDwTime, lstLowDwLvl)
print(lstHourLvls)