def _inside_board(row, col):
    return 0 <= row < 8 and 0 <= col < 8


def _piece_color(piece):
    return None if piece == '--' else piece[0]


def _is_empty(piece):
    return piece == '--'


def _is_enemy(piece, color):
    return piece != '--' and _piece_color(piece) != color


def _is_friend(piece, color):
    return piece != '--' and _piece_color(piece) == color


class Piece:
    def __init__(self, color):
        self.color = color

    def get_valid_moves(self, position, board):
        raise NotImplementedError('This method should be overridden by subclasses')


class Pawn(Piece):
    def get_valid_moves(self, position, board):
        row, col = position
        direction = -1 if self.color == 'w' else 1
        moves = []

        # One square forward
        forward_row = row + direction
        if _inside_board(forward_row, col) and _is_empty(board[forward_row][col]):
            moves.append((forward_row, col))

            # Two squares forward from starting rank
            start_row = 6 if self.color == 'w' else 1
            double_row = row + 2 * direction
            if row == start_row and _inside_board(double_row, col) and _is_empty(board[double_row][col]):
                moves.append((double_row, col))

        # Captures
        for capture_col in (col - 1, col + 1):
            capture_row = row + direction
            if _inside_board(capture_row, capture_col) and _is_enemy(board[capture_row][capture_col], self.color):
                moves.append((capture_row, capture_col))

        return moves


class Rook(Piece):
    def get_valid_moves(self, position, board):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            moves.extend(self._slide_moves(position, board, dr, dc))
        return moves

    def _slide_moves(self, position, board, dr, dc):
        row, col = position
        result = []
        while True:
            row += dr
            col += dc
            if not _inside_board(row, col):
                break
            target = board[row][col]
            if _is_empty(target):
                result.append((row, col))
                continue
            if _is_enemy(target, self.color):
                result.append((row, col))
            break
        return result


class Bishop(Piece):
    def get_valid_moves(self, position, board):
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            moves.extend(self._slide_moves(position, board, dr, dc))
        return moves

    def _slide_moves(self, position, board, dr, dc):
        row, col = position
        result = []
        while True:
            row += dr
            col += dc
            if not _inside_board(row, col):
                break
            target = board[row][col]
            if _is_empty(target):
                result.append((row, col))
                continue
            if _is_enemy(target, self.color):
                result.append((row, col))
            break
        return result


class Knight(Piece):
    def get_valid_moves(self, position, board):
        row, col = position
        moves = []
        offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        for dr, dc in offsets:
            target_row = row + dr
            target_col = col + dc
            if not _inside_board(target_row, target_col):
                continue
            target = board[target_row][target_col]
            if _is_empty(target) or _is_enemy(target, self.color):
                moves.append((target_row, target_col))
        return moves


class Queen(Piece):
    def get_valid_moves(self, position, board):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            moves.extend(self._slide_moves(position, board, dr, dc))
        return moves

    def _slide_moves(self, position, board, dr, dc):
        row, col = position
        result = []
        while True:
            row += dr
            col += dc
            if not _inside_board(row, col):
                break
            target = board[row][col]
            if _is_empty(target):
                result.append((row, col))
                continue
            if _is_enemy(target, self.color):
                result.append((row, col))
            break
        return result


class King(Piece):
    def get_valid_moves(self, position, board):
        row, col = position
        moves = []
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in offsets:
            target_row = row + dr
            target_col = col + dc
            if not _inside_board(target_row, target_col):
                continue
            target = board[target_row][target_col]
            if _is_empty(target) or _is_enemy(target, self.color):
                moves.append((target_row, target_col))
        return moves


class PieceFactory:
    _mapping = {
        'P': Pawn,
        'R': Rook,
        'B': Bishop,
        'N': Knight,
        'Q': Queen,
        'K': King,
    }

    def create_piece(self, piece_str):
        if piece_str == '--':
            return None
        color = piece_str[0]
        piece_type = piece_str[1]
        piece_class = self._mapping.get(piece_type)
        return piece_class(color) if piece_class else None
