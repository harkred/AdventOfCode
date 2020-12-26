'''
1. byr (Birth Year) - four digits; at least 1920 and at most 2002.
2. iyr (Issue Year) - four digits; at least 2010 and at most 2020.
3. eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
4. hgt (Height) - a number followed by either cm or in:
   If cm, the number must be at least 150 and at most 193.
   If in, the number must be at least 59 and at most 76.
5. hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
6. ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
7. pid (Passport ID) - a nine-digit number, including leading zeroes.
8. cid (Country ID) - ignored, missing or not.
'''
def checker(wrd):
    a='ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in list(a):
        if i in wrd:
            return 0
            break
    else:
        return 1

with open('input4.txt', 'r') as f:
    correct=0
    lst=[]
    tlst=[]
    for i in f.readlines():
        if i!='\n': tlst.append(i.rstrip('\n'))
        elif i=='\n':
            lst.append(tlst)
            tlst=[]
        else: continue
    
    nlst=[]
    ulst=[]
    for data in lst:
        for word in data:
            nlst.extend(word.split())
        ulst.append(nlst)
        nlst=[]

    #Updated
    cou=[]
    for data in ulst:
        for i in data:
        
            if 'byr' in i:
                if int(i[4:])>=1920 and int(i[4:])<=2002: cou.append('byr')
                    
            elif 'iyr' in i:
                if int(i[4:])>=2010 and int(i[4:])<=2020: cou.append('iyr')
                    
            elif 'eyr' in i:
                if int(i[4:])>=2020 and int(i[4:])<=2030: cou.append('eyr')
                    
            elif 'hgt' in i:
                if 'cm' in i:
                    if int(i[4:].rstrip('cm'))>=150 and int(i[4:].rstrip('cm'))<=193: cou.append('hgt')
                        
                elif 'in'==i[len(i)-3:len(i)]:
                    if int(i[4:].rstrip('in'))>=59 and int(i[4:].rstrip('in'))<=76: cou.append('hgt')
                        
            elif 'hcl' in i:
                if '#' in i[4:]:
                    if len(i[4:].lstrip('#'))==6 and checker(i[4:].lstrip('#'))==1: cou.append('hcl')
            
            elif 'ecl' in i:
                if i[4:]=='amb' or i[4:]=='blu' or i[4:]=='brn' or i[4:]=='gry' or i[4:]=='grn' or i[4:]=='hzl' or i[4:]=='oth': cou.append('ecl')
                    
            elif 'pid' in i:
                if len(i[4:])==9: cou.append('pid')

        if len(cou)==7: correct+=1
        else: pass
        cou=[]
    print(correct)
                
        
    