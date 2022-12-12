
valueDict = {}
sx, sy, ex, ey, y = 0,0,0,0,0
recCount = 0
queue = []

def surroundValues(x, y, map):
    values = []
    if y == 0:
        values.append(0)
    else:
        values.append(map[y+1][x])
    if x == len(map[y]) - 1:
        values.append(0)
    else:
        values.append(map[y][x+1])
    if y == len(map) - 1:
        values.append(0)
    else:
        values.append(map[y-1][x])
    if x == 0:
        values.append(0)
    else:
        values.append(map[y][x-1])
    return values

def dfs(visited, map, currX, currY, value):
    global valueDict, sx, sy, ex, ey, y, recCount
    if [currX, currY] not in visited or valueDict[str(currX) + " " + str(currY)] > value:
        visited.append([currX, currY])
        
        valueDict[str(currX) + " " + str(currY)] = value

        currValue = map[currY][currX]
        value += 1
        recCount +=1
        print(recCount)
       
        if currY < len(map) - 1 and map[currY+1][currX] == currValue + 1:
            dfs(visited, map, currX, currY+1, value)
        if currX < len(map[currY]) - 1 and map[currY][currX+1] == currValue + 1:
            dfs(visited, map, currX+1, currY, value)
        if currY > 0 and map[currY-1][currX] == currValue + 1:
            dfs(visited, map, currX, currY-1, value)
        if currX > 0 and map[currY][currX-1] == currValue + 1:
            dfs(visited, map, currX-1, currY, value)

        if currY < len(map) - 1 and map[currY+1][currX] == currValue:
            dfs(visited, map, currX, currY+1, value)
        if currX < len(map[currY]) - 1 and map[currY][currX+1] == currValue:
            dfs(visited, map, currX+1, currY, value)
        if currY > 0 and map[currY-1][currX] == currValue:
            dfs(visited, map, currX, currY-1, value)
        if currX > 0 and map[currY][currX-1] == currValue:
            dfs(visited, map, currX-1, currY, value)
        
        if currY < len(map) - 1 and map[currY+1][currX] < currValue:
            dfs(visited, map, currX, currY+1, value)
        if currX < len(map[currY]) - 1 and map[currY][currX+1] < currValue:
            dfs(visited, map, currX+1, currY, value)
        if currY > 0 and map[currY-1][currX] < currValue:
            dfs(visited, map, currX, currY-1, value)
        if currX > 0 and map[currY][currX-1] < currValue:
            dfs(visited, map, currX-1, currY, value)
    
def bfs(visited, map, currX, currY, ex, ey):
    global queue, valueDict
    visited.append([currX, currY])
    queue.append([currX, currY])
    valueDict[str(currX) + " " + str(currY)] = 0
    while queue:
        m = queue.pop(0)
        
        currX = m[0]
        currY = m[1]
        myValue = valueDict[str(currX) + " " + str(currY)]
        if currX == ex and currY == ey:
            print(myValue)
            return
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


    bfs(visited, map, sx, sy, ex, ey)
   
                    