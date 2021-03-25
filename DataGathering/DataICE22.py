from OpenModule import lstData, Num
from Functions import DataToLists, ObjectNumCheck

'''write data from block =22 to list of lists'''
lstDataIce22_1, lstDataIce22_2 = [], []
# yeah, don't wanna manually write vars, cycles is better this time
for x in range(0, 19, 1):
    lstDataIce22_1.append([])
    lstDataIce22_2.append([])
    for y in range(0, Num, 1):
        lstDataIce22_1[x].append('-')
        lstDataIce22_2[x].append('-')
for i in range(0, len(lstData), 1):  # Searching cycle begin
    if type(lstData[i]) == str:  # Needed numbers are next to string
        if lstData[i] == '=22' and lstData[i + 1] != "-":  # Looking for full block =22 with data
            if ObjectNumCheck(lstData, i) == 1:  # and data for 1 ice object
                DataToLists(lstData, i, *lstDataIce22_1)
            if ObjectNumCheck(lstData, i) == 2:  # and data for 1 ice object
                DataToLists(lstData, i, *lstDataIce22_2)
