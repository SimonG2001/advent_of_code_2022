
def main():
    score = 0
    with open('day14/input.txt', 'r') as f:
        lines = f.readlines()
        
        all = []
        ally = []
        allx = []
        
        for line in lines:
            line = line.split("\n")[0]
            moves = line.split("->")
            row = []
            for elem in moves:
                num = elem.split()[0].split(",")
                x = int(num[0])
                y = int(num[1])
                ally.append(y)
                allx.append(x)
                row.append([x,y])
            all.append(row)

        board = []
        for y in range(170):
            row = []
            for x in range(70):
                row.append(".")
            board.append(row)


        for elems in all:
            currX = elems[0][0]
            currY = elems[0][1]
            elems.pop(0)
            board[currY][currX] = "#"
            for elem in elems:
                while True:
                if 

        for i in range(170):
            print(''.join(board[i]))

if __name__ == "__main__": # x: 444-504  y: 14-161
    main()           