with open(r"input4.txt") as f:
    lst = [i for i in f.readlines()]
    chk_lst = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    nlst = []
    corr = 0
    for i in lst:
        nlst.append(i)
        if i == '\n':
            cou = 0
            for j in chk_lst:
                for k in nlst:
                    if j in k:
                        cou += 1
            if cou == len(chk_lst):
                corr += 1
            cou = 0
            nlst = []
    
    print(corr)