from aocd import get_data
import string

data = get_data(day=7, year=2020)
data = [{z[0] : z[1:]} for z in [[' '.join(y[0].strip().split(' ')[0:2])]+[' '.join(v[1].split(' ')[0:2]) for v in [w.strip(". ").split(' ',1) for w in y[1].split(',')]] for y in [x.split("contain") for x in data.split('\n')]]]

def main():
    nodes, new_nodes, leaves = set(), set(), set()
    nodes.add("shiny gold")
    while nodes != set():
        for node in nodes:
            tmp = get_keys(node)
            if tmp != []:
                new_nodes = new_nodes.union(tmp)
                leaves = leaves.union(tmp)
            else:
                leaves.add(node)
        nodes = new_nodes
        new_nodes = set()
    print(len(leaves))


def get_keys(bag_color):
    return [list(elem.keys())[0] for elem in data if (bag_color in (list(elem.values())[0]))]

if __name__ == "__main__":
    main()
