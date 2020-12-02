inFile = open("in_2.txt","r")
lines = inFile.readlines()

count = 0
for line in lines:
    sp1 = line.split(":",1)     # sp1[1] = password string
    sp2 = sp1[0].split("-",1)   # sp2[0] = lower char position
    sp3 = sp2[1].split(" ",1)   # sp3[0] = higher char position, sp3[1] = char
    b1 = (sp1[1][int(sp2[0])] == sp3[1])
    b2 = (sp1[1][int(sp3[0])] == sp3[1])
    if b1 != b2:
        count += 1

print(count)
