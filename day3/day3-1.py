
score = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()
    
    for line in lines:
        compA = []
        compB = []
        for i in range(len(line)):
            if (i < (len(line)-1)/2):
                compA.append(line[i])
            else:
                if i == len(line) - 1:
                    break
                compB.append(line[i])

        
        for elem in compA:
            if compB.count(elem) > 0:
                if elem.isupper():
                    score += ord(elem) - 38
                else:
                    score += ord(elem) - 96
                break
print(score) 