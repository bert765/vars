from OpenModule import lstData, Num
from Functions import DataToLists, BlockIdx
lstVis, lstWeath, lstWDir, lstWSpd, \
lstWGst, lstTemp, lstLevels = [], [], [], [], [], [], []                                   #Creating 'empty' lists to write in later
lstAirTemp, lstAirTempWet, lstPres,  \
lstFullCld, lstLowCld, lstHmdt = [], [], [], [], [], []
lstWaveType, lstWaveDirM, lstWaveDirS, \
lstWaveHav, lstWaveHmx, lstWavePer, lstWaveLen = [], [], [], [], [], [], []
for L in (lstVis, lstWeath, lstWDir, lstWSpd, lstWGst, lstTemp, lstLevels, \
          lstAirTemp, lstAirTempWet, lstPres, lstFullCld,lstLowCld, lstHmdt, \
          lstWaveType, lstWaveDirM, lstWaveDirS, lstWaveHav, lstWaveHmx, \
          lstWavePer, lstWaveLen):                                                         #Filling list with '-' to write data correctly later
    for n in range(0,4*Num,1):
        L.append('-')
for i in range(0,len(lstData),1):                                                          #Searching cycle begins
    if type(lstData[i]) == str:                                                            #Needed numbers are next to string
        if BlockIdx(lstData[i]) == 1 and lstData[i+1] != "-":                               #Looking for full block =01 with data
            DataToLists(lstData, i, lstVis, lstWeath, lstWDir, lstWSpd, \
                        lstWGst, lstTemp, lstLevels)
        if BlockIdx(lstData[i]) == 6 and lstData[i+1] != "-":                                #Looking for full block =06 with data
            DataToLists(lstData, i, lstAirTemp, lstAirTempWet, lstPres, \
                        lstFullCld,lstLowCld, lstHmdt)
        if BlockIdx(lstData[i]) == 2 and lstData[i+1] != "-" and lstData[i+1] != "/":        #Looking for full block =02 with data
            DataToLists(lstData, i, lstWaveType, lstWaveDirM, lstWaveDirS, \
                        lstWaveHav, lstWaveHmx, lstWavePer, lstWaveLen)
print(lstLevels)