class GameState():
    def __init__(self):
        #The board is a 8x8 2D list and each element of the list has 2 chars.
        #First char represents colour of the peice and the second char represents the type of the piece.
        #We have K, Q, R, B, N, P.
        #we have represented blank spaces as "--".

        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--" #after the piece is moved -- will take its place
        self.board[move.endRow][move.endCol] = move.pieceMoved #the coordinates where the piece will be moved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove #to Swap players

    def undoMove(self):
        if self.moveLog != 0: #Checking if the move log is empty if it is then there is no point in undoing
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

    def getValidMoves(self):
        return self.getAllPossibleMoves()


    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)): #number of rows
            for c in range(len(self.board[r])): #number of columns
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == 'P':
                        self.getPawnMoves(r, c, moves)
                    if piece == 'R':
                        self.getRookMoves(r, c, moves)
                    if piece == 'B':
                        self.getBishopMoves(r, c, moves)
                    if piece == 'N':
                        self.getNightMoves(r, c, moves)
                    if piece == 'K':
                        self.getKingMoves(r, c, moves)
                    if piece == 'Q':
                        self.getQueenMoves(r, c, moves)
        return moves
    

    def getPawnMoves(self, r, c, moves):
        if self.whiteToMove: #White Moves
            if self.board[r-1][c] == "--":
                moves.append(Move((r, c), (r-1, c), self.board))
                if r == 6 and self.board[r-2][c] == "--":
                    moves.append(Move((r, c), (r-2, c), self.board))
            
            #Captures
                if c-1 >= 0:
                    if self.board[r-1][c-1][0] == 'b':
                        moves.append(Move((r, c), (r-1, c-1), self.board))
                
                if c+1 <= 7:
                    if self.board[r-1][c+1][0] == 'b':
                        moves.append(Move((r, c), (r-1, c+1), self.board))

        else: #Black Moves
            if self.board[r+1][c] == '--':
                moves.append(Move((r, c), (r+1, c), self.board))
                if r == 1 and self.board[r+2][c] == "--": #2 square moves
                    moves.append(Move((r, c), (r+2, c),self.board))

            #Captures
            if c+1 >= 0:
                if self.board[r+1][c-1][0] == 'w':
                    moves.append(Move((r, c), (r+1, c-1), self.board))

            if c+1 <=7:
                    if self.board[r+1][c+1][0] == 'w':
                        moves.append(Move((r, c), (r+1, c+1), self.board))



    def getRookMoves(self, r, c, moves):
        pass

    def getBishopMoves(self, r, c, moves):
        pass

    def getNightMoves(self, r, c, moves):
        pass

    def getKingMoves(self, r, c, moves):
        pass

    def getQueenMoves(self, r, c, moves):
        pass

    def currentPlayer(self):
        return "White" if self.whiteToMove else "Black"
    

class Move():
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}

    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, 
               "e": 4, "f": 5, "g": 6, "h": 7}

    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, stsquare, edsquare, board):
        self.startRow = stsquare[0]
        self.startCol = stsquare[1]
        self.endRow = edsquare[0]
        self.endCol = edsquare[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol


    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False


    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
    


