
import pygame
import sys
import random
import os

from . import config
from .player import Player
from .enemy import Enemy
from .menu import Menu
from .game_over import GameOver


# Classe principal que gerencia os estados do jogo e o loop principal.
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.tela = pygame.display.set_mode((config.LARGURA_TELA, config.ALTURA_TELA))
        pygame.display.set_caption(config.TITULO)
        self.clock = pygame.time.Clock()

        self.asset_path = "assets"

        # Carrega o fundo do jogo
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

    def play_level(self):
        # Reseta as variáveis para um novo jogo
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


        # Loop principal do nível
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == enemy_timer:
                    enemy_image = "meteorGrey_med1.png"
                    new_enemy = Enemy(random.randint(40, config.LARGURA_TELA - 40), -50, self.asset_path, enemy_image)
                    enemies.add(new_enemy)
                    all_sprites.add(new_enemy)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
                    player.shoot()
                    self.som_tiro.play()

            # Lógica de atualização dos objetos
            player.update(config.LARGURA_TELA)
            enemies.update()
            player.projectiles.update()


            self.bg_y += self.bg_velocidade
            if self.bg_y >= config.ALTURA_TELA:
                self.bg_y = 0

            # Lógica de colisões
            hits = pygame.sprite.groupcollide(enemies, player.projectiles, True, True)
            if hits:
                pontuacao += len(hits) * 10

            if pygame.sprite.spritecollide(player, enemies, True):
                vidas -= 1
                if vidas <= 0:
                    pygame.mixer.music.stop()
                    return pontuacao


            # Lógica de desenho
            self.tela.blit(self.background, (0, self.bg_y))
            self.tela.blit(self.background, (0, self.bg_y - config.ALTURA_TELA))
            all_sprites.draw(self.tela)
            player.projectiles.draw(self.tela)

            texto_vidas = fonte.render(f"Vidas: {vidas}", True, config.BRANCO)
            self.tela.blit(texto_vidas, (config.LARGURA_TELA - texto_vidas.get_width() - 10, 10))

            texto_pontuacao = fonte.render(f"Pontos: {pontuacao}", True, config.BRANCO)
            self.tela.blit(texto_pontuacao, (10, 10))

            pygame.display.flip()
            self.clock.tick(config.FPS)

    # Gerencia os estados do jogo (menu, jogando, game over).
    def run(self):
        while True:
            self.menu.run()
            final_score = self.play_level()
            self.game_over.run(final_score)

