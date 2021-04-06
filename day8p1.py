with open(r'input8.txt') as file:
    instructions = [i.split() for i in file]
    acc = 0
    
    lst = []

    curse = 0

    while curse < len(instructions):
        if instructions[curse][0] == 'acc' and curse not in lst:
            lst.append(curse)
            acc += int(instructions[curse][1])
            curse += 1

        elif curse in lst: 
            break

        elif instructions[curse][0] == 'jmp':
            curse += int(instructions[curse][1])

        elif instructions[curse][0] == 'nop':
            curse += 1

    print(acc)