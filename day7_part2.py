from aocd import get_data
import string

data = get_data(day=7, year=2020)
data = [{z[0] : z[1:]} for z in [[' '.join(y[0].strip().split(' ')[0:2])]+[(v[0],' '.join(v[1].split(' ')[0:2])) for v in [w.strip(". ").split(' ',1) for w in y[1].split(',')] if not v[0] == "no"] 
    for y in [x.split("contain") for x in data.split('\n')]]]

def main():
    nodes, new_nodes, leaves = [("1", "shiny gold")], [], 0
    while nodes != []:
        for node in nodes:
            tmp = get_values(node[1])
            if tmp != []:
                for t in tmp:
                    cnt = int(t[0])*int(node[0])
                    new_nodes.append((str(cnt),t[1]))
            leaves += int(node[0])
        nodes = new_nodes
        new_nodes = []
    print(leaves-1)


def get_values(bag_color):
    return [list(elem.values())[0] for elem in data if (bag_color == (list(elem.keys())[0]))][0]

if __name__ == "__main__":
    main()
