def evaluate_board(board):
    material_values = {
        'P': 1,
        'N': 3,
        'B': 3,
        'R': 5,
        'Q': 9,
        'K': 0  # King is invaluable
    }

    score = 0

    for row in board:
        for piece in row:
            if piece != '--':
                color = piece[0]  # 'b' for black, 'w' for white
                piece_type = piece[1]

                # Add material value
                if color == 'w':
                    score += material_values[piece_type]
                else:
                    score -= material_values[piece_type]

    # Add positional evaluation factors here (e.g., center control, mobility, etc.)

    return score