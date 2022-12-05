
score = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if ((int(line.split(",")[0].split("-")[0]) <= int(line.split(",")[1].split("-")[0]) and int(line.split(",")[0].split("-")[1]) >= int(line.split(",")[1].split("-")[1])) or (int(line.split(",")[1].split("-")[0]) <= int(line.split(",")[0].split("-")[0]) and int(line.split(",")[1].split("-")[1]) >= int(line.split(",")[0].split("-")[1]))):
            score += 1  
print(score) 