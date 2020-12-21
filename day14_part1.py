from aocd import get_data

data = get_data(day=14, year=2020).split('\n')
mem = {}
mask = ""

for line in data:
    lsplit = [x.strip() for x in line.split('=')]
    if lsplit[0] == "mask":
        mask = lsplit[1]
    else:
        key = int((lsplit[0].replace('[',']').split(']'))[1])
        value = list(bin(int(lsplit[1]))[2:].zfill(36))
        for i in range(0,len(mask)):
            if mask[i] == '1':
                value[i] = '1'
            elif mask[i] == '0':
                value[i] = '0'
        value = "".join(value)
        mem.update({key: int(value,2)})
print(sum(mem.values()))
