import unittest
from src.rules import Rules
from src.board import Board

class TestRules(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.rules = Rules(self.board)

    def test_check_detection(self):
        # Set up a scenario where the king is in check
        self.board.setup_check_scenario()
        self.assertTrue(self.rules.is_in_check('w'))
        self.assertFalse(self.rules.is_in_check('b'))

    def test_checkmate_detection(self):
        # Set up a scenario where the king is in checkmate
        self.board.setup_checkmate_scenario()
        self.assertTrue(self.rules.is_checkmate('w'))
        self.assertFalse(self.rules.is_checkmate('b'))

    def test_stalemate_detection(self):
        # Set up a scenario where the game is in stalemate
        self.board.setup_stalemate_scenario()
        self.assertTrue(self.rules.is_stalemate('b'))
        self.assertFalse(self.rules.is_stalemate('w'))

    def test_pawn_promotion(self):
        # Set up a scenario for pawn promotion
        self.board.setup_pawn_promotion_scenario()
        self.rules.promote_pawn(0, 7, 'q')  # Promote to queen
        self.assertEqual(self.board.get_piece(0, 7), 'wQ')

if __name__ == '__main__':
    unittest.main()