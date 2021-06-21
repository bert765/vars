from OpenModule import open_file
from Vars import files, file_dir
from Data_01_02_06 import data_hy_met
from Data_Levels import hour_levels
from Data_ICE21 import ice21
from Data_ICE22 import ice22
from Data_ICE23 import ice23
from Data_ICE24 import ice24
from Data_ICE26 import ice26
from DataSal import sal

for file in files:
    Data, Num = open_file(file_dir, file)
    x = data_hy_met(Data, Num)
    print(x[6])