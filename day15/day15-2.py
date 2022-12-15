def isCloser(sensors, beacons, x, y):
    for i, elem in enumerate(sensors):
        dist = abs(elem[0]- beacons[i][0]) + abs(elem[1]- beacons[i][1])


def getMissingBeacon(sensors, pointsToCheck):
    for elem in pointsToCheck:
        test = True
        for elem2 in sensors:
            if abs(elem2[0]-elem[0]) + abs(elem2[1] - elem[1]) <= elem2[2]:
                test = False
                break
                #return x, y
        if test:
            return elem[0], elem[1]

   
    return 

def main():
    with open('day15/input.txt', 'r') as f:
        lines = f.readlines()
        
        
        sensors = []
        beacons = []
        for line in lines:
            line = line.split("\n")[0]
            sensor = line.split(":")[0]
            beacon = line.split(":")[1]
            sensor = sensor.split()
            sensorX = sensor[2].split(",")[0].split("=")[1]
            sensorY = sensor[3].split("=")[1]
            sensors.append([int(sensorX), int(sensorY)])
            beaconY = beacon.split("=")[2]
            beaconX = beacon.split(",")[0].split("=")[1]
            beacons.append((int(beaconX), int(beaconY)))

        
        
        for i, elem in enumerate(sensors):
            dist = abs(elem[0]- beacons[i][0]) + abs(elem[1]- beacons[i][1])
            sensors[i].append(dist)

        pointsToCheck = []
        print("start")
        print(len(sensors))
        for i, elem in enumerate(sensors):
            print(i)
            middlePointX = elem[0]
            middlePointY = elem[1]
            dir = 0
            posX = middlePointX
            posY = middlePointY + elem[2] + 1
            while True:
                if posX >= 0 and posY >= 0 and posX < 4000000 and posY < 4000000:
                    pointsToCheck.append([posX, posY])
                if dir == 0:
                    posX += 1
                    posY -= 1
                    if posY == middlePointY:
                        dir = 1
                elif dir == 1:
                    posX -= 1
                    posY -= 1
                    if posX == middlePointX:
                        dir = 2
                elif dir == 2:
                    posX -= 1
                    posY += 1
                    if posY == middlePointY:
                        dir = 3
                elif dir == 3:
                    posX += 1
                    posY += 1
                    if posX == middlePointX:

                        break

        beacons = list(dict.fromkeys(beacons))
     
        print("klar")
        
        
        #print(sensors)
        x, y = getMissingBeacon(sensors, pointsToCheck)
        
        #print(found)
        print(x, y)
        #print(x*4000000 + y)

if __name__ == "__main__": 
    main()           