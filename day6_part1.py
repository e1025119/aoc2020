import string

f = open("day6_in.txt", "r")
lines = [line.strip() for line in f.readlines()]
grps, grp = [], []
for line in lines:
    if line != "": grp.append(line)
    else:
        grps.append(grp)
        grp = []

cnt = 0
charset = set()
for grp in grps:
    for word in grp:
        for ch in word:
            charset.add(ch)
    cnt += len(charset)
    charset = set()
print(cnt)
