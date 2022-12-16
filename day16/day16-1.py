def shortestDist(start, end, startTime, valves):
    queue = []
    queue.append(start)
    timetot = startTime
    while queue:



def best(timeLeft, totalFlowRate, totalFlown, currentPos, valves, openvalves):
    if timeLeft == 0:
        return totalFlown
    elif timeLeft == 1:
        return totalFlown + totalFlowRate
    timeLeft -= 1
    totalFlown += totalFlowRate

    if valves[currentPos][0] != 0 and not currentPos in openvalves:
        openvalves.append(currentPos)
        totalFlowRate += valves[currentPos][0]
        timeLeft -= 1
        totalFlown += totalFlowRate

    valuesneighbours = []
    for neighbour in valves[currentPos][1]:
        valuesneighbours.append(best(timeLeft, totalFlowRate, totalFlown, neighbour, valves, openvalves))
    valuesneighbours.sort()
    return valuesneighbours[-1]

def main():
    with open('day16/input2.txt', 'r') as f:
        lines = f.readlines()
        valves = {}
        flows = []
        for i, line in enumerate(lines):
            line = line.split("\n")[0]
            valveName = line.split()[1]
            flowRate = int(line.split(";")[0].split("=")[1])
            if flowRate != 0:
                flows.append(valveName)
            leadTo = []
            line = line.split("to")[1]
            
            endValves = line.split()
            endValves.pop(0)
            for elem in endValves:
                leadTo.append(elem.split(",")[0])
            
            valves[valveName] = [flowRate, leadTo]
        
        openValves = []
        time = 29
        totalFlowRate= 0
        flown = 0
        start = "AA"
        
        print(best(time, totalFlowRate, flown, start, valves, openValves))




if __name__ == "__main__": 
    main()           