largest = 0
larger = 0
large = 0
with open('input1.txt', 'r') as f:
    lines = f.readlines()
    elf = 0
    for line in lines:
        if line.strip() == "":
            if elf > largest:
                large = larger
                larger = largest
                largest = elf
            elif elf > larger:
                large = larger
                larger = elf
            elif elf > large:
                large = elf
            elf = 0
        else:
            elf += int(line)
   
print(largest + larger + large)

    