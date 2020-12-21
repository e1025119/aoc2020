from aocd import get_data
import itertools

data = [list(y) for x, y in itertools.groupby(get_data(day=16, year=2020).split('\n'), lambda x: x == '') if not x]
rules = [[tuple([int(y) for y in x[0].split('-')]), tuple([int(y) for y in x[1].split('-')])] for x in [r.split(':')[1].strip().split(' or ') for r in data[0]]]
nearby = [[int(z) for z in y] for y in [x.split(',') for x in data[2][1:]]]

def main():
    nums = []
    for ticket in nearby:
        nums += check_ticket(ticket)
    print("nums:", sum(nums))

def check_ticket(ticket):
    return [n for n in ticket if n not in [num for num in ticket for rule in rules if (rule[0][0] <= num <= rule[0][1] or rule[1][0] <= num <= rule[1][1])]]

if __name__ == "__main__":
    main()
