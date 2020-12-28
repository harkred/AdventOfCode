with open('input5.txt', 'r') as f:
    lst=[i.rstrip('\n') for i in f.readlines()]
    
    row=[i for i in range(128)]
    column=[i for i in range(8)]
    
    lrow=len(row)-1
    lcol=len(column)-1
    
    ans=[]
    for data in lst:
        for deco in data:
            if data.index(deco)==len(data)-1: ans.append((row[lrow], column[lcol]))
            
            elif deco=='F':
                lrow//=2
                row=row[:lrow]
            
            elif deco=='B':
                lrow//=2
                row=row[lrow:]
                
            elif deco=='L':
                lcol//=2
                column=column[:lcol]
                print(column, lcol)
                
            elif deco=='R':
                lcol//=2
                column=column[lcol:]
                
        row=[i for i in range(128)]
        column=[i for i in range(8)]
    
        lrow=len(row)-1
        lcol=len(column)-1
        
    print(ans)