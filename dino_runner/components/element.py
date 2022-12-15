import pygame

from dino_runner.utils.constants import FONT_STYLE

class Element:

    def __init__(self):
        self.score = 0
        #self.death_count = 0
        self.highest_score = self.score

    def update_score(self, game):
            self.score += 1

            if self.score % 100 == 0 and game.game_speed > 500:
                game.game_speed += 5

    def draw_score(self, screen):
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (1000, 50)
        screen.blit(self.text, self.text_rect)