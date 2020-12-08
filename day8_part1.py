from aocd import get_data

cnt, acc  = 0, 0
data = [(y[0], y[1]) for y in [x.split() for x in get_data(day=8, year=2020).split('\n')]]

def main():
    visited = set()
    while not cnt in visited:
        visited.add(cnt)
        execute()
    print(acc)     
        

def execute():
    global cnt, acc
    pair = data[cnt]
    instr, val = pair[0], pair[1]
    if instr == "acc":
        acc += int(val)
        cnt += 1
    elif instr == "jmp":
        cnt += int(val)
    else:
        cnt += 1

if __name__ == "__main__":
    main()
