## problem 5

import numpy
from itertools import permutations

def makematrix(s,shape):
    l = list(s)
    m = numpy.asarray(l)
    return m.reshape(shape)

def swap_cols(arr, frm, to):
    arr[:,[frm, to]] = arr[:,[to, frm]]

def swap_rows(arr, frm, to):
    arr[[frm, to],:] = arr[[to, frm],:]

def permute_cols(arr, neworder):
    newarr = arr.copy()
    for to,frm in enumerate(neworder):
        newarr[:,to] = arr[:,frm]
    return newarr

def permute_rows(arr, neworder):
    newarr = arr.copy()
    for to,frm in enumerate(neworder):
        newarr[to,:] = arr[frm,:]
    return newarr

def check(arr):
    first = arr[:,0]
    second = arr[:,1]
    third = arr[:,2]
    fourth = arr[:,3]
    fifth = arr[:,4]

    if 'T' in first:
        if 'H' in second:
            if 'E' in third:
                if 'R' in fourth:
                    if 'E' in fifth:
                        return True
    return False

def check_first(arr):
    word = ['T', 'H', 'E', 'R', 'E']
    first = arr[0]

    i = 0

    for letter in range(5):
        if word[i] not in first:
            return False
        else:
            i += 1

    return True

def check_capital(arr):

    c_text = arr.tostring()

    capitals = ['TIRANE', 'VIENNA', 'BRUSSELS', 'SOFIA', 'NICOSIA', 'TALLINN',
                'CAYENNE', 'TBILISI', 'BERLIN', 'ATHENS', 'ROME', 'VILNIUS',
                'VALLETTA', 'MONACO', 'OSLO', 'BELFAST', 'WARSAW', 'LISBON',
                'BUCHAREST', 'MOSCOW', 'BRATISLAVA', 'BERNE', 'SANMARINO',
                'VATICANCITY']

    s = [x for x in capitals if x in c_text]

    if not s:
        return False
    else:
        return True

def check_capital_row(arr):
    if (arr[6][4] == 'B') and (arr[6][5] == 'E') and (arr[6][6] == 'R') and (arr[6][7] == 'L') and (arr[6][8] == 'I') and (arr[6][9] == 'N'):
        return True
    else:
        return False

def check_there(arr):
    if (arr[0][0] == 'T') and (arr[0][1] == 'H') and (arr[0][2] == 'E') and (arr[0][3] == 'R') and (arr[0][4] == 'E'):
        return True
    else:
        return False

def check_communism(arr):
    c = "COMMUNISM"
    f = "FUTURE"
    w = "WAVE"

    cc = arr.tostring()

    if (c in cc) and (f in cc) and (w in cc):
        return True
    else:
        return False

# str1 = capital, str2 = cipher
def contains(str1, str2):
    chrs1 = list(str1)
    x = len(chrs1)
    chrs2 = list(str2)

    i = 0

    for letter in range(x):
        if chrs1[i] not in chrs2:
            return False
        else:
            i += 1

    return True

def p_cities(q):
    poss_cities = []

    capitals = ["TIRANE", "JEREVAN", "VIENNA", "BAKU", "MINSK", "BRUSSELS", "SARAJEVO",
    "SOFIA", "ZAGREB", "NICOSIA", "PRAGUE", "COPENHAGEN", "TALLINN", "HELSINKI", "PARIS",
    "CAYENNE", "TBILISI", "BERLIN", "ATHENS", "BUDAPEST", "REYKJAVIK", "ROME", "RIGA",
    "VADUZ", "VILNIUS", "LUXEMBURG", "SKOPJE", "VALLETTA", "KISHINEV", "MONACO", "AMSTERDAM",
    "OSLO", "BELFAST", "WARSAW", "LISBON", "BUCHAREST", "MOSCOW", "EDINBURG", "BRATISLAVA", "LJUBLJANA",
    "MADRID", "STOCKHOLM", "BERNE", "DUSHANBE", "KIEV", "LONDON", "BELGRADE", "SANMARINO", "VATICANCITY"]

    for city in capitals:
        if contains(city, q) == True:
            poss_cities.append(city)

    return poss_cities

def main():
    q = 'IAUTMOCSMNIMREBOTNELSTRHEREOAEVMWIHTSEEATMAEOHWHSYCEELTTEOHMUOUFEHTRFT'
    mm = makematrix(q,[7,10])

    possible_cities = p_cities(q)

    rows = list(permutations([0,1,2,3,4,5,6]))
    possible_rows = []

    for row in rows:
        if check_first(permute_rows(mm, row)) == True:
            possible_rows.append(row)

    columns = list(permutations([0,1,2,3,4,5,6,7,8,9]))
    possible_columns = []

    for column in columns:
        if check(permute_cols(mm, column)) == True:
            possible_columns.append(column)

    double_poss_cols = []
    for pcol in possible_columns:
        if check_capital(permute_cols(mm, pcol)) == True:
            double_poss_cols.append(pcol)

    for cOrder in double_poss_cols:
        m = permute_cols(mm, cOrder)
        for rOrder in possible_rows:
            mr = permute_rows(m, rOrder)
            if ((check_there(mr) == True) and (check_capital_row(mr) == True) and (check_communism(mr) == True)):
                print(cOrder, rOrder)
                print("")
                print(mr)
                print("")

if __name__ == "__main__":
    main()
