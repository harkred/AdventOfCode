with open(r'C:\Users\DELL\Downloads\best_python\input2.txt') as f:
    lst=[i.rstrip('\n') for i in f]
    correct=0
    for patt in lst:
        if patt[3].isspace():
            low=int(patt[0])
            high=int(patt[2])
            chk=patt[4]
            passwd=patt[7:]
            wrd=[i for i in passwd if i==chk]
            x=1 if len(wrd)>=low and len(wrd)<=high else 0
            if x==1:
                correct+=1
            else:
                pass

        elif patt[4].isspace():
            low=int(patt[0])
            high=int(patt[2:4])
            chk=patt[5]
            passwd=patt[8:]
            wrd=[i for i in passwd if i==chk]
            x=1 if len(wrd)>=low and len(wrd)<=high else 0
            if x==1:
                correct+=1
            else:
                pass

        elif patt[5].isspace():
            low=int(patt[0:2])
            high=int(patt[3:5])
            chk=patt[6]
            passwd=patt[9:]
            wrd=[i for i in passwd if i==chk]
            x=1 if len(wrd)>=low and len(wrd)<=high else 0
            if x==1:
                correct+=1
            else:
                pass
    print(correct)
           

            
    
