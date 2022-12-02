#include 

largest = 0

with open('input1.txt', 'r') as f:
    lines = f.readlines()
    elf = 0
    for line in lines:
        if line.strip() == "":
            if elf > largest:
                    largest = elf
            elf = 0
        else:
            elf += int(line)
   
print(largest)
    