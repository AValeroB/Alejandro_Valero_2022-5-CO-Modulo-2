import pygame

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus = Cactus(SMALL_CACTUS)
            self.obstacles.append(cactus)
        elif len(self.obstacles) == 2:
            cactus = Cactus(LARGE_CACTUS)
            self.obstacles.append(cactus)
        elif len(self.obstacles) == 0:
            bird = Bird(BIRD)
            self.obstacles(bird)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                #no me hizo falta el break xd

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)