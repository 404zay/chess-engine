from copy import deepcopy

from src.pieces import PieceFactory


class MoveGenerator:
    def __init__(self, board):
        self.board = board

    def get_all_moves(self, player_color):
        return generate_all_moves(self.board, player_color)

    def get_piece_moves(self, position):
        matrix = _board_matrix(self.board)
        square = matrix[position[0]][position[1]]
        if square == '--':
            return []
        piece = PieceFactory().create_piece(square)
        return piece.get_valid_moves(position, matrix) if piece else []


def _board_matrix(board):
    return board.board if hasattr(board, 'board') else board


def _normalize_color(player_color):
    if player_color in ('white', 'w'):
        return 'w'
    if player_color in ('black', 'b'):
        return 'b'
    raise ValueError("player_color must be 'white', 'black', 'w', or 'b'.")


def _clone_board(board):
    matrix = _board_matrix(board)
    return deepcopy(matrix)


def _apply_move(matrix, move):
    (sr, sc), (er, ec) = move
    matrix[er][ec] = matrix[sr][sc]
    matrix[sr][sc] = '--'
    return matrix


def _find_king(matrix, color):
    target = f"{color}K"
    for row in range(8):
        for col in range(8):
            if matrix[row][col] == target:
                return row, col
    return None


def generate_legal_moves(board, player_color):
    color_key = _normalize_color(player_color)
    legal_moves = []
    factory = PieceFactory()
    matrix = _board_matrix(board)

    for row in range(8):
        for col in range(8):
            square = matrix[row][col]
            if square.startswith(color_key):
                piece = factory.create_piece(square)
                if piece is None:
                    continue
                for target in piece.get_valid_moves((row, col), matrix):
                    legal_moves.append(((row, col), target))
    return legal_moves


def filter_legal_moves(board, moves, player_color):
    filtered_moves = []
    for move in moves:
        matrix = _clone_board(board)
        _apply_move(matrix, move)
        if not is_king_in_check(matrix, player_color):
            filtered_moves.append(move)
    return filtered_moves


def is_king_in_check(board, player_color):
    matrix = _board_matrix(board)
    color_key = _normalize_color(player_color)
    opponent = 'b' if color_key == 'w' else 'w'
    king_position = _find_king(matrix, color_key)
    if king_position is None:
        return True

    opponent_moves = generate_legal_moves(matrix, opponent)
    return any(end == king_position for (_, end) in opponent_moves)


def generate_all_moves(board, player_color):
    return filter_legal_moves(board, generate_legal_moves(board, player_color), player_color)


def get_all_pieces(board, player_color):
    color_key = _normalize_color(player_color)
    matrix = _board_matrix(board)
    pieces = []
    for row in range(8):
        for col in range(8):
            square = matrix[row][col]
            if square.startswith(color_key):
                pieces.append(((row, col), square))
    return pieces
