# code/enemy.py

import pygame
from .entity import Entity
from . import config

# Representa os meteoros.
class Enemy(Entity):
    def __init__(self, x, y, asset_path, image_name, speed, size):
        super().__init__(x, y, asset_path, image_name)

        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    # O update agora apenas move o inimigo para baixo.
    def update(self):
        self.move(0, self.speed)
