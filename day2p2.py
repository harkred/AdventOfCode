with open(r"C:\Users\DELL\Downloads\best_python\input2.txt") as f:
    lst=[i.rstrip('\n') for i in f]
    correct=0
    for patt in lst:
        if patt[3].isspace():
            p1=int(patt[0])
            p2=int(patt[2])
            chk=patt[4]
            wrd=patt[7:]
            x=1 if wrd[p1-1]==chk or wrd[p2-1]==chk else 0
            y=1 if wrd[p1-1]==chk and wrd[p2-1]==chk else 0
            if x==1 and y==0:
                correct+=1
            else:
                pass
            #print(p1, p2, chk, wrd, x, sep='\t')
            
         
        elif patt[4].isspace():
            p1=int(patt[0])
            p2=int(patt[2:4])
            chk=patt[5]
            wrd=patt[8:]
            x=1 if wrd[p1-1]==chk or wrd[p2-1]==chk else 0
            y=1 if wrd[p1-1]==chk and wrd[p2-1]==chk else 0
            if x==1 and y==0:
                correct+=1
            else:
                pass
            #print(p1, p2, chk, wrd, x, sep='\t')
        
        elif patt[5].isspace():
            p1=int(patt[0:2])
            p2=int(patt[3:5])
            chk=patt[6]
            wrd=patt[9:]
            x=1 if wrd[p1-1]==chk or wrd[p2-1]==chk else 0
            y=1 if wrd[p1-1]==chk and wrd[p2-1]==chk else 0
            if x==1 and y==0:
                correct+=1
            else:
                pass
            #print(p1, p2, chk, wrd, x, sep='\t')
    print(correct)
        
        
    
