# code/abertura.py
import pygame
import sys


# Função auxiliar para quebrar o texto em múltiplas linhas
def wrap_text(surface, text, font, color, rect):
    words = text.split(' ')
    lines = []
    current_line = ''
    for word in words:
        test_line = current_line + word + ' '
        if font.size(test_line)[0] < rect.width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + ' '
    lines.append(current_line)

    y = rect.top
    line_spacing = font.get_height() + 5
    for line in lines:
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(centerx=rect.centerx, top=y)
        surface.blit(text_surface, text_rect)
        y += line_spacing


# Gerencia a tela de abertura com a história do jogo.
class TelaAbertura:
    def __init__(self, tela):
        self.tela = tela
        self.fonte_historia = pygame.font.Font(None, 28)
        self.fonte_instrucao = pygame.font.Font(None, 30)
        self.cor_texto = (200, 200, 200)
        self.cor_instrucao = (255, 255, 255)

        # Texto da história com a gramática corrigida
        self.historia = (
            "No ano de 2065, décadas após a Terceira Guerra Mundial, a humanidade inicia sua reconstrução. "
            "As nações se uniram para formar a Aliança Terrestre, garantindo a paz. "
            "Mas uma ameaça surge do cosmos: uma tempestade de fragmentos cósmicos, "
            "apelidada de 'A Grande Queda', foi detectada em rota de colisão com a Terra. "
            "As defesas planetárias, ainda enfraquecidas, são incapazes de deter a ameaça. "
            "A última esperança reside em um piloto solitário, a bordo do protótipo 'Vanguarda'. "
            "Você é esse piloto. O destino da Terra está em suas mãos."
        )

    def desenhar(self):
        self.tela.fill((0, 0, 10))

        area_texto_historia = pygame.Rect(50, 50, self.tela.get_width() - 100, self.tela.get_height() - 150)
        wrap_text(self.tela, self.historia, self.fonte_historia, self.cor_texto, area_texto_historia)

        texto_instrucao = self.fonte_instrucao.render("Pressione ENTER para continuar...", True, self.cor_instrucao)
        rect_instrucao = texto_instrucao.get_rect(center=(self.tela.get_width() / 2, self.tela.get_height() - 50))
        self.tela.blit(texto_instrucao, rect_instrucao)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                    return

            self.desenhar()
            pygame.display.flip()