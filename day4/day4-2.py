
score = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        e = line.split(",")
        e1s = int(e[0].split("-")[0])
        e1e = int(e[0].split("-")[1])
        e2s = int(e[1].split("-")[0])
        e2e = int(e[1].split("-")[1])
        if ((e1s <= e2s and e1e >= e2s) or (e2s <= e1s and e2e >= e1s) or (e1s <= e2e and e1e >= e2e) or (e2s <= e1s and e2e >= e1e)):
            score += 1
    
print(score) 