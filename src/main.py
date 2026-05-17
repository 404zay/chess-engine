from board import Board
from move_generation import generate_all_moves
from minimax import best_move

def main():
    board = Board()

    print("Welcome to Chess!")
    print("Enter moves like: e2 e4")
    board.print_board()

    while True:
        if board.turn == 'w':
            user_input = input("Your move: ")
            try:
                start, end = user_input.split()
                move = (parse(start), parse(end))
                legal = generate_all_moves(board, 'w')
                if move not in legal:
                    print("Illegal move, try again.")
                    continue
                board.update_move(move[0], move[1])
            except:
                print("Invalid format. Use: e2 e4")
                continue
        else:
            print("AI thinking...")
            move = best_move(board, depth=3)
            if move is None:
                print("Checkmate or stalemate!")
                break
            board.update_move(move[0], move[1])

        board.print_board()

def parse(square):
    col = ord(square[0]) - ord('a')
    row = 8 - int(square[1])
    return (row, col)

if __name__ == "__main__":
    main()
    