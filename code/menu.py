
import pygame
import sys
import os


# Gerencia a tela de menu inicial.
class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.fonte_instrucao = pygame.font.Font(None, 40)
        self.cor_texto = (255, 255, 255)

        asset_path = "assets"
        menu_background_path = os.path.join(asset_path, "image", "menu_inicial.png")
        self.background_image = pygame.image.load(menu_background_path).convert()
        self.background_image = pygame.transform.scale(self.background_image,
                                                       (self.tela.get_width(), self.tela.get_height()))


    def desenhar(self):
        self.tela.blit(self.background_image, (0, 0))

        texto_instrucao = self.fonte_instrucao.render("Pressione ENTER para começar", True, self.cor_texto)
        rect_instrucao = texto_instrucao.get_rect(center=(self.tela.get_width() / 2, self.tela.get_height() - 50))

        self.tela.blit(texto_instrucao, rect_instrucao)

    # Loop da tela de menu, fica ativo até o jogador interagir.
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return  # Sai do loop para começar o jogo

            self.desenhar()
            pygame.display.flip()


