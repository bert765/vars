from OpenModule import lstData
from Vars import Num
from Functions import DayHour24, BlockIdx, DataToLists
'''Extracting hour-levels'''


lstHourLvls = []
lstMaxTime, lstMaxLvl, lstMinTime, lstMinLvl = [], [], [], []
lstHiUpTime, lstHiUpLvl, lstHiDwTime, lstHiDwLvl, lstLowHiTime, \
    lstLowHiLvl, lstLowDwTime, lstLowDwLvl = [], [], [], [], [], [], [], []
# create list exclusivly for hour-levels
for n in range(0, 24*Num, 1):
    lstHourLvls.append('-')
for L in (lstMaxTime, lstMaxLvl, lstMinTime, lstMinLvl, lstHiUpTime,
          lstHiUpLvl, lstHiDwTime, lstHiDwLvl, lstLowHiTime,
          lstLowHiLvl, lstLowDwTime, lstLowDwLvl):    
    for n in range(0, Num, 1):
        L.append('-')
# Searching cycle begins
for i in range(0, len(lstData), 1):
    # Needed numbers are next to string
    if type(lstData[i]) == str:
        # Hour-levels search
        if BlockIdx(lstData[i]) == 7:
            z = 0
            while z < 24:
                if str(lstData[i+z+1])[0:2] == '((':
                    break
                if type(lstData[i+z+1]) == int: 
                    lstHourLvls[DayHour24(lstData, i)+z] = lstData[i+z+1]
                z += 1
        # Max and min for a day
        if BlockIdx(lstData[i]) == 8:
            DataToLists(lstData, i, lstMaxTime, lstMaxLvl, lstMinTime, lstMinLvl)
        # Extremums of daily sea levels
        if BlockIdx(lstData[i]) == 9:
            DataToLists(lstData, i, lstHiUpTime, lstHiUpLvl,
                        lstHiDwTime, lstHiDwLvl, lstLowHiTime,
                        lstLowHiLvl, lstLowDwTime, lstLowDwLvl)
