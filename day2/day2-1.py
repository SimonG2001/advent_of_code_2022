
score = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        if (ord(line[2]) - ord(line[0])) == 23:
            score += 3
        score += ord(line[2]) - 87
        if (line[2] == "X" and line[0] == "C") or (line[2] == "Y" and line[0] == "A") or (line[2] == "Z" and line[0] == "B"):
            score += 6

print (score)



