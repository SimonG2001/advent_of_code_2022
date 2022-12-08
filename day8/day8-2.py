


visibleTrees = 0
highestScenic = 0

def treeVisible(x, y, trees):
    scenicValue = 1
    if x == 0 or y == 0 or y == len(trees) - 1 or x == len(trees[y]) - 1:
        return 0

    treeValue = trees[y][x]
    
    stopped = True
    for xcheck in range(x):
        if trees[y][x - xcheck - 1] >= treeValue:
            scenicValue *= xcheck + 1
            stopped = False
            break
    if stopped:
        scenicValue *= x

    stopped = True
    for xcheck in range(len(trees[y]) - x - 1):
        if trees[y][x + xcheck + 1] >= treeValue:
            scenicValue *= xcheck + 1
            stopped = False
            break
    
    if stopped:
        scenicValue *= len(trees[y]) - x - 1
 
    stopped = True
    for ycheck in range(y):
        if trees[y - ycheck - 1][x] >= treeValue:
            scenicValue *= ycheck + 1
            stopped = False
            break
    if stopped:
        scenicValue *= y
    
    stopped = True
    for ycheck in range(len(trees) - y - 1):
        if trees[y + ycheck + 1][x] >= treeValue:
            scenicValue *= ycheck + 1
            stopped = False
            break
    if stopped:
        scenicValue *= len(trees) - y - 1
    return scenicValue

with open('input.txt', 'r') as f:
    lines = f.readlines()
    alllines = []
    totalSize = 0 
    for line in lines:
        currLine = []
        for elem in line:
            if elem == "\n":
                break
            currLine.append(int(elem))
        alllines.append(currLine)
    
    for y in range(len(alllines)):
        for x in range(len(alllines[y])):
            if treeVisible(x, y, alllines) > highestScenic:
                highestScenic = treeVisible(x, y, alllines)


    
    
print("exersice 2: ", highestScenic)
