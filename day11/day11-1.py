

with open('input.txt', 'r') as f:
    
    lines = f.readlines()
    monkeys = []
    mon = 0
    all = []
    for line in lines:
        all.append(line.split("\n")[0])
    
    for elem in all:
        
        if elem == "":
            pass
        elif elem.split()[0] == "Monkey":
            
            if elem.split()[1] != "0:":
                monkeys.append(monkey)
            monkey = []
        
        elif elem.split()[0] == "Starting":
            monkey.append(elem.split(":")[1][1:].split(", "))
        
        elif elem.split()[0] == "Operation:":
            monkey.append([elem.split("=")[1].split()[1], elem.split("=")[1].split()[2]])

        elif elem.split()[0] == "Test:":
            monkey.append(int(elem.split()[3]))
        
        elif elem.split()[1] == "true:":
            monkey.append(int(elem.split()[5]))

        elif elem.split()[1] == "false:":
            monkey.append(int(elem.split()[5]))
   
    monkeys.append(monkey)
    inspect = []
    for i in monkeys:
        inspect.append(0)

    for i in range(20):
        for j in range(len(monkeys)):
            monkey = monkeys[j]
            while monkey[0]:
                inspect[j] += 1
                item = int(monkey[0].pop(0))
                if monkey[1][0] == "+":
                    item += int(monkey[1][1])
                else:
                    if monkey[1][1] == "old":
                        item *= item
                    else:
                        item *= int(monkey[1][1])

                item //= 3

                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)
    
    inspect.sort()
    print(inspect[-1] * inspect[-2])