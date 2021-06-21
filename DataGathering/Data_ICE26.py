def ice26(lstData, Num):
    """write data from blocks =26 and = 27 to list of lists"""
    from Functions import DataToLists, ObjectNumCheck

    lstDataIce26_1, lstDataIce26_2 = [], []
    lstDataIce27_1, lstDataIce27_2 = [], []
    for x in range(0, 6, 1):
        lstDataIce26_1.append([])
        lstDataIce26_2.append([])
        lstDataIce27_1.append([])
        lstDataIce27_2.append([])
        for y in range(0, Num, 1):
            lstDataIce26_1[x].append('-')
            lstDataIce26_2[x].append('-')
            lstDataIce27_1[x].append('-')
            lstDataIce27_2[x].append('-')
    # Searching cycle begin
    for i in range(0, len(lstData), 1):
        # Needed numbers are next to string
        if type(lstData[i]) == str:
            # Looking for full block =21 with data
            if lstData[i] == '=26' and lstData[i+1] != "-":
                # data for 1 ice object
                if ObjectNumCheck(lstData, i) == 1:
                    DataToLists(lstData, i, *lstDataIce26_1)
                # data for 2 ice object
                elif ObjectNumCheck(lstData, i) == 2:
                    DataToLists(lstData, i, *lstDataIce26_2)
            # Looking for full block =21 with data
            if lstData[i] == '=27' and lstData[i+1] != "-":
                # data for 1 ice object
                if ObjectNumCheck(lstData, i) == 1:
                    DataToLists(lstData, i, *lstDataIce27_1)
                # data for 2 ice object
                elif ObjectNumCheck(lstData, i) == 2:
                    DataToLists(lstData, i, *lstDataIce27_2)
    return lstDataIce26_1, lstDataIce26_2, lstDataIce27_1, lstDataIce27_2
