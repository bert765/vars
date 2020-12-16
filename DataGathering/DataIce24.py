from OpenModule import lstData, Num
from Functions import DataToLists, ObjectNumCheck
'''write data from block =24 to list of lists'''
#copypaste DataICE22
lstDataIce24_1, lstDataIce24_2 = [], []
for x in range(0,7,1):
    lstDataIce24_1.append([])
    lstDataIce24_2.append([])
    for y in range(0,Num,1):
        lstDataIce24_1[x].append('-')
        lstDataIce24_2[x].append('-')
for i in range(0,len(lstData),1):                                                    #Searching cycle begin
    if type(lstData[i]) == str:                                                      #Needed numbers are next to string
        if lstData[i] == '=24' and lstData[i+1] != "-":                              #Looking for full block =24 with data
            if ObjectNumCheck(lstData, i) == 1:                                      #and data for 1 ice object
                DataToLists(lstData, i, *lstDataIce24_1)
            if ObjectNumCheck(lstData, i) == 2:                                      #and data for 1 ice object
                DataToLists(lstData, i, *lstDataIce24_2)