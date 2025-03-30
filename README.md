## Chess Question

### Project Overview

The goal was to develop a Python script that simulates a chess scenario where a white piece (either a pawn or a rook) attempts to capture black pieces placed on a chessboard.

### Repository Contents

- **`chess.py`** – the main Python script containing:
  - **Work plan**, written as comments, explaining the step-by-step approach used in development.
  - **Game script**, which includes user input handling, board generation, piece placement, and capture logic.

### Game Rules and Logic

This simulation follows simplified chess rules:

1. The game starts when the user selects a white piece (either a pawn or a rook) and enters its coordinates on the board.
2. Then, black pieces are placed, with a range of 1 to 16 pieces allowed.
3. The white piece (either a pawn or a rook) tries to capture black pieces according to chess movement rules:
   - **Pawns** move forward and capture diagonally.
   - **Rooks** move in straight lines.
4. The game ends by indicating which black pieces the white piece successfully captured.

### Special Conditions and Restrictions

- The game allows only **16 black pieces**, in accordance with chess rules.
- A **piece limit** is also specified based on the initial chessboard setup.
- **Pawn promotion** is not implemented since the game ends after one move. If a pawn reaches the 8th (or 1st) rank, it does not change into another piece.
- If players want to continue the game for more than one move, future updates could include logic for promoting pawns into other pieces.
