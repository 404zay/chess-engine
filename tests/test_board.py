import unittest
from src.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initialization(self):
        expected_initial_board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.assertEqual(self.board.board, expected_initial_board)

    def test_move_update(self):
        self.board.update_move((1, 0), (3, 0))  # Move bP to a3
        self.assertEqual(self.board.board[3][0], "bP")
        self.assertEqual(self.board.board[1][0], "--")

    def test_board_rendering(self):
        expected_render = (
            " bR bN bB bQ bK bB bN bR \n"
            " bP bP bP bP bP bP bP bP \n"
            " -- -- -- -- -- -- -- -- \n"
            " -- -- -- -- -- -- -- -- \n"
            " -- -- -- -- -- -- -- -- \n"
            " -- -- -- -- -- -- -- -- \n"
            " wP wP wP wP wP wP wP wP \n"
            " wR wN wB wQ wK wB wN wR \n"
        )
        self.assertEqual(self.board.render(), expected_render)

if __name__ == '__main__':
    unittest.main()