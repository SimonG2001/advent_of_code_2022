def shortestDist(start, end, valves):
    queue = []
    queue.append([start, 0])
    lookedThrough = [start]
    while queue:
        curr = queue.pop(0)
        
        if curr[0] == end:
            return curr[1] + 1
        
        for neighbour in valves[curr[0]][1]:
            if not neighbour in lookedThrough:
                lookedThrough.append(neighbour)
                queue.append([neighbour, curr[1]+1])
    
    return -1



def best(timeForOpenNodeFromNode, nodes, valves, currentValve, currentTime, totalFlow, currentFlow, opened):
    all = []
    for node in timeForOpenNodeFromNode[currentValve]:
        if node[0] not in opened:
            time = node[1]
            if time + currentTime < 30:
                opened.append(node[0])
                all.append(best(timeForOpenNodeFromNode, nodes, valves, node[0], currentTime+time, totalFlow+(currentFlow)*time, currentFlow+valves[node[0]][0], opened))
                opened.pop(-1)
    all.append(totalFlow+currentFlow*(30-currentTime))
    all.sort()
    return all[-1]



def main():
    with open('day16/input.txt', 'r') as f:
        lines = f.readlines()
        valves = {}
        nodes = []
        for i, line in enumerate(lines):
            line = line.split("\n")[0]
            valveName = line.split()[1]
            flowRate = int(line.split(";")[0].split("=")[1])
            if flowRate != 0 or valveName == "AA":
                nodes.append(valveName)
            leadTo = []
            line = line.split("to")[1]
            
            endValves = line.split()
            endValves.pop(0)
            for elem in endValves:
                leadTo.append(elem.split(",")[0])
            
            valves[valveName] = [flowRate, leadTo]
        
        
        start = "AA"
        timeFromNodeToNodeAndOpen = {}
        
        for startNode in nodes:
            timeFromStart = []
            for endNode in nodes:
                if startNode != endNode and endNode != start:
                    dist = shortestDist(startNode, endNode, valves)
                    if dist != -1:
                        timeFromStart.append([endNode, dist])
            timeFromNodeToNodeAndOpen[startNode] = timeFromStart


        print(best(timeFromNodeToNodeAndOpen, nodes, valves, start, 0, 0, 0, []))



if __name__ == "__main__": 
    main()           