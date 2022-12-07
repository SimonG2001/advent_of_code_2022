

score = ""
with open('input.txt', 'r') as f:
    lines = f.readlines()
    i = 1
    b = {}
    
    for j in range(9):
        b[j+1] = []
    for line in lines:
            if i < 9:
                for j in range(9):
                    if line[j*4+1] != " ":
                        b[j+1].append(line[j*4+1])
                        
            elif i > 10:
                spl = line.split()
                count = int(spl[1])
                size = count
                fromS = int(spl[3])
                toS = int(spl[5])
                for j in range(count):
                    b[toS].insert(0, b[fromS].pop(size-1-j))
            i += 1
    
    for j in range(9):
        score += b[j+1][0]

print(score) 