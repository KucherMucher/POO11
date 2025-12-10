import pygame
import sys

pygame.init()

# -------------------------------------------------------------
# CONFIGURAÇÃO DA JANELA EM ECRÃ INTEIRO
# -------------------------------------------------------------
info = pygame.display.Info()
LARGURA = info.current_w       # largura do ecrã
ALTURA = info.current_h        # altura do ecrã

# FULLSCREEN faz a janela ocupar o ecrã todo
ecra = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
pygame.display.set_caption("Quiz - Tecnologias da Informação")

clock = pygame.time.Clock()

# -------------------------------------------------------------
# CORES (RGB)
# -------------------------------------------------------------
BRANCO   = (255, 255, 255)
PRETO    = (0, 0, 0)
VERMELHO = (220, 20, 60)
AZUL     = (30, 144, 255)
VERDE    = (34, 139, 34)
AMARELO  = (255, 215, 0)
CINZENTO_ESCURO = (20, 20, 20)

# -------------------------------------------------------------
# IMAGEM DE FUNDO
# Colocar um ficheiro "fundo_quiz.jpg" na mesma pasta do código.
# Se não existir, o código usa um fundo de cor lisa.
# -------------------------------------------------------------
try:
    img_fundo = pygame.image.load("fundo_quiz.png") #Z:\\11F\\nao_tocas_grrrrr\\forvscode\POO\pygame exerc\\15\\2.jpg
    img_fundo = pygame.transform.scale(img_fundo, (LARGURA, ALTURA))
    usar_imagem_fundo = True
except:
    usar_imagem_fundo = False

# -------------------------------------------------------------
# FONTES
# None = fonte padrão do sistema
# O número indica o tamanho da letra
# -------------------------------------------------------------
fonte_pergunta = pygame.font.Font(None, 52)  # pergunta grande
fonte_resposta = pygame.font.Font(None, 32)  # texto das respostas
fonte_info     = pygame.font.Font(None, 32)  # pontuação e nº pergunta

# -------------------------------------------------------------
# DADOS DO QUIZ (EXEMPLO SIMPLES)
# -------------------------------------------------------------
num_pergunta = 1
total_perguntas = 10
pontuacao = 0

pergunta = "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"

# Respostas curtas para caberem numa linha dentro dos botões
respostas = [
    "Programa que gere o computador",   # correta (exemplo)
    "Cabo que liga o computador",
    "Ficheiro de texto simples",
    "Componente físico interno"
]

# -------------------------------------------------------------
# BOTÕES DE RESPOSTA (4 BOTÕES COLORIDOS)
# Dimensões calculadas em função do tamanho do ecrã
# -------------------------------------------------------------
LARGURA_BOTAO = int(LARGURA * 0.35)   # 35% da largura do ecrã
ALTURA_BOTAO  = int(ALTURA * 0.10)   # 10% da altura do ecrã
ESP_VERTICAL  = int(ALTURA * 0.1)   # espaço entre linhas de botões

# duas linhas de botões (linha 1 e linha 2)
y_linha1 = int(ALTURA * 0.55)
y_linha2 = y_linha1 + ALTURA_BOTAO + ESP_VERTICAL

# posição à esquerda e à direita
x_esquerda = int(LARGURA * 0.12)
x_direita  = LARGURA - LARGURA_BOTAO - x_esquerda

# rectângulos dos botões (posição e tamanho)
botao_rects = [
    pygame.Rect(x_esquerda, y_linha1, LARGURA_BOTAO, ALTURA_BOTAO),
    pygame.Rect(x_direita,  y_linha1, LARGURA_BOTAO, ALTURA_BOTAO),
    pygame.Rect(x_esquerda, y_linha2, LARGURA_BOTAO, ALTURA_BOTAO),
    pygame.Rect(x_direita,  y_linha2, LARGURA_BOTAO, ALTURA_BOTAO),
]

# cor de cada botão (uma cor diferente)
cores_botoes = [AZUL, VERMELHO, VERDE, AMARELO]

# -------------------------------------------------------------
# FUNÇÕES DE DESENHO DA INTERFACE
# -------------------------------------------------------------
def desenhar_fundo():
    """Desenha a imagem de fundo ou uma cor lisa."""
    if usar_imagem_fundo:
        ecra.blit(img_fundo, (0, 0))
    else:
        ecra.fill(BRANCO)

def desenhar_barra_superior():
    """Desenha a barra superior com nº da pergunta e pontuação."""
    altura_barra = 60
    pygame.draw.rect(ecra, PRETO, (0, 0, LARGURA, altura_barra))

    texto_info = f"Pergunta: {num_pergunta}/{total_perguntas}   |   Pontuação: {pontuacao}"
    sup_info = fonte_info.render(texto_info, True, BRANCO)
    rect_info = sup_info.get_rect(midtop=(LARGURA // 2, 10))
    ecra.blit(sup_info, rect_info)

def desenhar_pergunta():
    """Desenha a pergunta em grande, centrada na parte superior."""
    sup_pergunta = fonte_pergunta.render(pergunta, True, BRANCO)
    rect_pergunta = sup_pergunta.get_rect(center=(LARGURA // 2, int(ALTURA * 0.25)))
    size_backpergunta = sup_pergunta.get_size()
    rect_backpergunta = ((rect_pergunta.x-50, rect_pergunta.y-50), (size_backpergunta[0]+100, size_backpergunta[1]+100))
    pygame.draw.rect(ecra, PRETO, rect_backpergunta, border_radius=15)
    ecra.blit(sup_pergunta, rect_pergunta)

def desenhar_botoes():
    """Desenha os quatro botões de resposta com texto numa linha, centrado."""
    pygame.draw.rect(ecra, PRETO, (x_esquerda-50, y_linha1-50, x_direita*1.53, ALTURA_BOTAO*3+ESP_VERTICAL))
    for i, rect in enumerate(botao_rects):
        # desenhar o botão (retângulo) com cantos arredondados
        pygame.draw.rect(ecra, cores_botoes[i], rect, border_radius=15)

        # desenhar o texto da resposta (uma linha)
        texto = respostas[i]
        sup_txt = fonte_resposta.render(texto, True, PRETO)
        rect_txt = sup_txt.get_rect(center=rect.center)
        ecra.blit(sup_txt, rect_txt)

# -------------------------------------------------------------
# CICLO PRINCIPAL
# -------------------------------------------------------------
running = True
while running:
    clock.tick(60)  # 60 fotogramas por segundo

    for event in pygame.event.get():
        # fechar a janela clicando no X (em modo janela)
        if event.type == pygame.QUIT:
            running = False
        # tecla ESC para sair do modo fullscreen
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # desenhar todos os elementos da interface
    desenhar_fundo()
    desenhar_barra_superior()
    desenhar_pergunta()
    desenhar_botoes()

    # atualizar o ecrã
    pygame.display.flip()

pygame.quit()
sys.exit()