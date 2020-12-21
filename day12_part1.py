from aocd import get_data

data = get_data(day=12, year=2020).split('\n')
dist = [0,0]    # (east/west axis, north/south axis)
facing = 1      # facing: N: 0, E: 1, S: 2, W: 3 -> e.g. E, R90 => (1 + (90 / 90) % 4 = 2

def main():
    for comm in data:
        update(comm)
    print(abs(dist[0])+abs(dist[1]),dist)

def update(command):
    global facing
    c = command[0]
    tail = command[1:]

    if c == 'N':
        dist[1] += int(tail)
    elif c == 'S':
        dist[1] -= int(tail) 
    elif c == 'E':
        dist[0] += int(tail) 
    elif c == 'W':
        dist[0] -= int(tail) 
    elif c == 'L':
        facing = (facing - (int(tail)/90)) % 4
    elif c == 'R':
        facing = (facing + (int(tail)/90)) % 4
    elif c == 'F':
        if facing == 0:
            dist[1] += int(tail) 
        elif facing == 2:
            dist[1] -= int(tail) 
        elif facing == 1:
            dist[0] += int(tail) 
        elif facing == 3:
            dist[0] -= int(tail) 

if __name__ == "__main__":
    main()
