import json

def comparePair(left, right):
    print("left", left, "right", right)
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
        pair_number = 1
        left = ""
        right = ""
        all = []
        mode = 2
        for line in lines:
            
            line = line.split("\n")[0]
            if line == "":
                pair_number += 1
                left = ""
                right = ""
                mode += 1
            else:
                line = json.loads(line)
                
                if mode == 2:
                    left = line
                    mode += 1
                else:
                    right = line
                    #print("Pair", pair_number, left, right)
                    '''if pair_number == 4:
                        if comparePair(left, right) == 2:
                            
                            print("Pair", pair_number,"left:", left,"right", right)
                            score += pair_number
                    '''
                    if comparePair(left, right) == 2:
                        
                        print("Pair", pair_number,"left:", left,"right", right)
                        score += pair_number
                    
                    mode = 1
        print(score)
        #print(pair_number)


if __name__ == "__main__":
    main()           