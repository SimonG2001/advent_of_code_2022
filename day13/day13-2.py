import json

def comparePair(left, right):
    #print("left", left, "right", right)
    if right == [] and left == []:
        return 1
    elif left == []:
        return 2
    elif right == []:
        return 0
    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 2
        elif left == right:
            return 1
        else:
            return 0

    elif isinstance(left, int) and isinstance(right, list):
        return comparePair([left], right)        
        

    elif isinstance(left, list) and isinstance(right, int):
        return comparePair(left, [right])

    elif isinstance(left, list) and isinstance(right, list):
        for i in range(len(right)):
            
            if i <= len(left) - 1:
                answer = comparePair(left[i], right[i])
                if answer == 1:
                    pass
                else:
                    return answer   
            else:
                return 2
        if len(left) > len(right):
            return 0 
        return 1 
    
    else:
        print("hur fan??")

def main():
    score = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        
        all = []
        
        for line in lines:
            
            line = line.split("\n")[0]
            if line == "":
                pass
            else:
                line = json.loads(line)
                
                if all  == []:
                    all.append(line)
                else:
                    insertAt = len(all) - 1
                    for i, elem in enumerate(all):
                        if comparePair(line, elem) == 2:
                            insertAt = i
                            break
                    all.insert(insertAt, line)

        m = all.pop(-1)
        insertAt = len(all) - 1
        for i, elem in enumerate(all):
            if comparePair(m, elem) == 2:
                insertAt = i
                break

        all.insert(insertAt, m)

        div1 = [[2]]
        div2 = [[6]]
        div1i, div2i = 0, 0

        for i, elem in enumerate(all):
            if comparePair(div1, elem) == 2:
                insertAt = i
                break
        div1i = insertAt + 1
        all.insert(insertAt, div1)

        for i, elem in enumerate(all):
            if comparePair(div2, elem) == 2:
                insertAt = i
                break
        div2i = insertAt + 1
        all.insert(insertAt, div2)

        #print(all)
        print(div1i * div2i)
                    
                    
        #print(pair_number)


if __name__ == "__main__":
    main()           