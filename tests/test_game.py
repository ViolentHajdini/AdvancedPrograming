import pytest
from game.main import RockPaperScissors

def test_initial_scores():
    """Test that initial scores are zero."""
    game = RockPaperScissors()
    assert game.player_score == 0
    assert game.computer_score == 0

def test_determine_winner():
    """Test the winner determination logic."""
    game = RockPaperScissors()
    # Check that correct win scenarios are handled
    assert game.determine_winner("Rock", "Scissors") == True
    assert game.determine_winner("Scissors", "Paper") == True
    assert game.determine_winner("Paper", "Rock") == True
    # Check that losing scenarios are handled
    assert game.determine_winner("Rock", "Paper") == False
    assert game.determine_winner("Scissors", "Rock") == False
    assert game.determine_winner("Paper", "Scissors") == False
    # Check for draws
    assert game.determine_winner("Rock", "Rock") is None
    assert game.determine_winner("Paper", "Paper") is None
    assert game.determine_winner("Scissors", "Scissors") is None

def test_play_round():
    """Test playing a round of the game."""
    game = RockPaperScissors()
    game.get_computer_choice = lambda: "Rock"  # Mock the computer's choice to be "Rock"
    message, _ = game.play_round("Scissors")
    assert "lose" in message.lower()
    assert game.computer_score == 1
    assert game.player_score == 0

    game.get_computer_choice = lambda: "Paper"  # Change mock to "Paper"
    message, _ = game.play_round("Scissors")
    assert "win" in message.lower()
    assert game.computer_score == 1
    assert game.player_score == 1
