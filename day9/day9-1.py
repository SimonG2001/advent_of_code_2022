



with open('input.txt', 'r') as f:
    hx, hy, tx, ty, ohx, ohy = 0, 0, 0, 0, 0, 0
   
    visited = []
    visited.append("0 0")
    
    lines = f.readlines()

    for line in lines:
        lin = line.split()
        for i in range(int(lin[1])):
            ohx = hx
            ohy = hy
            if lin[0] == "U":
                hy += 1
            elif lin[0] == "R":
                hx += 1
            elif lin[0] == "D":
                hy -= 1
            elif lin[0] == "L":
                hx -= 1
            hStr = str(hx) + " " + str(hy)
            
            if not (abs(hx - tx) <= 1 and abs(hy - ty) <= 1):
                tx = ohx
                ty = ohy
               
                tailStr = str(tx) + " " + str(ty)
                if visited.count(tailStr) == 0:
                    visited.append(tailStr)

print(len(visited))