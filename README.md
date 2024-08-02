# Chess Game in Pygame

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Game Mechanics](#game-mechanics)
6. [Undo Moves](#undo-moves)
7. [Future Scope](#future-scope)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction
This project is a chess game built using the Pygame library in Python. The game allows two players to play chess on the same computer. The game is designed with an intuitive graphical user interface, making it easy for players to enjoy the classic game of chess.

## Features
- Fully functional chess game with standard rules.
- Graphical user interface using Pygame.
- Move validation and enforcement of chess rules.
- Highlighting possible moves.
- Move history and undo functionality.

## Installation
### Prerequisites
- Python 3.x
- Pygame library

### Installing Pygame
You can install Pygame using pip:
```sh
pip install pygame
```

### Cloning the Repository
Clone this repository to your local machine using:
```sh
git clone https://github.com/yourusername/chess-pygame.git
cd chess-pygame
```

## Usage
Run the game by executing the `main.py` file:
```sh
python main.py
```

## Game Mechanics
### Board Representation
The chessboard is represented as an 8x8 grid, with each square either containing a piece or being empty.

### Pieces and Moves
Each piece (pawn, rook, knight, bishop, queen, king) follows standard chess rules for movement. The game enforces these rules to ensure only valid moves are made.

### Move Highlighting
When a player selects a piece, all possible valid moves for that piece are highlighted on the board.

### Capturing Pieces
If a move results in capturing an opponent's piece, the captured piece is removed from the board and stored in a list of captured pieces.

## Undo Moves
### Implementation
The game maintains a history of moves in a stack. Each move is recorded along with the state of the board before the move. To undo a move, the game pops the last move from the stack and restores the board to its previous state.

### Usage
To undo the last move, press the `U` key on the keyboard. The game will revert to the state before the last move was made.

## Future Scope
### Save and Load Game
Implement functionality to save the current game state to a file and load a previously saved game.

### AI Opponent
Develop an AI opponent that players can play against. The AI should have multiple difficulty levels.

### Online Multiplayer
Extend the game to support online multiplayer, allowing players to compete against others over the internet.

### Enhanced Graphics
Improve the graphical interface with better piece designs, animations, and sound effects.

## Contributing
Contributions are welcome! Please fork this repository and submit pull requests to contribute to the project.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-feature-branch`
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
