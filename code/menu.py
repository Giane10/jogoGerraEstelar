# code/menu.py

import pygame
import sys
import os
import random
from .enemy import Enemy  # Importa a classe Enemy


# Gerencia a tela de menu inicial do jogo.
class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.fonte_instrucao = pygame.font.Font(None, 40)
        self.cor_texto = (255, 255, 255)
        self.asset_path = "assets"

        # Carrega a imagem de fundo do menu
        menu_background_path = os.path.join(self.asset_path, "image", "menu_inicial.png")
        self.background_image = pygame.image.load(menu_background_path).convert()
        self.background_image = pygame.transform.scale(self.background_image,
                                                       (self.tela.get_width(), self.tela.get_height()))

        # --- Lógica para os meteoros caindo ---
        self.meteors = pygame.sprite.Group()
        self.meteor_timer = pygame.USEREVENT + 2  # Um timer separado para o menu
        pygame.time.set_timer(self.meteor_timer, 400)  # Cria um meteoro a cada 400ms

    def desenhar(self):
        self.tela.blit(self.background_image, (0, 0))

        # Desenha os meteoros
        self.meteors.draw(self.tela)

        texto_instrucao = self.fonte_instrucao.render("Pressione ENTER para começar", True, self.cor_texto)
        rect_instrucao = texto_instrucao.get_rect(center=(self.tela.get_width() / 2, self.tela.get_height() - 100))

        self.tela.blit(texto_instrucao, rect_instrucao)

    # Loop da tela de menu, fica ativo até o jogador interagir.
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    # Limpa os meteoros da tela antes de sair do menu
                    self.meteors.empty()
                    return  # Sai do loop para começar o jogo

                # Cria um novo meteoro quando o timer dispara
                if event.type == self.meteor_timer:
                    enemy_image = "meteorGrey_med1.png"
                    # Cria um meteoro com velocidade e tamanho personalizados para o menu.
                    new_meteor = Enemy(random.randint(0, self.tela.get_width()), -50, self.asset_path, enemy_image,
                                       speed=1, size=(65, 65))
                    self.meteors.add(new_meteor)

            # Atualiza a posição dos meteoros
            self.meteors.update()

            self.desenhar()
            pygame.display.flip()
