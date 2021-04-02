with open(r"AdventOfCode\input3.txt") as f:
    mapo=[i.rstrip('\n') for i in f.readlines()]
    cursor = 0
    tree_count = 0
    for path in mapo:
        if path[cursor] == '#':
            tree_count += 1
        else:
            pass
        cursor += 3
        if cursor >= 31:
            cursor -= 31
    
    print(tree_count)

