with open(r'input9.txt', 'r') as file:
    num = [int(i.rstrip('\n')) for i in file]
    l = len(num)
    done = 0
    
    def preamble(i, num, done):
        for j in range(i-25, i):
            for k in range(j+1, i):
                if num[j] + num[k] == num[i]:
                    done = 1
                    break
            if done:
                done = 0
                break
        else: 
            return num[i]


    for i in range(25, l):
        answer = preamble(i, num, done)
        
        if answer:
             break
    
    print(answer)