from aocd import get_data
from itertools import product

data = [int(x) for x in get_data(day = 9, year = 2020).split('\n')]
offset = 25

def main():
    curr = 25
    while sum_two_in_n(data[curr], curr-25, curr):
        curr += 1
    invalid = data[curr]            # part 1
    print(find_contiguous(invalid)) # part 2

def sum_two_in_n(n, i1, i2):
    sums = [x+y for (x,y) in product(data[i1:i2],data[i1:i2])]
    return True if n in sums else False 

def find_contiguous(invalid):
    ind1, ind2 = 0, 1
    l = []
    while ind1 < len(data):
        while ind2 <= len(data):
            tmp = sum(data[ind1:ind2])
            if tmp == invalid:
                l = data[ind1:ind2]
                break
            elif tmp < invalid:
                ind2 += 1
            else:
                ind1 += 1
                ind2 = ind1+1
        break
    return min(l)+max(l) 

if __name__ == "__main__":
    main()
