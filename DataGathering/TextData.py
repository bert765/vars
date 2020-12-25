from OpenModule import lstData
from Functions import DataToLists
'''Write data from text blocks =91...=96'''
Info_Mesure, Info_Change, Info_Danger, \
Info_Ice1, Info_Ice2 = [], [], [], [], []
for i in range(0,len(lstData),1):                                                          
    if type(lstData[i]) == str:                                                            
        if lstData[i] == '=91':
            DataToLists(lstData,i,Info_Mesure)
    
    