def isCloser(sensors, beacons, x, y):
    for i, elem in enumerate(sensors):
        dist = abs(elem[0]- beacons[i][0]) + abs(elem[1]- beacons[i][1])


def main():
    score = 0
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
            beacons.append([int(beaconX), int(beaconY)])

        
        
        for i, elem in enumerate(sensors):
            dist = abs(elem[0]- beacons[i][0]) + abs(elem[1]- beacons[i][1])
            sensors[i].append(dist)


        
        print(sensors)
        startX = -10
        posY = 2000000
        found = []
        for i in range(5000000):
            posX = startX + i
            for elem in sensors:
                if abs(elem[0]-posX) + abs(elem[1] - posY) <= elem[2] and beacons.count([posX, posY]) == 0:
                    score += 1
                    found.append([posX, posY])
                    break
        #print(found)
        print(score)

if __name__ == "__main__": 
    main()           