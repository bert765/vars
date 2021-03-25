from OpenModule import lstData
'''Write data from text blocks =91...=96 to named lists'''

Info_Mesure, Info_Change, Info_Danger, \
    Info_Crit, Info_Ice1, Info_Ice2 = [], [], [], [], [], []
block_list = {'=91': Info_Mesure, '=92': Info_Change, '=93': Info_Danger,
              '=94': Info_Crit, '=95': Info_Ice1, '=96': Info_Ice2}
for i in range(0, len(lstData), 1):
    if type(lstData[i]) == str:
        if lstData[i] in block_list.keys():
            List_to_write = block_list.get(lstData[i])
            while str(lstData[i+1])[0] != '=':
                List_to_write.append(lstData[i+1])
                i += 1
print(Info_Change)