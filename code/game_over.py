

import pygame
import sys
import os


# Gerencia a tela de "Game Over".
class GameOver:
    def __init__(self, tela):
        self.tela = tela
        self.fonte_titulo = pygame.font.Font(None, 72)
        self.fonte_instrucao = pygame.font.Font(None, 40)
        self.fonte_pequena = pygame.font.Font(None, 24)  # Nova fonte para os créditos
        self.cor_texto = (255, 255, 255)

        asset_path = "assets"
        game_over_background_path = os.path.join(asset_path, "image", "game_over_final.png")
        self.background_image = pygame.image.load(game_over_background_path).convert()
        self.background_image = pygame.transform.scale(self.background_image,
                                                       (self.tela.get_width(), self.tela.get_height()))

    def desenhar(self, pontuacao):
        self.tela.blit(self.background_image, (0, 0))


        # Posição do texto da pontuação ajustada para ficar ACIMA do centro
        texto_pontuacao = self.fonte_instrucao.render(f"Pontuacao final: {pontuacao}", True, self.cor_texto)
        rect_pontuacao = texto_pontuacao.get_rect(center=(self.tela.get_width() / 2, self.tela.get_height() / 2 - 50))

        # Posição da instrução para reiniciar ajustada para ficar no centro
        texto_instrucao = self.fonte_instrucao.render("Pressione ENTER para reiniciar", True, self.cor_texto)
        rect_instrucao = texto_instrucao.get_rect(center=(self.tela.get_width() / 2, self.tela.get_height() / 2))

        self.tela.blit(texto_pontuacao, rect_pontuacao)
        self.tela.blit(texto_instrucao, rect_instrucao)


        # --- Adiciona os créditos na tela ---
        # Adiciona meu nome no canto inferior direito
        texto_nome = self.fonte_pequena.render("Criado por: Giane", True, self.cor_texto)
        rect_nome = texto_nome.get_rect(bottomright=(self.tela.get_width() - 10, self.tela.get_height() - 10))
        self.tela.blit(texto_nome, rect_nome)

        # Adiciona a nota de projeto acadêmico no canto inferior esquerdo
        texto_projeto = self.fonte_pequena.render("Projeto Acadêmico - UNINTER", True, self.cor_texto)
        rect_projeto = texto_projeto.get_rect(bottomleft=(10, self.tela.get_height() - 10))
        self.tela.blit(texto_projeto, rect_projeto)

    # Loop da tela de game over, aguarda o jogador interagir.

    def run(self, pontuacao):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return  # Sai do loop para voltar ao menu

            self.desenhar(pontuacao)
            pygame.display.flip()