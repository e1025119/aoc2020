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
inter_set, word_set = set(), set()
union = True
for grp in grps:
    for word in grp:
        for ch in word:
            word_set.add(ch)
        if union:
            inter_set = word_set
            union = False
        else:    
            inter_set.intersection_update(word_set)
        word_set = set()    
    union = True
    cnt += len(inter_set)
    inter_set = set()
print(cnt)
