from aocd import get_data
from itertools import product

data = [int(x) for x in get_data(day = 9, year = 2020).split('\n')]
offset = 25

def main():
    curr = 25
    while sum_two_in_n(data[curr], curr-25, curr):
        curr += 1
    print(data[curr])

# for a number n, checks if it is 
# a sum of any 2 of the numbers in range [i1,i2]
def sum_two_in_n(n, i1, i2):
    sums = [x+y for (x,y) in product(data[i1:i2],data[i1:i2])]
    return True if n in sums else False 

if __name__ == "__main__":
    main()
