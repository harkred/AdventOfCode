with open(r"AdventOfCode\input3.txt") as f:
    mapo = [i.rstrip('\n') for i in f.readlines()]

    cursor1 = 0
    cursor2 = 0
    cursor3 = 0
    cursor4 = 0
    cursor5 = 0
    
    tree_count1 = 0
    tree_count2 = 0
    tree_count3 = 0
    tree_count4 = 0
    tree_count5 = 0

    for path1 in mapo:
        if path1[cursor1] == '#':
            tree_count1 += 1
        else:
            pass
        cursor1 += 1
        if cursor1 >= 31:
            cursor1 -= 31

    for path2 in mapo:
        if path2[cursor2] == '#':
            tree_count2 += 1
        else:
            pass
        cursor2 += 3
        if cursor2 >= 31:
            cursor2 -= 31

    for path3 in mapo:
        if path3[cursor3] == '#':
            tree_count3 += 1
        else:
            pass
        cursor3 += 5
        if cursor3 >= 31:
            cursor3 -= 31

    for path4 in mapo:
        if path4[cursor4] == '#':
            tree_count4 += 1
        else:
            pass
        cursor4 += 7
        if cursor4 >= 31:
            cursor4 -= 31

    for path5 in mapo:
        if mapo.index(path5) % 2 == 0:
            if path5[cursor5] == '#':
                tree_count5 += 1
            else:
                pass
            cursor5 += 1
            if cursor5 >= 31:
                cursor5 -= 31
    
    print(tree_count1 * tree_count2 * tree_count3 * tree_count4 * tree_count5)
