f = open("day5_in.txt")
lines = f.readlines()
mylist = sorted([int(line[0:7].replace("F","0").replace("B","1"), 2) * 8 + int(line[7:10].replace("L","0").replace("R","1"), 2) for line in lines])
print([(mylist[x], mylist[x+1]) for x in range(len(mylist)-1) if mylist[x]+1 != mylist[x+1]])
