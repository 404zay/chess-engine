from src.move_generation import generate_all_moves, generate_legal_moves
from src.pieces import PieceFactory


class Rules:
    def __init__(self, board):
        self.board = board
        self.piece_factory = PieceFactory()

    def _board_matrix(self):
        return self.board.board if hasattr(self.board, 'board') else self.board

    def is_in_check(self, color):
        king_position = self.find_king(color)
        if king_position is None:
            return False
        return self.is_square_attacked(king_position, color)

    def is_in_checkmate(self, color):
        if not self.is_in_check(color):
            return False
        return len(self.generate_all_legal_moves(color)) == 0

    def is_in_stalemate(self, color):
        if self.is_in_check(color):
            return False
        return len(self.generate_all_legal_moves(color)) == 0

    def is_checkmate(self, color):
        return self.is_in_checkmate(color)

    def is_stalemate(self, color):
        return self.is_in_stalemate(color)

    def find_king(self, color):
        for row in range(8):
            for col in range(8):
                piece = self._board_matrix()[row][col]
                if piece == f"{color}K":
                    return row, col
        return None

    def is_square_attacked(self, position, color):
        opponent_color = 'b' if color == 'w' else 'w'
        opponent_moves = generate_legal_moves(self.board, opponent_color)
        return any(end == position for _, end in opponent_moves)

    def is_valid_move(self, piece, start, end):
        piece_obj = self.piece_factory.create_piece(piece)
        if piece_obj is None:
            return False
        return end in piece_obj.get_valid_moves(start, self._board_matrix())

    def generate_all_legal_moves(self, color):
        return generate_all_moves(self.board, color)

    def get_piece_moves(self, piece, position):
        piece_obj = self.piece_factory.create_piece(piece)
        if piece_obj is None:
            return []
        return piece_obj.get_valid_moves(position, self._board_matrix())

    def promote_pawn(self, row, col, new_piece):
        matrix = self._board_matrix()
        current = matrix[row][col]
        if current == '--':
            color = 'w' if getattr(self.board, 'current_turn', 'white') == 'white' else 'b'
        else:
            color = current[0]
        matrix[row][col] = f"{color}{new_piece.upper()}"
        if hasattr(self.board, 'board'):
            self.board.board = matrix
