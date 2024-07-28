import pygame
import random
import os
from sound import GameSound
from typing import Dict, Tuple, Optional

# Class for the Rock-Paper-Scissors game
class RockPaperScissors:
    def __init__(self, base_path: str):
        icon_path = os.path.join(base_path, "..", "icons")
        self.icons = self.load_icons(icon_path)
        self.icons_score = self.load_score_icons(icon_path)

        self.player_score = 0
        self.computer_score = 0
        self.draw = 0
        self.sound = GameSound(base_path)
        
        # Rules for determining the winner
        self.rules = {
            ("Rock", "Scissors"): True,
            ("Scissors", "Paper"): True,
            ("Paper", "Rock"): True
        }

    # Load the game icons
    def load_icons(self, icon_path: str) -> Dict[str, pygame.Surface]:
        return {
            "Rock": pygame.image.load(os.path.join(icon_path, "rock.png")),
            "Paper": pygame.image.load(os.path.join(icon_path, "paper.png")),
            "Scissors": pygame.image.load(os.path.join(icon_path, "scissor.png")),
        }

    # Load the score icons
    def load_score_icons(self, icon_path: str) -> Dict[str, pygame.Surface]:
        return {
            "Computer": pygame.image.load(os.path.join(icon_path, "computer.png")),
            "Person": pygame.image.load(os.path.join(icon_path, "person.png"))
        }

    # Get a random choice for the computer
    def get_computer_choice(self) -> str:
        return random.choice(list(self.icons.keys()))

    # Determine the winner of the round
    def determine_winner(self, player: str, computer: str) -> Optional[bool]:
        if player == computer:
            return None  # It's a draw
        return self.rules.get((player, computer), False)

    # Play a round of the game
    def play_round(self, player_choice: str) -> Tuple[str, str]:
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(player_choice, computer_choice)
        if winner is None:
            self.draw += 1
            self.sound.play_draw_sound()
            return "It's a draw!", computer_choice
        elif winner:
            self.player_score += 1
            self.sound.play_win_sound()
            return "You win!", computer_choice
        else:
            self.computer_score += 1
            self.sound.play_lose_sound()
            return "You lose!", computer_choice

# Initialize the game
def initialize_game(base_path: str) -> RockPaperScissors:
    pygame.init()
    return RockPaperScissors(base_path)

# Setup the game screen
def setup_screen() -> pygame.Surface:
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Rock, Paper, Scissors Game')
    return screen

# Main function to run the game
def main():
    base_path = os.path.dirname(__file__)
    game = initialize_game(base_path)
    screen = setup_screen()
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)
    # Define rectangles for score icons
    figures = {choice: pygame.Rect(10 + i * 210, 100, 65, 65) for i, choice in enumerate(game.icons_score.keys())}
    # Define rectangles for game buttons
    buttons = {choice: pygame.Rect(10 + i * 210, 350, 100, 100) for i, choice in enumerate(game.icons.keys())}

    BLACK = (0, 0, 0)
    font = pygame.font.SysFont(None, 48)

    running = True
    while running:
        screen.fill((245, 245, 220))
        # Handle events and update the game state
        running = handle_events(game, buttons, running)
        # Update the game screen
        update_screen(game, screen, font, figures, buttons, BLACK)
        clock.tick(30)

    pygame.quit()

# Handle events like quitting the game or clicking a button
def handle_events(game: RockPaperScissors, buttons: Dict[str, pygame.Rect], running: bool) -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False  # Exit the game loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for choice, rect in buttons.items():
                if rect.collidepoint(event.pos):
                    result, computer_choice = game.play_round(choice)
                    print(result, " ", computer_choice)
                    print(f"Score: You {game.player_score} - Computer {game.computer_score}")
    return running

# Update the game screen with the latest scores and icons
def update_screen(game: RockPaperScissors, screen: pygame.Surface, font: pygame.font.Font, figures: Dict[str, pygame.Rect], buttons: Dict[str, pygame.Rect], color: Tuple[int, int, int]):
    cmpt = font.render(str(game.computer_score), True, color)
    prsn = font.render(str(game.player_score), True, color)
    screen.blit(cmpt, (90, 120))
    screen.blit(prsn, (290, 120))

    # Draw score icons
    for i, rect in figures.items():
        pygame.draw.rect(screen, -1, rect)
        icon = pygame.transform.scale(game.icons_score[i], (rect.width, rect.height))
        screen.blit(icon, rect)

    # Draw game buttons
    for choice, rect in buttons.items():
        pygame.draw.rect(screen, -1, rect)
        icon = pygame.transform.scale(game.icons[choice], (rect.width, rect.height))
        screen.blit(icon, rect)

    pygame.display.flip()

if __name__ == "__main__":
    main()
