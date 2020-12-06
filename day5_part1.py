f = open("day5_in.txt")
lines = f.readlines()
ls = [sid for sid in lines]
highest = 0
for line in lines:
	row = int(line[0:7].replace("F","0").replace("B","1"), 2)
	seat = int(line[7:10].replace("L","0").replace("R","1"), 2)
	sid = (row*8)+seat
	if sid > highest:
		highest = sid
print(highest)		
