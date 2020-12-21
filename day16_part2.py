from aocd import get_data
from itertools import groupby
from math import prod

data = [list(y) for x, y in groupby(get_data(day=16, year=2020).split('\n'), lambda x: x == '') if not x]
rules = [(x[0],[tuple([int(y) for y in x[1][0].split('-')]), tuple([int(y) for y in x[1][1].split('-')])]) for x in [(u[0], u[1].strip().split(' or ')) for u in [r.split(':') for r in data[0]]]]
my_ticket = [int(x) for x in data[1][1].split(',')]
nearby = [[int(z) for z in y] for y in [x.split(',') for x in data[2][1:]]]

def main():
    global nearby, rules
    places = list(range(0, len(nearby[0])))
    dic = {}
    nearby = [x for x in nearby if check_ticket(x) == []]
    while rules != []:
        for rule in rules:
            valid = True
            pot = []
            for place in places:
                for ticket in nearby:
                    if not (rule[1][0][0] <= ticket[place] <= rule[1][0][1] or rule[1][1][0] <= ticket[place] <= rule[1][1][1]):
                        valid = False
                        break;
                if valid:
                    pot.append(place)
                else:
                    valid = True
            if len(pot) == 1:
                rules = [x for x in rules if x != rule]
                dic.update({rule[0]: pot[0]})
                places = [x for x in places if x != pot[0]]
    rows = [dic.get(x) for x in dic.keys() if "departure" in x]
    res = prod([my_ticket[x] for x in rows])
    print(res)

def check_ticket(ticket):
    return [n for n in ticket if n not in [num for num in ticket for rule in rules if (rule[1][0][0] <= num <= rule[1][0][1] or rule[1][1][0] <= num <= rule[1][1][1])]]

if __name__ == "__main__":
    main()
