with open(r'C:\Users\DELL\Downloads\best_python\input.txt.txt', 'r') as f:
    lst=[int(i.rstrip('\n')) for i in f]
    l=len(lst)
    for i in range(l):
        for j in range(i, l):
            for k in range(j, l):
                if lst[i]+lst[j]+lst[k]==2020:
                    print(lst[i]*lst[j]*lst[k])
