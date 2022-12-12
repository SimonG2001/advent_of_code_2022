
valueDict = {}
sx, sy, ex, ey, y = 0,0,0,0, 0


    
def bfs(visited, map, queue, ex, ey):
    global valueDict
    m = queue.pop(0)
    while queue:
        smallest = 600
        indexSmallest = 0
        for i, pos in enumerate(queue):
            if valueDict[str(pos[0]) + " " + str(pos[1])] < smallest:
                smallest = valueDict[str(pos[0]) + " " + str(pos[1])]
                indexSmallest = i

        m = queue.pop(indexSmallest)
        
        currX = m[0]
        currY = m[1]

        myValue = valueDict[str(currX) + " " + str(currY)]
        if currX == ex and currY == ey:
            
            return myValue
        currValue = map[currY][currX]

        if currY < len(map) - 1 and map[currY+1][currX] <= currValue + 1 and [currX, currY+1] not in visited:
            visited.append([currX, currY+1])
            queue.append([currX, currY+1])
            valueDict[str(currX) + " " + str(currY+1)] = myValue + 1
        if currX < len(map[currY]) - 1 and map[currY][currX+1] <= currValue + 1 and [currX+1, currY] not in visited:
            visited.append([currX+1, currY])
            queue.append([currX+1, currY])
            valueDict[str(currX+1) + " " + str(currY)] = myValue + 1
        if currY > 0 and map[currY-1][currX] <= currValue + 1 and [currX, currY-1] not in visited:
            visited.append([currX, currY-1])
            queue.append([currX, currY-1])
            valueDict[str(currX) + " " + str(currY-1)] = myValue + 1
        if currX > 0 and map[currY][currX-1] <= currValue + 1 and [currX-1, currY] not in visited:
            visited.append([currX-1, currY])
            queue.append([currX-1, currY])
            valueDict[str(currX-1) + " " + str(currY)] = myValue + 1
        
    return 520
    

with open('input.txt', 'r') as f:
    lines = f.readlines()
    
    map = [] 
    for line in lines:
        x = 0   
        row = []
        for elem in line:
            if elem == "E":
                ex = x
                ey = y
                row.append(26)
            elif elem == "S":
                sx = x
                sy = y
                row.append(1)
            elif elem == "\n":
                pass
            else:
                row.append(ord(elem) - 96)
            x += 1
        map.append(row)
        y+= 1
    

    visited = []
    queue = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 1:
                valueDict[str(x) + " " + str(y)] = 0
                queue.append([x, y])
                visited.append([x, y])
    
    print(bfs(visited, map, queue, ex, ey))
    
   
                    