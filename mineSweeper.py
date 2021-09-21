####Pseudo Code####
#There are 3 cases
#1. If we click on an unrevealed mine 'M'
#       change M to X and return
#2. Else: (don't click on a mine)
#       if board[x][y] has adjacent mines:
#           changed board[x][y] to num of adjacent mines
#       else: (if board[x][y] has no adjacent mines)
#           change bord[x][y] to 'B'
#           recurisviely reveal all of its adjacent unrevealed squares which will either be B or a digit

class Solution:
    #board:
    #(x-1, y-1) (x-1, y) (x-1, y+1)
    #(x, y-1) (x, y) (x, y+1)
    #(x+1, y-1 (x+1, y) (x+1, y+1)

    def getAdjacentMines(self, board, x, y):
        numMines=0
        for r in range(x-1, x+2):
            for c in range(y-1, y+2):
                if r>= 0 and r < len(board) and c >= 0 and c < len(board[r]) and board[r][c]=='M':
                    numMines+=1
        return numMines

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        #if we're givn an invalid board
        if not board:
            return board

        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            #get number of adjacent mines
            numMines = self.getAdjacentMines(board,x,y)
            #returns Truthy
            if numMines:
                board[x][y] = str(numMines)
            #else it's a blank space
            else:
                board[x][y] = 'B'
                for r in range(x-1, x+2):
                    for c in range(y-1, y+2):
                        #checks to make sure it's in bounds when we recursively call updateBoard
                        #don't want it to be 'B' b/c we've already checked B w/ board[r][c] = 'B'
                        if r>= 0 and r < len(board) and c >= 0 and c < len(board[r]) and board[r][c]!='B':
                            #[r,c] b/c click is a list
                            self.updateBoard(board,[r,c])
        return board
        