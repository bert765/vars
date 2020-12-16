from OpenModule import lstData, Num
from Functions import DataToLists, ObjectNumCheck
'''write data from block =23 to list of lists'''
#copypaste DataICE22
lstDataIce23_1, lstDataIce23_2 = [], []
for x in range(0,22,1):
    lstDataIce23_1.append([])
    lstDataIce23_2.append([])
    for y in range(0,Num,1):
        lstDataIce23_1[x].append('-')
        lstDataIce23_2[x].append('-')
for i in range(0,len(lstData),1):                                                    #Searching cycle begin
    if type(lstData[i]) == str:                                                      #Needed numbers are next to string
        if lstData[i] == '=23' and lstData[i+1] != "-":                              #Looking for full block =23 with data
            if ObjectNumCheck(lstData, i) == 1:                                      #and data for 1 ice object
                DataToLists(lstData, i, *lstDataIce23_1)
            if ObjectNumCheck(lstData, i) == 2:                                      #and data for 1 ice object
                DataToLists(lstData, i, *lstDataIce23_2)