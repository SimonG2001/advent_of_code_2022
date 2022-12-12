
with open('input.txt', 'r') as f:
    lines = f.readlines()
    sx, sy, ex, ey, y = 0,0,0,0,0
    map = []
    
    for line in lines:
        x = 0
        
        row = []
        for elem in line:
            if elem == "E":
                ex = x
                ey = y
                row.append(100)
            elif elem == "S":
                sx = x
                sy = y
                row.append(0)
            elif elem == "\n":
                pass
            else:
                row.append(ord(elem) - 96)
            x += 1
        map.append(row)
        y+= 1
    print(map)
    print("start: ", sx, " ", sy)
    print("mål: ", ex, " ", ey)