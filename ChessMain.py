import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 20
IMAGES = {}

"""
Lets load Images of the pieces
"""

def loadImages():
    pieces = ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR", "bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR", "bP", "wP"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False #flag variable for when a move is made

    loadImages() #done only once before while loop
    running = True
    sqSelected = () #it is a tuple and will keep track of the user's last mouse location.
    playerClicks = [] #to keep track of player clicks with two tuples.
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row, col): #what if the user selects same square twice
                    sqSelected = () #this will set the sqselected variable to the default value
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) #we append for first and second clicks
                if len(playerClicks) == 2:
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                    sqSelected = ()
                    playerClicks = []
            elif e.type == p.KEYDOWN:
                if e.key == p.K_a:
                    gs.undoMove()
                    moveMade = True 
        
        #change to black 
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False
            print("Current player to move:", gs.currentPlayer())
            
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

    
    

"""
Draw game state is responsible for all the graphics of current gamestate.
"""

def drawGameState(screen, gs):
    drawBoard(screen) #to draw board on the screen
    drawPiece(screen, gs.board) #to draw pieces on the board


#Quick Note: The top left square is always white.
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    

def drawPiece(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))



if __name__ == "__main__":
    main()
