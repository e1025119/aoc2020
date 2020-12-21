from aocd import get_data

data = get_data(day=14, year=2020).split('\n')
mem = {}
mask = ""

for line in data:
    lsplit = [x.strip() for x in line.split('=')]
    if lsplit[0] == "mask":
        mask = lsplit[1]
    else:
        key = [list(bin(int((lsplit[0].replace('[',']').split(']'))[1]))[2:].zfill(36))]
        value = int(lsplit[1])
        for i in range(0,len(mask)):
            if mask[i] == '1':
                for k in key:
                    k[i] = '1'
            elif mask[i] == 'X':
                tmp = []
                for k in key:
                    k0, k1 = k.copy(), k.copy()
                    k0[i] = '0'
                    k1[i] = '1'
                    tmp.append(k0)
                    tmp.append(k1)
                key = tmp
        for k in key:    
            k = "".join(k)
            mem.update({int(k, 2): value})
print(sum(mem.values()))
