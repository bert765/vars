from OpenModule import lstData, Num
from Functions import DataToLists, ObjectNumCheck
'''write data from blocks =26 and = 27 to list of lists'''
lstDataIce26_1, lstDataIce26_2 = [], []
lstDataIce27_1, lstDataIce27_2 = [], []
for x in range(0,6,1):
    lstDataIce26_1.append([])
    lstDataIce26_2.append([])
    lstDataIce27_1.append([])
    lstDataIce27_2.append([])
    for y in range(0,Num,1):
        lstDataIce26_1[x].append('-')
        lstDataIce26_2[x].append('-')
        lstDataIce27_1[x].append('-')
        lstDataIce27_2[x].append('-')
for i in range(0,len(lstData),1):                                                    #Searching cycle begin
    if type(lstData[i]) == str:                                                      #Needed numbers are next to string
        if lstData[i] == '=26' and lstData[i+1] != "-":                              #Looking for full block =21 with data
            if ObjectNumCheck(lstData, i) == 1:                                      # data for 1 ice object
                DataToLists(lstData, i, *lstDataIce26_1)
            elif ObjectNumCheck(lstData, i) == 2:                                    # data for 2 ice object
                DataToLists(lstData, i, *lstDataIce26_2)
        if lstData[i] == '=27' and lstData[i+1] != "-":                              #Looking for full block =21 with data
            if ObjectNumCheck(lstData, i) == 1:                                      # data for 1 ice object
                DataToLists(lstData, i, *lstDataIce27_1)
            elif ObjectNumCheck(lstData, i) == 2:                                    # data for 2 ice object
                DataToLists(lstData, i, *lstDataIce27_2)   