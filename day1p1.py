with open(r'AdventOfCode\input.txt', 'r') as f:
    lst = [int(i.rstrip('\n')) for i in f.readlines()]
    l = len(lst)
    for i in range(l):
       for j in range(i, l):
           if lst[i] + lst[j] == 2020:
               print(lst[i] * lst[j])