import unittest
from src.evaluation import evaluate_board

class TestEvaluationFunction(unittest.TestCase):

    def test_material_advantage(self):
        # Test a simple material advantage scenario
        board_state = [
            ["bR", "bN", "bB", "bQ", "bK", "--", "--", "--"],
            ["bP", "bP", "bP", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wK", "--", "--", "--"],
            ["wR", "wN", "wB", "wQ", "--", "--", "--", "--"],
        ]
        score = evaluate_board(board_state)
        self.assertGreater(score, 0)  # White should have an advantage

    def test_checkmate_scenario(self):
        # Test a checkmate scenario
        board_state = [
            ["bR", "bN", "bB", "bQ", "bK", "--", "--", "--"],
            ["bP", "bP", "bP", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wK", "--", "--", "--"],
            ["wR", "wN", "wB", "wQ", "--", "--", "--", "--"],
        ]
        score = evaluate_board(board_state)
        self.assertEqual(score, float('-inf'))  # Checkmate for black

    def test_stalemate_scenario(self):
        # Test a stalemate scenario
        board_state = [
            ["bK", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wK", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
        ]
        score = evaluate_board(board_state)
        self.assertEqual(score, 0)  # Stalemate should score as neutral

if __name__ == '__main__':
    unittest.main()