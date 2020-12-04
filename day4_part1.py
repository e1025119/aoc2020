fin = open("day4_in.txt", "r")
pp_norm = {"byr": 1989, "iyr": 2010, "eyr": 2020, "hgt": 175, "hcl": "bld", "ecl": "bl", "pid": 0, "cid": 0}

lines = fin.readlines()
pp_curr = {"cid": 0}
valid = 0
for line in lines:
    if line == "\n":
        if pp_curr.keys() == pp_norm.keys():
            valid += 1
        pp_curr = {"cid": 0}
    else:
        for field in line.split():
            tmp = field.split(":", 1)
            pp_curr.update({tmp[0]: tmp[1]})
print("valid passports: "+str(valid))            
