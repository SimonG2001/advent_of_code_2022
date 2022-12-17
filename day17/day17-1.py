
def lowest(block):
    heights = []
    for elem in block:
        heights.append(elem[0])
    heights.sort()
    return heights[1]

def main():
    with open('day17/input2.txt', 'r') as f:
        line = f.readline()
        
        
            

        height = 0
        blockNum = 0
        board = []
        block = []
        for y in range (5):
            row = []
            for x in range(9):
                if x == 0 or x == 8:
                    row.append("|")
                elif y == 4:
                    row.append("-")
                elif y == 0 and x > 2 and x < 7:
                    block.append([y, x])
                    row.append("@")
                else:
                    row.append(".")
            board.append(row)

        while True:
            for direction in line:
                
                #print(board)
                if direction == "<":
                    canMove = True
                    for elem in block:
                        if board[elem[0]][elem[1]-1] == "|" or board[elem[0]][elem[1]-1] == "#":
                            canMove = False
                            break
                    if canMove:
                        for i, elem in enumerate(block):
                            board[elem[0]][elem[1]] = "."
                            block[i][1] -= 1
                        for elem in block:
                            board[elem[0]][elem[1]] = "@"
                elif direction == ">":
                    canMove = True
                    for elem in block:
                        if board[elem[0]][elem[1]+1] == "|" or board[elem[0]][elem[1]+1] == "#":
                            canMove = False
                            break
                    if canMove:
                        for i, elem in enumerate(block):
                            board[elem[0]][elem[1]] = "."
                            block[i][1] += 1
                        for elem in block:
                            board[elem[0]][elem[1]] = "@"
                
                canMove = True
                for elem in block:
                    if board[elem[0]+1][elem[1]] == "-" or board[elem[0]+1][elem[1]] == "#":
                        for i, elem in enumerate(block):
                            board[elem[0]][elem[1]] = "#"
                        
                        newHeight = len(board) - lowest(block) - 1
                        if newHeight > height:
                            height = newHeight
                        blockNum += 1


                        closest = len(board) - height - 1
                        if blockNum % 5 == 1:
                            for i in range(3-closest + 3):
                                board.insert(0, ["|", ".", ".", ".", ".", ".", ".", ".", "|"])
                            board[0] = ["|", ".", ".", ".", "@", ".", ".", ".", "|"]
                            board[1] = ["|", ".", ".", "@", "@", "@", ".", ".", "|"]
                            board[2] = ["|", ".", ".", ".", "@", ".", ".", ".", "|"]
                            block = [[0, 4], [1, 3], [1, 4], [1, 5], [2, 4]]
                        
                        elif blockNum % 5 == 2:
                            
                            for i in range(3-closest + 4):
                                board.insert(0, ["|", ".", ".", ".", ".", ".", ".", ".", "|"])
                            board[0] = ["|", ".", ".", ".", ".", "@", ".", ".", "|"]
                            board[1] = ["|", ".", ".", ".", ".", "@", ".", ".", "|"]
                            board[2] = ["|", ".", ".", "@", "@", "@", ".", ".", "|"]
                            block = [[0, 5], [1, 5], [2, 5], [2, 4], [2, 3]]

                        elif blockNum % 5 == 3:
                            for i in range(3-closest + 5):
                                board.insert(0, ["|", ".", ".", ".", ".", ".", ".", ".", "|"])
                            board[0] = ["|", ".", ".", "@", ".", ".", ".", ".", "|"]
                            board[1] = ["|", ".", ".", "@", ".", ".", ".", ".", "|"]
                            board[2] = ["|", ".", ".", "@", ".", ".", ".", ".", "|"]
                            board[3] = ["|", ".", ".", "@", ".", ".", ".", ".", "|"]
                            block = [[0, 3], [1, 3], [2, 3], [3, 3]]

                        elif blockNum % 5 == 4:
                            for i in range(3-closest + 1):
                                board.insert(0, ["|", ".", ".", ".", ".", ".", ".", ".", "|"])
                            board[0] = ["|", ".", ".", "@", "@", ".", ".", ".", "|"]
                            board[1] = ["|", ".", ".", "@", "@", ".", ".", ".", "|"]
                            block = [[0, 3], [0, 4], [1, 3], [1, 4]]

                        elif blockNum % 5 == 0:
                            for i in range(3-closest + 1):
                                board.insert(0, ["|", ".", ".", ".", ".", ".", ".", ".", "|"])
                            board[0] = ["|", ".", ".", "@", "@", "@", "@", ".", "|"]
                            block = [[0, 3], [0, 4], [0, 5], [0, 6]]
                            for row in board:
                                print(row)
                            print("")
                            while True:
                                pass
                            
                        for row in board:
                            print(row)
                        print("")

                        
                        #print(height)
                        


                        canMove = False
                if canMove:
                    for i, elem in enumerate(block):
                        board[elem[0]][elem[1]] = "."
                        block[i][0] += 1
                    for elem in block:
                        board[elem[0]][elem[1]] = "@"


if __name__ == "__main__": 
    main()           