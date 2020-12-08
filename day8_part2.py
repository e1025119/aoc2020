from aocd import get_data

cnt, acc, swap  = 0, 0, 0
data = [(y[0], y[1]) for y in [x.split() for x in get_data(day=8, year=2020).split('\n')]]

def main():
    global cnt, acc, swap
    term = False
   
    while not term:
        visited = set()
        cnt, acc = 0, 0
        while (not cnt in visited):
            if cnt == len(data):
                term = True
                break
            else:
                visited.add(cnt)
                execute()
        swap += 1
    print(acc)     
        

def execute():
    global cnt, acc
    pair = data[cnt]
    instr, val = pair[0], pair[1]
    
    if instr == "acc":
        acc += int(val)
        cnt += 1
    elif (instr == "jmp" and not cnt == swap) or (instr == "nop" and cnt == swap):
        cnt += int(val)
    elif (instr == "nop" and not cnt == swap) or (instr == "jmp" and cnt == swap):
        cnt += 1  

if __name__ == "__main__":
    main()
