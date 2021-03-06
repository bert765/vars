def ice24(lstData, Num):
    """write data from block =24 to list of lists"""
    from Functions import DataToLists, ObjectNumCheck

    # copypaste DataICE22
    lstDataIce24_1, lstDataIce24_2 = [], []
    for x in range(0, 7, 1):
        lstDataIce24_1.append([])
        lstDataIce24_2.append([])
        for y in range(0, Num, 1):
            lstDataIce24_1[x].append('-')
            lstDataIce24_2[x].append('-')
    # Searching cycle begin
    for i in range(0, len(lstData), 1):
        # Needed numbers are next to string
        if type(lstData[i]) == str:
            # Looking for full block =24 with data
            if lstData[i] == '=24' and lstData[i+1] != "-":
                # and data for 1 ice object
                if ObjectNumCheck(lstData, i) == 1:
                    DataToLists(lstData, i, *lstDataIce24_1)
                # and data for 1 ice object
                if ObjectNumCheck(lstData, i) == 2:
                    DataToLists(lstData, i, *lstDataIce24_2)
    return lstDataIce24_1, lstDataIce24_2
