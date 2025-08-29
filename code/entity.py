
import pygame
import os


# Classe para todos os objetos do jogo (jogador, inimigos).
# Herda de pygame.sprite.Sprite para usar os recursos de grupo do Pygame.
class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, asset_path, image_name):
        super().__init__()

        image_full_path = os.path.join(asset_path, "image", image_name)

        self.image = pygame.image.load(image_full_path).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))


    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
