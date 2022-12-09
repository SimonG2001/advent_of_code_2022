
def isAdjacent(hx, hy, tx, ty):
    return abs(hx - tx) <= 1 and abs(hy - ty) <= 1


score = 1   
with open('input.txt', 'r') as f:
    hx = 0
    hy = 0
    tx = 0
    ty = 0
    visited = []
    visited.append("0 0")
    headV = []
    headV.append("0 0")
    lines = f.readlines()

    for line in lines:
        lin = line.split()
        for i in range(int(lin[1])):
            #print("head: " + str(hx) + " " + str(hy) + " tail: " + str(tx) + " " + str(ty))
            if lin[0] == "U":
                hy += 1
            elif lin[0] == "R":
                hx += 1
            elif lin[0] == "D":
                hy -= 1
            elif lin[0] == "L":
                hx -= 1
            hStr = str(hx) + " " + str(hy)
            if headV.count(hStr) == 0:
                headV.append(hStr)
            
            if not isAdjacent(hx, hy, tx, ty):
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
                tailStr = str(tx) + " " + str(ty)
                if visited.count(tailStr) == 0:
                    visited.append(tailStr)
                    score += 1
            else:
                pass
                #print("head: " + str(hx) + " " + str(hy) + " tail: " + str(tx) + " " + str(ty))

#print(headV)
#print(visited)

print(score)