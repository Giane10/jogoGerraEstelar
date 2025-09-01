# code/menu.py
import pygame
import sys
import os
import random
from .enemy import Enemy


# Gerencia a tela de menu inicial.
class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.fonte_instrucao = pygame.font.Font(None, 40)
        self.fonte_controles = pygame.font.Font(None, 28)  # Fonte para os controles
        self.cor_texto = (255, 255, 255)
        self.asset_path = "assets"

        # Carrega a imagem de fundo do menu
        menu_background_path = os.path.join(self.asset_path, "image", "menu_inicial.png")
        self.background_image = pygame.image.load(menu_background_path).convert()
        self.background_image = pygame.transform.scale(self.background_image,
                                                       (self.tela.get_width(), self.tela.get_height()))

        # Lógica para os meteoros caindo
        self.meteors = pygame.sprite.Group()
        self.meteor_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.meteor_timer, 400)

    def desenhar(self):
        self.tela.blit(self.background_image, (0, 0))
        self.meteors.draw(self.tela)


        # --- Adiciona os controles na tela ---
        y_pos_controles = self.tela.get_height() / 2 + 200  # Posição inicial para os textos de controle

        texto_mover = self.fonte_controles.render("Setas Esquerda/Direita - Mover Nave", True, self.cor_texto)
        rect_mover = texto_mover.get_rect(center=(self.tela.get_width() / 2, y_pos_controles))
        self.tela.blit(texto_mover, rect_mover)

        texto_atirar = self.fonte_controles.render("Ctrl - Atirar", True, self.cor_texto)
        rect_atirar = texto_atirar.get_rect(center=(self.tela.get_width() / 2, y_pos_controles + 30))
        self.tela.blit(texto_atirar, rect_atirar)

    # Loop da tela de menu, fica ativo até o jogador interagir.
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                    self.meteors.empty()
                    return

                if event.type == self.meteor_timer:
                    enemy_image = "meteorGrey_med1.png"
                    new_meteor = Enemy(random.randint(0, self.tela.get_width()), -50, self.asset_path, enemy_image,
                                       speed=1, size=(65, 65))
                    self.meteors.add(new_meteor)

            self.meteors.update()
            self.desenhar()
            pygame.display.flip()
