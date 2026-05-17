import unittest
from src.move_generation import generate_legal_moves
from src.board import Board

class TestMoveGeneration(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_pawn_moves(self):
        self.board.setup_initial_position()
        legal_moves = generate_legal_moves(self.board, 'w')
        # Check that pawns can move forward
        self.assertIn(('e', 4), legal_moves)  # e2 to e4
        self.assertIn(('d', 4), legal_moves)  # d2 to d4

    def test_rook_moves(self):
        self.board.setup_initial_position()
        legal_moves = generate_legal_moves(self.board, 'w')
        # Check that rooks can move vertically and horizontally
        self.assertIn(('a', 5), legal_moves)  # a1 to a5
        self.assertIn(('h', 3), legal_moves)  # h1 to h3

    def test_knight_moves(self):
        self.board.setup_initial_position()
        legal_moves = generate_legal_moves(self.board, 'w')
        # Check that knights can move in L shapes
        self.assertIn(('b', 3), legal_moves)  # g1 to f3
        self.assertIn(('c', 4), legal_moves)  # g1 to e2

    def test_bishop_moves(self):
        self.board.setup_initial_position()
        legal_moves = generate_legal_moves(self.board, 'w')
        # Check that bishops can move diagonally
        self.assertIn(('c', 6), legal_moves)  # f1 to c4
        self.assertIn(('d', 5), legal_moves)  # f1 to d2

    def test_queen_moves(self):
        self.board.setup_initial_position()
        legal_moves = generate_legal_moves(self.board, 'w')
        # Check that queens can move in all directions
        self.assertIn(('d', 5), legal_moves)  # d1 to d5
        self.assertIn(('h', 5), legal_moves)  # d1 to h5

    def test_king_moves(self):
        self.board.setup_initial_position()
        legal_moves = generate_legal_moves(self.board, 'w')
        # Check that kings can move one square in any direction
        self.assertIn(('e', 5), legal_moves)  # e1 to e2
        self.assertIn(('f', 1), legal_moves)  # e1 to f1

    def test_edge_cases(self):
        # Test for check and checkmate scenarios
        self.board.setup_check_scenario()
        legal_moves = generate_legal_moves(self.board, 'w')
        self.assertEqual(len(legal_moves), 0)  # No legal moves if in check

if __name__ == '__main__':
    unittest.main()