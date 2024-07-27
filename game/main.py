# main.py
import pygame
import random
import os
from .sound import GameSound 

class RockPaperScissors:
    def __init__(self, base_path):
        icon_path = os.path.join(base_path, "..", "icons")
        self.icons = {
            "Rock": pygame.image.load(os.path.join(icon_path, "rock.png")),
            "Paper": pygame.image.load(os.path.join(icon_path, "paper.png")),
            "Scissors": pygame.image.load(os.path.join(icon_path, "scissor.png")),
        }
    
        self.icons_score = {
            "Computer": pygame.image.load(os.path.join(icon_path, "computer.png")),
            "Person": pygame.image.load(os.path.join(icon_path, "person.png"))
        }

        self.player_score = 0
        self.computer_score = 0
        self.sound = GameSound(base_path)
        
        self.rules = {
            ("Rock", "Scissors"): True,
            ("Scissors", "Paper"): True,
            ("Paper", "Rock"): True
        }

    def get_computer_choice(self):
        return random.choice(list(self.icons.keys()))

    def determine_winner(self, player, computer):
        if player == computer:
            return None  # It's a draw
        return self.rules.get((player, computer), False)

    def play_round(self, player_choice):
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(player_choice, computer_choice)
        if winner is None:
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

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Rock, Paper, Scissors Game')
    clock = pygame.time.Clock()
    base_path = os.path.dirname(__file__)

    game = RockPaperScissors(base_path)
    font = pygame.font.Font(None, 36)

    # Define button sizes and positions based on icon size
    figures = {choice: pygame.Rect(10 + i * 210, 100, 65, 65) for i, choice in enumerate(game.icons_score.keys())} 
    buttons = {choice: pygame.Rect(10 + i * 210, 350, 100, 100) for i, choice in enumerate(game.icons.keys())}

    BLACK = (0, 0, 0)
    font = pygame.font.SysFont(None, 48)
    cmpt = font.render(str(game.computer_score), True, BLACK)
    prsn = font.render(str(game.player_score), True, BLACK)

    running = True
    while running:
        screen.fill((255, 255, 252))  # Fill the screen with white

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for choice, rect in buttons.items():
                    if rect.collidepoint(event.pos):
                        result, computer_choice = game.play_round(choice)
                        print(result, " ", computer_choice)
                        print(f"Score: You {game.player_score} - Computer {game.computer_score}")

        # Render and blit score text
        cmpt = font.render(str(game.computer_score), True, BLACK)
        prsn = font.render(str(game.player_score), True, BLACK)
        screen.blit(cmpt, (90, 120))
        screen.blit(prsn, (290, 120))

        for i, rect in figures.items():
            pygame.draw.rect(screen, -1, rect)
            icon = pygame.transform.scale(game.icons_score[i], (rect.width, rect.height))
            screen.blit(icon, rect)

        for choice, rect in buttons.items():
            pygame.draw.rect(screen, -1, rect)
            icon = pygame.transform.scale(game.icons[choice], (rect.width, rect.height))
            screen.blit(icon, rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()