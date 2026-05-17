class Board:
    def __init__(self):
        self.board = self._starting_board()
        self.current_turn = 'white'  # White starts
        self.move_log = []

    def _starting_board(self):
        return [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]

    def __iter__(self):
        return iter(self.board)

    def __getitem__(self, index):
        return self.board[index]

    def render(self):
        rows = [f" {' '.join(row)} " for row in self.board]
        return "\n".join(rows) + "\n"

    def parse_move(self, move):
        if isinstance(move, str):
            tokens = move.strip().lower().split()
            if len(tokens) != 2:
                raise ValueError("Move must be in the format 'e2 e4'.")
            return self._algebraic_to_position(tokens[0]), self._algebraic_to_position(tokens[1])
        if isinstance(move, (tuple, list)) and len(move) == 2:
            return tuple(move[0]), tuple(move[1])
        raise ValueError("Unsupported move format.")

    def _algebraic_to_position(self, algebraic):
        if len(algebraic) != 2:
            raise ValueError("Algebraic notation must be 2 characters, e.g. 'e2'.")
        file_char, rank_char = algebraic[0], algebraic[1]
        if file_char < 'a' or file_char > 'h' or rank_char < '1' or rank_char > '8':
            raise ValueError("Algebraic notation must be in range a1-h8.")
        col = ord(file_char) - ord('a')
        row = 8 - int(rank_char)
        return row, col

    def update(self, move):
        start_pos, end_pos = self.parse_move(move)
        self.update_move(start_pos, end_pos)

    def update_move(self, start_pos, end_pos):
        piece = self.board[start_pos[0]][start_pos[1]]
        captured = self.board[end_pos[0]][end_pos[1]]
        self.board[end_pos[0]][end_pos[1]] = piece
        self.board[start_pos[0]][start_pos[1]] = "--"
        self.move_log.append((start_pos, end_pos, piece, captured))
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'

    def make_move(self, move):
        if isinstance(move, (tuple, list)) and len(move) == 2:
            self.update_move(move[0], move[1])
        else:
            self.update(move)

    def undo_move(self, move_record):
        if not move_record or len(move_record) != 4:
            raise ValueError("Undo requires a move record from update_move.")
        start_pos, end_pos, piece, captured = move_record
        self.board[start_pos[0]][start_pos[1]] = piece
        self.board[end_pos[0]][end_pos[1]] = captured
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'

    def is_game_over(self):
        has_white_king = any('wK' in row for row in self.board)
        has_black_king = any('bK' in row for row in self.board)
        return not (has_white_king and has_black_king)

    def setup_initial_position(self):
        self.board = self._starting_board()
        self.current_turn = 'white'
        self.move_log = []

    def setup_check_scenario(self):
        self.board = [["--"] * 8 for _ in range(8)]
        self.board[0][4] = "bR"
        self.board[0][7] = "bK"
        self.board[7][4] = "wK"
        self.current_turn = 'white'
        self.move_log = []

    def setup_checkmate_scenario(self):
        self.board = [["--"] * 8 for _ in range(8)]
        self.board[7][7] = "wK"
        self.board[6][6] = "bQ"
        self.board[5][5] = "bK"
        self.current_turn = 'white'
        self.move_log = []

    def setup_stalemate_scenario(self):
        self.board = [["--"] * 8 for _ in range(8)]
        self.board[0][7] = "bK"
        self.board[1][5] = "wQ"
        self.board[2][5] = "wK"
        self.current_turn = 'black'
        self.move_log = []

    def setup_pawn_promotion_scenario(self):
        self.board = [["--"] * 8 for _ in range(8)]
        self.board[1][7] = "wP"
        self.board[0][7] = "--"
        self.current_turn = 'white'
        self.move_log = []

    def get_piece(self, row, col):
        return self.board[row][col]

    def print_board(self):
        print(self.render())

    def reset_board(self):
        self.__init__()
