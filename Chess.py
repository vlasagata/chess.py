"""
 Plan of execution:
     1. Get the white piece and its coordinates from the user.
       - Ensure valid input (piece type and position).
       - Restrict choices to pawn or rook.
     2. Get black pieces and their coordinates from the user.
       - Allow multiple pieces, but enforce limits on each type.
       - Ensure input validity (correct piece names and valid positions).
     3. Print the chessboard with the given pieces.
       - Display the board with pieces correctly placed.
       - Represent white and black pieces with appropriate symbols.
     4. Check which black pieces can be captured by the white piece.
       - If a pawn, check diagonal capture moves.
       - If a rook, check all straight-line moves until hitting an obstacle.
     5. Display the results.
       - List out any capturable black pieces with their positions.
"""

def validate_coordinates(coord: str) -> bool:
    """
    Validates if the given coordinates is a vailid chessboard square (e.g. a5 )

    Args:
        coord (str): The coordinate to validate (e.g. a1, h8)

    Returns:
        bool:True if the coordinate is valid, False otherwise.
    """
    return len(coord) == 2 and coord[0] in 'abcdefgh' and coord[1].isdigit() and 1 <= int(coord[1]) <= 8



def get_white_piece() -> tuple[str, str]:
    """
    Asks the user to choose a white piece (pawn or rook) and enter its coordinates.

    Returns:
        tuple[str, str]: The selected white piece and its position on the board.
    """
    print("Welcome to the Chess Capturing Game!")
    print("The game starts with the white piece ")

    while True:

        ask_input = input("Choose a figure (pawn or rook) and its coordinates (e.g. pawn c5): ")
        parts = ask_input.split() 

        if len(parts) != 2: 
            print("Invalid input. Please enter in the format: 'pawn c5'")
            continue
            
        figure_w, coordinates_w = parts 

        if figure_w not in {"pawn", "rook"}:
            print("Invalid piece. Choose 'pawn' or 'rook'. ")
            continue

        if validate_coordinates(coordinates_w):
            return figure_w, coordinates_w
        else:
            print("Invalid coordinates. Try again.")


    
def get_black_pieces(white_piece: tuple[str, str]) -> dict[str, str]:
    """
    Asks the user to place black pieces on the board.

    Returns:
        dict[str,str]: A dict of black pieces and theis coordinates
    """
        
    black_pieces_dict = {} 
    limits = {"king": 1, "queen": 1, "rook": 2, "bishop": 2, "knight": 2, "pawn": 8}

    current_count = {"king": 0, "queen": 0, "rook": 0, "bishop": 0, "knight": 0, "pawn": 0}
    coordinates_w = white_piece[1]

    print("Black pieces turn. ")

    while True:

        ask_for_black_input = input("Choose a figure from 1 to 16 and their coordinates (e.g.: knight a5), or type 'done' to finish: ")
            
        if ask_for_black_input.lower() == "done":
            if not black_pieces_dict:
                print("You must place at least one black piece!")
                continue
            break
            
        parts = ask_for_black_input.split()
        if len(parts) !=2:
            print("Invalid input. Please enter in the format: 'knight a5'")
            continue
            
        figure_b, coordinates_b = parts 

        if figure_b not in ["pawn", "rook", "knight", "bishop", "queen", "king"]:
            print("Invalid figure. Choose beetween: 'pawn', 'rook', 'knight', 'bishop', 'queen', 'king'. ")
            continue

        if coordinates_b == coordinates_w:
            print("Invalid move. You cannot place a black piece on the same square as the white piece.")
            continue

        if validate_coordinates(coordinates_b):
            if current_count[figure_b] < limits[figure_b]: 
                black_pieces_dict[coordinates_b] = figure_b
                current_count[figure_b] += 1 
            else:
                print(f"Too many {figure_b}s. It exceeds the limit. ")
                continue
        else:
            print("Invalid coordinates. Try again. ")
            continue

    return black_pieces_dict


def print_board(white_piece: tuple[str, str], black_pieces: list[tuple[str, str]]):
    """
    Prints the current state of the chessboard with the white piece and black pieces.

    Args:
    white_piece (tuple[str, str]): The white piece and its position.
    black_pieces (list[tuple[str, str]]): The list of black pieces and their positions.

    """

    figures = {
        "king": "K",
        "queen": "Q",
        "rook": "R",
        "bishop": "B",
        "knight": "N",
        "pawn": "P"
        }


    board = {f"{letter}{number}": "." for letter in "abcdefgh" for number in range(1, 9)}


    figure_w, coordinates_w = white_piece
    board[coordinates_w] = figures[figure_w] 


    for coord, figure in black_pieces.items():
        board[coord] = figures[figure] 


    for row in range(8, 0, -1): 
        row_str = str(row) + " |" 
        for column in "abcdefgh": 
            coord = column + str(row) 
            row_str += " " + board[coord] 
        print(row_str)

    print("    _______________")
    print("    a b c d e f g h")


def get_capturable_pieces(white_piece: tuple[str, str], black_pieces: list[tuple[str,str]]) -> list[str]:
    """
    Determines which black pieces can be captured by the white piece.

    Args:
        white_piece (tuple[str, str]): The white piece and its position.
        black_pieces (list[tuple[str, str]]): The list of black pieces and their positions.

    Returns:
        list[str]: A list of capturable black pieces and their positions.

    """
    figure_w, coordinates_w = white_piece
    capturable_pieces = [] 

    if figure_w == "pawn":
        possible_moves = [
            f"{chr(ord(coordinates_w[0]) - 1)}{int(coordinates_w[1]) + 1}",  
            f"{chr(ord(coordinates_w[0]) + 1)}{int(coordinates_w[1]) + 1}"   
        ]

        for move in possible_moves:
            if move in black_pieces:
                capturable_pieces.append((move, black_pieces[move])) 
        

    elif figure_w == "rook":
        directions = [(0,1), (0, -1), (-1, 0), (1, 0)] 

        for direct_x, direct_y in directions:
            x, y = coordinates_w[0], int(coordinates_w[1])

            while True:
                x = chr(ord(x) + direct_x) 
                y += direct_y 
                new_position = f"{x}{y}" 

                if x < "a" or x > "h" or y < 1 or y > 8: 
                    break

                if new_position in black_pieces: 
                    capturable_pieces.append((new_position, black_pieces[new_position]))
                    break

    return capturable_pieces 

def main():
    """
    The main function to run the chess piece setup and game logic.
    """

    white_piece =  get_white_piece()
    black_pieces = get_black_pieces(white_piece)

    print("\nGame setup complete! ")
    print("White piece: ", white_piece)
    print("Black pieces: ", black_pieces)

    print_board(white_piece, black_pieces)

    capturable = get_capturable_pieces(white_piece, black_pieces)

    if capturable:
        print("\nCapturable black pieces: ", capturable)
    else:
        print("\nNo capturable pieces. ")


main()







# Assumptions made:
# 1. The number of each black piece is limited (e.g., only 1 queen, 2 rooks) to reflect standard chess rules.
# 2. The user must enter at least one black piece before continuing.
# 3. The program does not allow more than 16 black pieces in total.