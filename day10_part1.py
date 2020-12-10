from aocd import get_data

data = [0]+[int(x) for x in get_data(day=10, year=2020).split('\n')]
data.sort()
cnt1, cnt2, cnt3 = 0, 0, 1
for idx, val in enumerate(data[0:-1]):
    if data[idx+1] - val == 1:
        cnt1 += 1
    elif data[idx+1] - val == 2:
        cnt2 += 1
    elif data[idx+1] - val == 3:
        cnt3 += 1
    else:
        print("error")
print(cnt1, cnt2, cnt3, cnt1*cnt3)

