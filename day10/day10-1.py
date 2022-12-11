
score, cycle, strength = 0, 0, 1

with open('input.txt', 'r') as f:
    
    lines = f.readlines()

    for line in lines:
        lin = line.split()
        cycle += 1
        if cycle % 40 == 20:
            score += cycle * strength
        
        if lin[0] == "noop":
            pass
        
        elif lin[0] == "addx":
            cycle +=1
            if cycle % 40 == 20:
                score += cycle * strength

            strength += int(lin[1])
            

print(score)
        

        
        
        