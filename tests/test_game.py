import unittest
from unittest.mock import patch, Mock
import sys
import os

# Adjust the path to include the 'game' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../game')))

from main import RockPaperScissors

class TestRockPaperScissors(unittest.TestCase):
    def setUp(self):
        self.game = RockPaperScissors("test_path")
        self.game.sound = Mock()

    @patch('random.choice', return_value="Rock")
    def test_get_computer_choice(self, mock_choice):
        choice = self.game.get_computer_choice()
        self.assertEqual(choice, "Rock")

    def test_determine_winner(self):
        self.assertIsNone(self.game.determine_winner("Rock", "Rock"))
        self.assertTrue(self.game.determine_winner("Rock", "Scissors"))
        self.assertFalse(self.game.determine_winner("Rock", "Paper"))

    @patch.object(RockPaperScissors, 'get_computer_choice', return_value="Rock")
    def test_play_round(self, mock_get_choice):
        self.game.sound.play_draw_sound = Mock()
        result, computer_choice = self.game.play_round("Rock")
        self.assertEqual(result, "It's a draw!")
        self.assertEqual(computer_choice, "Rock")
        self.game.sound.play_draw_sound.assert_called_once()

if __name__ == '__main__':
    unittest.main()
