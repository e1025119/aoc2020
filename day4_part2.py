def main():
    fin = open("day4_in.txt", "r")
    pp_norm = {"byr": 1989, "iyr": 2010, "eyr": 2020, "hgt": 175, "hcl": "bld", "ecl": "bl", "pid": 0, "cid": 0}

    lines = fin.readlines()
    pp_curr = {"cid": 0}
    valid = 0
    for line in lines:
        if line == "\n":
            if validate(pp_curr, pp_norm):
                valid += 1
            pp_curr = {"cid": 0}
        else:
            for field in line.split():
                tmp = field.split(":", 1)
                pp_curr.update({tmp[0]: tmp[1]})
    print("valid passports: "+str(valid))            

def validate(pp_curr, pp_norm):
    if pp_curr.keys() != pp_norm.keys():
        return False
    str_byr = pp_curr.get("byr")
    if not str_byr.isdigit() or not len(str_byr) == 4:
        return False
    else: byr = int(str_byr)
    str_iyr = pp_curr.get("iyr")
    if not str_iyr.isdigit() or not len(str_iyr) == 4:
        return False
    else: iyr = int(str_iyr)
    str_eyr = pp_curr.get("eyr")
    if not str_eyr.isdigit() or not len(str_eyr) == 4:
        return False
    else: eyr = int(str_eyr)
    if byr < 1920 or byr > 2002:
        return False
    if iyr < 2010 or iyr > 2020:
        return False
    if eyr < 2020 or eyr > 2030:
        return False
    str_hgt = pp_curr.get("hgt")
    if not str_hgt[:-2].isdigit() or not str_hgt[-1:-3:-1] in {"mc","ni"}:
        return False
    else:
        hgt = int(str_hgt[:-2])
        hgt_unit = str_hgt[-1:-3:-1]
    if hgt_unit == "mc" and (hgt < 150 or hgt > 193):
        return False
    if hgt_unit == "ni" and (hgt < 59 or hgt > 76):
        return False
    str_hcl = pp_curr.get("hcl")
    if not str_hcl[0:1] == '#' or not len(str_hcl) == 7:
        return False
    else:
        try:
            int(str_hcl[1:], 16)
        except ValueError:
            return False
    str_ecl = pp_curr.get("ecl")
    if str_ecl not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False
    str_pid = pp_curr.get("pid")
    if not len(str_pid) == 9:
        return False
    else:
        try:
            int(str_pid, 10)
        except ValueError:
            return False
    return True    

if __name__ == "__main__":
    main()    
