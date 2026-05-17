import unittest
from src.minimax import minimax
from src.board import Board

class TestMinimax(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.max_depth = 3  # Set a reasonable depth for testing

    def test_minimax_returns_best_move(self):
        # Assuming the board is in a specific state
        best_move = minimax(self.board, self.max_depth, True)
        self.assertIsNotNone(best_move)
        # Additional assertions can be added based on expected move

    def test_minimax_with_check(self):
        # Set up a board state where the AI is in check
        self.board.set_check_state()  # Hypothetical method to set check
        best_move = minimax(self.board, self.max_depth, True)
        self.assertIsNotNone(best_move)
        # Assert that the move does not leave the king in check

    def test_minimax_depth_limit(self):
        # Test that the minimax function respects the depth limit
        best_move = minimax(self.board, 0, True)
        self.assertIsNotNone(best_move)
        # Check that the depth limit is enforced

if __name__ == '__main__':
    unittest.main()