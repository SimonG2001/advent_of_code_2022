


visibleTrees = 0

def treeVisible(x, y, trees):
    if x == 0 or y == 0 or y == len(trees) - 1 or x == len(trees[y]) - 1:
        return True
    treeValue = trees[y][x]

    visible = True
    for xcheck in range(x):
        if trees[y][xcheck] >= treeValue:
            visible = False
    if visible:
        return True
    
    visible = True
    for xcheck in range(len(trees[y]) - x - 1):
        if trees[y][x + xcheck + 1] >= treeValue:
            visible = False
    if visible:
        return True

    visible = True
    for ycheck in range(y):
        if trees[ycheck][x] >= treeValue:
            visible = False
    if visible:
        return True
    
    visible = True
    for ycheck in range(len(trees) - y - 1):
        if trees[y + ycheck + 1][x] >= treeValue:
            visible = False
    return visible

with open('input.txt', 'r') as f:
    lines = f.readlines()
    alllines = []
    totalSize = 0 
    for line in lines:
        currLine = []
        for elem in line:
            if elem == "\n":
                break
            currLine.append(elem)
        alllines.append(currLine)
    
    for y in range(len(alllines)):
        for x in range(len(alllines[y])):
            if treeVisible(x, y, alllines):
                visibleTrees += 1


    
    
print("exersice 1: ", visibleTrees)
