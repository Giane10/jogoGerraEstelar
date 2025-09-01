# code/game.py

import pygame
import sys
import random
import os

# Importa as configurações e as classes do jogo
from . import config # ADICIONE/CORRIJA ESTA LINHA
from .player import Player
from .enemy import Enemy
from .menu import Menu
from .game_over import GameOver


# Classe principal que gerencia o jogo e seus estados.
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        # Usa as configurações do arquivo config.py para a tela
        self.tela = pygame.display.set_mode((config.LARGURA_TELA, config.ALTURA_TELA))
        pygame.display.set_caption(config.TITULO)
        self.clock = pygame.time.Clock()

        # Define o caminho base para os assets
        self.asset_path = "assets"

        # Carrega o fundo
        background_image_path = os.path.join(self.asset_path, "image", "fundo_nebulosa.png")
        self.background = pygame.image.load(background_image_path).convert()
        self.background = pygame.transform.scale(self.background, (config.LARGURA_TELA, config.ALTURA_TELA))
        self.bg_y = 0
        self.bg_velocidade = 2

        # Carrega os sons
        caminho_sons = os.path.join(self.asset_path, "sons")
        self.som_tiro = pygame.mixer.Sound(os.path.join(caminho_sons, "tiro.mp3"))
        pygame.mixer.music.load(os.path.join(caminho_sons, "somJogo.mp3"))
        pygame.mixer.music.set_volume(0.5)

        # Cria as telas
        self.menu = Menu(self.tela)
        self.game_over = GameOver(self.tela)

    # Contém a lógica principal do nível
    def play_level(self):
        # Configuração para um novo jogo
        player_image = "principal.png"
        player = Player(config.LARGURA_TELA / 2, config.ALTURA_TELA - 60, self.asset_path, player_image)

        all_sprites = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        all_sprites.add(player)

        vidas = 3
        pontuacao = 0
        fonte = pygame.font.Font(None, 36)

        enemy_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(enemy_timer, 1000)

        pygame.mixer.music.play(-1)

        # Loop do Jogo
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == enemy_timer:
                    enemy_image = "meteorGrey_med1.png"
                    # CORRIGIDO: Adiciona os argumentos 'speed' e 'size'
                    new_enemy = Enemy(random.randint(40, config.LARGURA_TELA - 40), -50, self.asset_path, enemy_image,
                                      speed=config.VELOCIDADE_INIMIGO, size=(45, 45))
                    enemies.add(new_enemy)
                    all_sprites.add(new_enemy)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
                    player.shoot()
                    self.som_tiro.play()

            # Atualizações
            player.update(config.LARGURA_TELA)
            enemies.update()
            player.projectiles.update()

            self.bg_y += self.bg_velocidade
            if self.bg_y >= config.ALTURA_TELA:
                self.bg_y = 0

            # Colisões
            hits = pygame.sprite.groupcollide(enemies, player.projectiles, True, True)
            if hits:
                pontuacao += len(hits) * 10

            if pygame.sprite.spritecollide(player, enemies, True):
                vidas -= 1
                if vidas <= 0:
                    pygame.mixer.music.stop()
                    return pontuacao

            # Verifica se inimigo passou
            for inimigo in enemies:
                if inimigo.rect.top > config.ALTURA_TELA:
                    inimigo.kill()
                    vidas -= 1
                    if vidas <= 0:
                        pygame.mixer.music.stop()
                        return pontuacao

            # Desenho na tela
            self.tela.blit(self.background, (0, self.bg_y))
            self.tela.blit(self.background, (0, self.bg_y - config.ALTURA_TELA))
            all_sprites.draw(self.tela)
            player.projectiles.draw(self.tela)

            # UI (Vidas e Pontuação)
            texto_vidas = fonte.render(f"Vidas: {vidas}", True, config.BRANCO)
            self.tela.blit(texto_vidas, (config.LARGURA_TELA - texto_vidas.get_width() - 10, 10))

            texto_pontuacao = fonte.render(f"Pontos: {pontuacao}", True, config.BRANCO)
            self.tela.blit(texto_pontuacao, (10, 10))

            pygame.display.flip()
            self.clock.tick(config.FPS)

    # Loop principal que gerencia os estados (telas).
    def run(self):
        while True:
            self.menu.run()
            final_score = self.play_level()
            self.game_over.run(final_score)
