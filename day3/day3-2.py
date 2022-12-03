
score = 0

def makeList(str):
    list = []
    for i in range(len(str)):
        if i == len(line)-1:
            break
        list.append(str[i])
    return list

with open('input.txt', 'r') as f:
    lines = f.readlines()
    j = 0
    ruck1 = []
    ruck2 = []
    ruck3 = []
    for line in lines:
        if j == 0:
            ruck1 = makeList(line)
            j = 1
        elif j == 1:
            ruck2 = makeList(line)
            j = 2
        else:
            j = 0
            ruck3 = makeList(line)
            for elem in ruck1:
                if ruck2.count(elem) > 0 and ruck3.count(elem) > 0:
                    if elem.isupper():
                        score += ord(elem) - 38
                    else:
                        score += ord(elem) - 96
                    break

print(score) 