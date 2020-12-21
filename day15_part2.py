from aocd import get_data

data = [[int(x),(0,i+1)] for i,x in enumerate(get_data(day=15, year=2020).split(','))]
prev = data[-1][0]
init_len = len(data)
data = dict(data)

for idx in range(init_len+1,30000001):
    if data.get(prev)[0] == 0:
        data.update({0: (data.get(0)[1], idx)})
        prev = 0
    else:
        pt = data.get(prev)
        dist = pt[1] - pt[0]
        fst = data.get(dist, (0,0))[1]
        data.update({dist: (fst, idx)})
        prev = dist
print(prev)
