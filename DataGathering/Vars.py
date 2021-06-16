"""Variables and paths for other modules"""

from Functions import NumberOfDays
file_dir = r'O:\ГМЦ\Отдел гидрометеорологии\Виталий\BEREGWIN\ISX RES TAB ПРОВЕРЕННЫЕ\89011 Амдерма\2020\ISX'
files = 'mpo89011.c20'
month = files[-3]
year = files[-2:]
Num = NumberOfDays(year,month)
