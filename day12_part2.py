from aocd import get_data
import numpy as np

data = get_data(day=12, year=2020).split('\n')
dist = [0,0]    # (east/west axis, north/south axis)
waypoint = [10,1]

def main():
    for comm in data:
        update(comm)
    print(abs(dist[0])+abs(dist[1]),dist)

def update(command):
    global waypoint
    c = command[0]
    tail = int(command[1:])
    if c == 'N':
        waypoint[1] += tail
    elif c == 'S':
        waypoint[1] -= tail
    elif c == 'E':
        waypoint[0] += tail
    elif c == 'W':
        waypoint[0] -= tail
    elif c == 'R':
        waypoint = rotate(waypoint,dist,360-tail)
    elif c == 'L':
        waypoint = rotate(waypoint,dist,tail)  
    elif c == 'F':
        for i in range(0,tail):
            dist[0] += waypoint[0]
            dist[1] += waypoint[1]

def rotate(point, origin, degrees):
    rad = np.deg2rad(degrees)
    x,y = point[0],point[1]
    x1 = x*np.cos(rad)-y*np.sin(rad)
    y1 = x*np.sin(rad)+y*np.cos(rad)
    return [int(np.round_(x1)),int(np.round_(y1))]

if __name__ == "__main__":
    main()
