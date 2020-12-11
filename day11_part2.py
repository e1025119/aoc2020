from aocd import get_data

data = [list(x) for x in get_data(day=11, year=2020).split('\n')]
dRows, dCols = len(data)-1, len(data[0])-1
FREE, OCC = 'L', '#'

def main():
    changed = True
    while changed:
        locL, locP = [], []
        for row, i in enumerate(data):
            for col, j in enumerate(i):
                if j == FREE and check_L(row, col):
                    locL.append((row,col))
                elif j == OCC and check_P(row, col):
                   locP.append((row,col))
        if locL == [] and locP == []:
            changed = False
        else:
            change_L(locL)
            change_P(locP)
    print(len([j for x in data for j in x if j == OCC]))

def check_L(row, col):
    if len([x for x in get_nbs(row, col) if data[x[0]][x[1]] == OCC]) == 0:
        return True
    else:
        return False

def check_P(row, col):
    if len([x for x in get_nbs(row, col) if data[x[0]][x[1]] == OCC]) >= 5:
        return True
    else:
        return False

def change_L(lst):
    global data
    for l in lst:
        data[l[0]][l[1]] = OCC

def change_P(lst):
    global data
    for p in lst:
        data[p[0]][p[1]] = FREE

#get all first visible grid elements
def get_nbs(row, col):
    return [x for x in [get_tl(row, col), get_tm(row, col), get_tr(row, col), get_ml(row, col), get_mr(row, col), get_bl(row, col), get_bm(row, col), get_br(row, col)] if x != None]

def get_tl(row,col):
    found = False
    while (row > 0 and col > 0) and not found:
        row -= 1
        col -= 1
        tmp = data[row][col]
        if tmp == 'L' or tmp == '#':
            return (row,col)

def get_tm(row,col):
    found = False
    while (row > 0) and not found:
        row -= 1
        tmp = data[row][col]
        if tmp == 'L' or tmp == '#':
            return (row,col)

def get_tr(row,col):
    found = False
    while (row > 0 and col < dCols) and not found:
        row -= 1
        col += 1
        tmp = data[row][col]
        if tmp == 'L' or tmp == '#':
            return (row,col)

def get_ml(row,col):
    found = False
    while (col > 0) and not found:
        col -= 1
        tmp = data[row][col]
        if tmp == 'L' or tmp == '#':
            return (row,col)

def get_mr(row,col):
    found = False
    while (col < dCols) and not found:
        col += 1
        tmp = data[row][col]
        if tmp == 'L' or tmp == '#':
            return (row,col)

def get_bl(row,col):
    found = False
    while (row < dRows and col > 0) and not found:
        row += 1
        col -= 1
        tmp = data[row][col]
        if tmp == 'L' or tmp == '#':
            return (row,col)

def get_bm(row,col):
    found = False
    while (row < dRows) and not found:
        row += 1
        tmp = data[row][col]
        if tmp == 'L' or tmp == '#':
            return (row,col)

def get_br(row,col):
    found = False
    while (row < dRows and col < dCols) and not found:
        row += 1
        col += 1
        tmp = data[row][col]
        if tmp == 'L' or tmp == '#':
            return (row,col)



if __name__ == "__main__":
    main()
