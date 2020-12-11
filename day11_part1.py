from aocd import get_data

data = [list(x) for x in get_data(day=11, year=2020).split('\n')]
dRows, dCols = len(data), len(data[0])
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
    if len([x for x in get_nbs(row, col) if data[x[0]][x[1]] == OCC]) >= 4:
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

#get all adjacent grid elements
def get_nbs(row, col):
    return [n for n in [(row-1,col-1),(row-1,col),(row-1,col+1),(row,col-1),(row,col+1),(row+1,col-1),(row+1,col),(row+1,col+1)] if n[0] >= 0 and n[0] < dRows and n[1] >= 0 and n[1] < dCols]

if __name__ == "__main__":
    main()
