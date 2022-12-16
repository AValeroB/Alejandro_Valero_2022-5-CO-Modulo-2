import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import CLOUD

class Cloud(Obstacle):
    CLOUD_HEIGHTS = [260, 220, 170]
    CLOUD = CLOUD

    def __init__(self):
        self.image = self.CLOUD
        self.type = 0
        self.rect = self.image[self.type]
        self.rect.y = self.CLOUD_HEIGHTS[random.randint(0, 2)]