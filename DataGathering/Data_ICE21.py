from OpenModule import lstData
from Vars import Num
from Functions import DataToLists, ObjectNumCheck

''' Write ice data after blocks =21, =25 into lists. 
    Its always have constant amount of parts
    unlike =22,=23,=24'''
lstIceTime1, lstIceVis1, lstIceWDir1, lstIceWSpd1, \
    lstIceTa1, lstIceTw1 = [], [], [], [], [], [],
lstChar11, lstChar12, lstChar13, lstChar14, lstChar15, \
    lstChar16 = [], [], [], [], [], []
lstIceTime2, lstIceVis2, lstIceWDir2, lstIceWSpd2, \
    lstIceTa2, lstIceTw2 = [], [], [], [], [], []
lstChar21, lstChar22, lstChar23, lstChar24, lstChar25, \
    lstChar26 = [], [], [], [], [], []
for L in (lstIceTime1, lstIceVis1, lstIceWDir1, lstIceWSpd1,
          lstIceTa1, lstIceTw1, lstIceTime2, lstIceVis2,
          lstIceWDir2, lstIceWSpd2, lstIceTa2, lstIceTw2,
          lstChar11, lstChar12, lstChar13, lstChar14, lstChar15,
          lstChar16, lstChar21, lstChar22, lstChar23, lstChar24,
          lstChar25, lstChar26):
    for n in range(0, Num, 1):
        L.append('-')
for i in range(0, len(lstData), 1):  # Searching cycle begin
    if type(lstData[i]) == str:  # Needed numbers are next to string
        if lstData[i] == '=21' and lstData[i + 1] != "-":  # Looking for full block =21 with data
            if ObjectNumCheck(lstData, i) == 1:  # and data for 1 ice object
                DataToLists(lstData, i, lstIceTime1, lstIceVis1,
                            lstIceWDir1, lstIceWSpd1, lstIceTa1,
                            lstIceTw1)
            elif ObjectNumCheck(lstData, i) == 2:  # and data for 2 ice object
                DataToLists(lstData, i, lstIceTime2, lstIceVis2,
                            lstIceWDir2, lstIceWSpd2, lstIceTa2,
                            lstIceTw2)
        if lstData[i] == '=25':  # Looking for full block =21 with data
            if ObjectNumCheck(lstData, i) == 1:  # and data for 1 ice object
                DataToLists(lstData, i, lstChar11, lstChar12,
                            lstChar13, lstChar14, lstChar15,
                            lstChar16)
            elif ObjectNumCheck(lstData, i) == 2:  # and data for 2 ice object
                DataToLists(lstData, i, lstChar21, lstChar22,
                            lstChar23, lstChar24, lstChar25,
                            lstChar26)
