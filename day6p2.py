with open('input6.txt', 'r') as f:
    lst = [i.rstrip('\n') for i in f.readlines()]
    lst.append('')
    correct = 0
    tlst = []
    print(lst)
    for i in lst:
        tlst.append(i)
        
        if i == '':
            tlst.pop()
            
            if len(tlst) == 1:
                correct += len(tlst[0])
                tlst = []
            
            else:
                nlst = []
                for i in tlst:
                    nlst.extend(list(i))
                
                mlst=set(nlst)
                    
                for j in mlst:
                    if nlst.count(j) == len(tlst): correct += 1

                tlst = []                 
    print(correct)