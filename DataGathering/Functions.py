import os


# dict for function NumberOfDays
Sw = {1: 31, 2: 28, 3: 31, 4: 30,
      5: 31, 6: 30, 7: 31, 8: 31,
      9: 30, 10: 31, 11: 30, 12: 31}


def emptyTest(lst):
    # Check for only spaces element in list
    for x in lst:
        if x == " ":
            pass
        else:
            return False
    return True


def NumberOfDays(Year, Month):
    # Check the month, year and return amount of day in it
    if type(Month) is not int:
        month_letters = ['a', 'b', 'c']
        if Month in month_letters:
            Month = 10 + month_letters.index(Month)
    if int(Year) % 4 == 0 and int(Month) == 2:
        return 29
    else:
        return Sw.get(Month)


def DayHour(lst, pos):
    # Function that handle given day-hour
    # (common x1 form) and calculates position in list
    for x in range(pos, 0, -1):
        if type(lst[x]) == str:
            if lst[x][0:2] == "((":
                return int(lst[x].lstrip('(('))-1


def DayHour4(lst, pos):
    # Function that handle given day-hour
    # (x4 form) and calculates position in list
    for x in range(pos, 0, -1):
        if type(lst[x]) == str:
            if lst[x][0:2] == "((":
                day = int(lst[x].lstrip('(('))
                hour = lst[x+1]
                return int((day*4)+int(hour/6))-4


def DayHour24(lst, pos):
    # Function that handle given day-hour
    # (x24 form) and calculates position in list
    for x in range(pos, 0, -1):
        if type(lst[x]) == str:
            if lst[x][0:2] == "((":
                day = int(lst[x].lstrip('(('))
                return int((day-1)*24)            


def CalcDH(pos):
    # Inverse function of DayHour4
    # Calculate day and hour with given position in list
    for D in range(1, 32, 1):
        for H in range(0, 19, 6):
            if int((D*4) + int(H/6))-4 == pos:
                return D, H


def DataToLists(lst, pos, *Lists):
    # Function that write data to given list in Lists
    if BlockIdx(lst[pos]) < 7:
        # Executing function to find right place in list for data
        n = DayHour4(lst, pos)
    else:
        n = DayHour(lst, pos)
    # Counter
    k = 1
    # Writing data to proper place in each list
    for List in Lists:
        if IsData(lst[pos+k]) is False:
            break
        List[n] = lst[pos+k]
        k += 1


def IsData(val):
    # check value for markers of next block of code
    if type(val) == str:
        if val[0] == '=' or val[0:2] == '((':
            return False
        if val[-1] == 'Щ' or val[-1] == 'щ':
            return False
    return True 


def BlockIdx(x):
    # Function that convert block indices to integer
    #  because it could be =01 or = 1 or =1'''
    if len(x) > 0 and x[0] == '=':
        index = int(x.lstrip('='))
        return index


def ObjectNumCheck(lst, pos):
    # Find number of the object for given data
    for x in range(pos, 0, -1):
        if type(lst[x]) == str:
            if lst[x][0:2] == "((" and lst[x+1] == 21:
                return lst[x+2]


def wrt(file_name, lstData, path):
    os.chdir(path)
    Fl = open(file_name, 'a')
    Fl.write('\n')
    for Data in lstData:
        Fl.write(str(Data) + ',')