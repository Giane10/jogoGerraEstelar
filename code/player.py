import pygame
from .entity import Entity
from .projectile import Projectile


# Representa a nave do jogador, herdando da classe Entity.
class Player(Entity):
    def __init__(self, x, y, asset_path, image_name):
        super().__init__(x, y, asset_path, image_name)

        # Ajusta a imagem para um tamanho melhor para o jogo.
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = 5
        self.projectiles = pygame.sprite.Group()

    # Controla o movimento do jogador com o teclado.
    def update(self, screen_width):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.move(-self.speed, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.move(self.speed, 0)



    # Cria um novo projétil.
    def shoot(self):
        new_projectile = Projectile(self.rect.centerx, self.rect.top)
        self.projectiles.add(new_projectile)
