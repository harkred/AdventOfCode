#Part1
with open(r'AdventOfCode\input5.txt', 'r') as f:
    lst = [i.rstrip('\n') for i in f.readlines()]
    
    row = [i for i in range(128)]
    column = [i for i in range(8)]
    
    lrow = len(row)
    lcol = len(column)
    
    ans  =[]
    for data in lst:
        for deco in list(data):
            if deco == 'F':
                lrow //= 2
                row = row[:lrow]
                
            elif deco == 'B':
                lrow //= 2
                row = row[lrow:]
                
            elif deco == 'L':
                lcol //= 2
                column = column[:lcol]
                
            elif deco == 'R':
                lcol //=2
                column = column[lcol:]
        
        ans.append((row[0] * 8) + column[0])
        
        row = [i for i in range(128)]
        column = [i for i in range(8)]
    
        lrow = len(row)
        lcol = len(column)
        
    print(max(ans))
    
    
    #Part2
    for i in ans:
        if i+1 not in ans and i+2 in ans:
            print(i + 1)
   