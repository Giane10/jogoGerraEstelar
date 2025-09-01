# main.py

# Importa a classe principal do jogo, que está no arquivo game.py
from code.game import Game


# Bloco principal que executa o jogo quando o script é chamado diretamente.
if __name__ == '__main__':
    game = Game()
    game.run()
