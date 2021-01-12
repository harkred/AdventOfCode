with open('input7.txt', 'r') as f:
    NEED = 'shiny gold'
    rules = [i.rstrip('\n') for i in f.readlines()]
    rules = [(i[0:i.index('bags')], i[(i.index('contain')+8):]) for i in rules]
    bags = []
    for i in rules:
        if NEED in i[1]: 
            count += 1
            bags.append(i[0])
        else: continue
        
    for i in bags:
        for j in rules:
            if i in j[1]:
                bags.append(j[0])
            else: continue

    count = len(set(bags))
    print(count)