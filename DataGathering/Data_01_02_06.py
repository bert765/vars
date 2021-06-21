def data_hy_met(lstData, Num):
    """Search through lstData for values in blocks = 01, =02, =03
       Return as tuple"""
    from Functions import DataToLists, BlockIdx

    # Creating 'empty' lists to write in later
    lstVis, lstWeath, lstWDir, lstWSpd, \
        lstWGst, lstTemp, lstLevels = [], [], [], [], [], [], []
    lstAirTemp, lstAirTempWet, lstPres, \
        lstFullCld, lstLowCld, lstHmdt = [], [], [], [], [], []
    lstWaveType, lstWaveDirM, lstWaveDirS, \
        lstWaveHav, lstWaveHmx, lstWavePer, lstWaveLen = [], [], [], [], [], [], []
    for L in (lstVis, lstWeath, lstWDir, lstWSpd, lstWGst, lstTemp, lstLevels,
              lstAirTemp, lstAirTempWet, lstPres, lstFullCld, lstLowCld, lstHmdt,
              lstWaveType, lstWaveDirM, lstWaveDirS, lstWaveHav, lstWaveHmx,
              lstWavePer, lstWaveLen):  # Filling list with '-' to write data correctly later
        for n in range(0, 4 * Num, 1):
            L.append('-')
    for i in range(0, len(lstData), 1):  # Searching cycle begins
        if type(lstData[i]) == str:  # Needed numbers are next to string
            # Looking for full block =01 with data
            if BlockIdx(lstData[i]) == 1 and lstData[i + 1] != "-":
                DataToLists(lstData, i, lstVis, lstWeath, lstWDir, lstWSpd,
                            lstWGst, lstTemp, lstLevels)
            # Looking for full block =06 with data
            if BlockIdx(lstData[i]) == 6 and lstData[i + 1] != "-":
                DataToLists(lstData, i, lstAirTemp, lstAirTempWet, lstPres,
                            lstFullCld, lstLowCld, lstHmdt)
            # Looking for full block =02 with data
            if BlockIdx(lstData[i]) == 2 and lstData[i + 1] != "-" and lstData[i + 1] != "/":
                DataToLists(lstData, i, lstWaveType, lstWaveDirM, lstWaveDirS,
                            lstWaveHav, lstWaveHmx, lstWavePer, lstWaveLen)
    return lstVis, lstWeath, lstWDir, lstWSpd, lstWGst, lstTemp, lstLevels