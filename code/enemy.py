# code/enemy.py

import pygame
from .entity import Entity


# Representa os meteoros que o jogador deve desviar ou destruir.
class Enemy(Entity):
    def __init__(self, x, y, asset_path, image_name, speed, size):
        # Inicia a classe Entity com os dados do inimigo.
        super().__init__(x, y, asset_path, image_name)

        # Ajusta o tamanho da imagem do inimigo.
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=(x, y))

        # Define a velocidade.
        self.speed = speed

    # Move o inimigo para baixo.
    def update(self):
        self.move(0, self.speed)

