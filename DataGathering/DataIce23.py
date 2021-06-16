from OpenModule import lstData
from Vars import Num
from Functions import DataToLists, ObjectNumCheck
'''write data from block =23 to list of lists'''


# copypaste DataICE22
lstDataIce23_1, lstDataIce23_2 = [], []
for x in range(0, 22, 1):
    lstDataIce23_1.append([])
    lstDataIce23_2.append([])
    for y in range(0, Num, 1):
        lstDataIce23_1[x].append('-')
        lstDataIce23_2[x].append('-')
# Searching cycle begin
for i in range(0, len(lstData), 1):
    # Needed numbers are next to string
    if type(lstData[i]) == str:
        # Looking for full block =23 with data
        if lstData[i] == '=23' and lstData[i+1] != "-":
            # and data for 1 ice object
            if ObjectNumCheck(lstData, i) == 1:
                DataToLists(lstData, i, *lstDataIce23_1)
            # and data for 1 ice object
            if ObjectNumCheck(lstData, i) == 2:
                DataToLists(lstData, i, *lstDataIce23_2)
