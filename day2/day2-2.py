
score = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if line[2] == "X":
            if line[0] == "A":
                score += 3
            else:
                score += ord(line[0]) - 65
        elif line[2] == "Y":
            score += 3
            score += ord(line[0]) - 64
        elif line[2] == "Z":
            score += 6
            if line[0] == "C":
                score += 1
            else:
                score += ord(line[0]) - 63
                        

print (score)



