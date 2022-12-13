

def moveTail(hx, hy, tx, ty):
    if not (abs(hx - tx) <= 1 and abs(hy - ty) <= 1):
        if hx == tx:
            if hy > ty:
                ty += 1
            else:
                ty -= 1
        elif hy == ty:
            if hx > tx:
                tx += 1
            else:
                tx -= 1
                
        elif hx == tx + 2 and hy == ty + 2:
            tx += 1
            ty+= 1
        elif hx == tx - 2 and hy == ty - 2:
            tx -= 1
            ty-= 1
        elif hx == tx + 2 and hy == ty - 2:
            tx += 1
            ty -= 1
        elif hx == tx - 2 and hy == ty + 2:
            tx -= 1
            ty+= 1

        else:
            if tx + 1 == hx or tx - 1 == hx:
                tx = hx
                if hy - ty > 0:
                    ty += 1
                else:
                    ty -= 1
            else:
                ty = hy
                if hx - tx > 0:
                    tx += 1
                else:
                    tx -= 1
        
    return tx, ty


with open('input.txt', 'r') as f:
    
    visited , tails= [], {}

    for i in range(10):
        tails[i] = [0, 0]
    visited.append("0 0")
    
    lines = f.readlines()

    for line in lines:
        lin = line.split()
        for i in range(int(lin[1])):
            if lin[0] == "U":
                tails[0][1] += 1
            elif lin[0] == "R":
                tails[0][0] += 1
            elif lin[0] == "D":
                tails[0][1] -= 1
            elif lin[0] == "L":
                tails[0][0] -= 1
            
            for i in range(9):
                tails[i+1][0], tails[i+1][1] = moveTail(tails[i][0], tails[i][1], tails[i+1][0], tails[i+1][1])

            tailStr = str(tails[9][0]) + " " + str(tails[9][1])
            if visited.count(tailStr) == 0:
                visited.append(tailStr)
            


print(len(visited))

