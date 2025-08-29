
import pygame
from .entity import Entity



# Representa os meteoros (inimigos)que caem.
class Enemy(Entity):

    def __init__(self, x, y, asset_path, image_name):
        super().__init__(x, y, asset_path, image_name)


        # Ajusta o tamanho da imagem do inimigo.
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = 3


    # Move o inimigo para baixo e o remove se sair da tela.
    def update(self):
        self.move(0, self.speed)
        if self.rect.top > 600:
            self.kill()


