import pygame

# Define o comportamento dos tiros do jogador.
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 0)) # Amarelo
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -10 # Negativo para subir na tela



    def update(self):
        self.rect.y += self.speed
        # Remove o projétil se ele sair da tela.
        if self.rect.bottom < 0:
            self.kill()
