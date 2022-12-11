
cycle, strength, pixelpos = 0, 1, 0

with open('input.txt', 'r') as f:
    
    lines = f.readlines()
    picture = ""

    for line in lines:
        lin = line.split()
        cycle += 1
        
        if abs(strength - pixelpos) <= 1:
            picture += "#"
        else:
            picture += " "
        pixelpos += 1

        if cycle % 40 == 0:
            picture += "\n"
            pixelpos = 0
        
        if lin[0] == "noop":
            pass
        
        elif lin[0] == "addx":
            cycle +=1
            if abs(strength - pixelpos) <= 1:
                picture += "#"
            else:
                picture += " "
            pixelpos += 1

            if cycle % 40 == 0:
                picture += "\n"
                pixelpos = 0

            strength += int(lin[1])
            
print(picture)
        

        
        
        