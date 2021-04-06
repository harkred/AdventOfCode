with open(r'input6.txt', 'r') as f:
    ans = 0
    tlst = []
    alst = []
    lst = [i.rstrip('\n') for i in f.readlines()]
    for i in lst:
        tlst.append(i)
        if i == '' or lst.index(i) == len(lst)-1:
            if lst.index(i) != len(lst)-1: tlst.pop(-1)
            a = ('').join(tlst)
            alst = list(a)
            b = set(alst)
            ans += len(b)
            tlst = []
    
    print(ans)