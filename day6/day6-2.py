
def find():
    score = 0
    with open('input.txt', 'r') as f:
        line = f.readline()
        buff = []
        for i in range(len(line)):
            if i < 14:
                buff.append(line[i])
            else:
                buff.pop(0)
                buff.append(line[i])
                for j in range(14):
                    test = buff.pop(j)
                    if buff.count(test) > 0:
                        buff.insert(j, test)
                        break
                    elif j == 13:
                        return i+1
                    else:
                        buff.insert(j, test)
                
            



print(find()) 