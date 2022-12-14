
def main():
    with open('day14/input.txt', 'r') as f:
        lines = f.readlines()
        
        all = []
        
        for line in lines:
            moves = line.split("\n")[0].split("->")
            row = []
            for elem in moves:
                num = elem.split()[0].split(",")      
                row.append([int(num[0]),int(num[1])])
            all.append(row)

        board = []
        for y in range(164):
            row = []
            for x in range(330):
                if y == 163:
                    row.append("#")
                else:
                    row.append(".")
            board.append(row)


        for elems in all:
            currX = elems[0][0]
            currY = elems[0][1]
            elems.pop(0)
            board[currY][currX-335] = "#"   
            for elem in elems:
                while True:
                    if currX == elem[0] and currY == elem[1]:
                        break
                    elif currX == elem[0]:
                        if currY > elem[1]:
                            currY -= 1
                        else:
                            currY += 1
                    elif currY == elem[1]:
                        if currX > elem[0]:
                            currX -= 1
                        else:
                            currX += 1
                    board[currY][currX-335] = "#" 
        
        sandSX = 500 - 335 
        sandSY = 0
        count = 0
        part1 = True
        countP1 = 0
        while True:
            if board[sandSY][sandSX] == "o":
                break
            currX = sandSX
            currY = sandSY
            while True:
                if board[currY+1][currX] == ".":
                    currY += 1
                elif board[currY+1][currX-1] == ".":
                    currY += 1
                    currX -= 1
                elif board[currY+1][currX+1] == ".":
                    currY += 1
                    currX += 1
                else:
                    
                    board[currY][currX] = "o"
                    if part1 and currY == 162:
                        countP1 = count
                        part1 = False
                    count += 1
                    
                    break


        '''for i in range(164):
            print(''.join(board[i]))
        '''
        print("Part 1:", countP1)
        print("Part 2:", count)
        

if __name__ == "__main__": # x: 444-504  y: 14-161
    main()           