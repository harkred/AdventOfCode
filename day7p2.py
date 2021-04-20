with open(r'input7.txt', 'r') as f:
    rules = [i.rstrip('\n') for i in f.readlines()]
    rules = [(i[0:i.index('bags')], i[(i.index('contain')+8):]) for i in rules]
    rules = [[i[0], i[1].split(',')] for i in rules]
    count = 0
    bags = ['shiny gold']
    
    for need in bags:
        for bag in rules:
            if str(need).strip() in str(bag[0]).strip():
                for items in bag[1]:
                    for no in items:
                        if no.isdigit(): 
                            extension = [items[2:].rstrip('bags.')] * int(items[:2])
                            bags.extend(extension)
    print(len(bags) - 1)