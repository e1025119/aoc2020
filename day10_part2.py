from aocd import get_data

data = [0]+[int(x) for x in get_data(day=10, year=2020).split('\n')]
data.sort()
ways = [[j for j in range(i+1,i+4) if data[j] - x <= 3] for i,x in enumerate(data[:-3])]
ways.append([j for j in range(len(data)-2,len(data)) if data[j] - data[-3] <= 3])
ways.append([len(data)-1])
ways.append(1)

def main():
    print(ways_sum(0))

def ways_sum(idx):
    if isinstance(ways[idx], int):
        return ways[idx]
    else:
        print(ways[idx])
        cnt = 0
        for x in ways[idx]:
            cnt += ways_sum(x)
        ways[idx] = cnt
        return cnt    

if __name__ == "__main__":
    main()
