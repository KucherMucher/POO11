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
VERMELHO = (220*0.9, 20*0.9, 60*0.9)
AZUL     = (30*0.9, 144*0.9, 255*0.9)
VERDE    = (34*0.9, 139*0.9, 34*0.9)
AMARELO  = (255*0.9, 215*0.9, 0)
CINZENTO_ESCURO = (20, 20, 20)
GREY_PURPLE = (50*0.9, 40, 100*0.8)
WGREY_PURPLE = (100, 85, 150)
GREY = (100*1.7, 105*1.6, 150*1.7)
BPURPLE = (30*0.8, 10*0.8, 70*0.8)
LARANJA  = (255*0.9, 115*0.9, 10*0.9)
# -------------------------------------------------------------
# IMAGEM DE FUNDO
# Colocar um ficheiro "fundo_quiz.jpg" na mesma pasta do código.
# Se não existir, o código usa um fundo de cor lisa.
# -------------------------------------------------------------
try:
    img_fundo = pygame.image.load("Z:\\11F\\nao_tocas_grrrrr\\forvscode\POO\pygame exerc\\15\\fundo_quiz.jpg") #Z:\\11F\\nao_tocas_grrrrr\\forvscode\POO\pygame exerc\\15\\2.jpg
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
fonte_resposta = pygame.font.Font(None, 52)  # texto das respostas
fonte_info     = pygame.font.Font(None, 32)  # pontuação e nº pergunta

# -------------------------------------------------------------
# DADOS DO QUIZ (EXEMPLO SIMPLES)
# -------------------------------------------------------------
num_pergunta = 1
total_perguntas = 10
pontuacao = 369

pergunta = "O que é um sistema operativo?"

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
    pygame.Rect(x_esquerda-30, y_linha1-30, LARGURA_BOTAO+70, ALTURA_BOTAO+90),
    pygame.Rect(x_direita-40,  y_linha1-30, LARGURA_BOTAO+70, ALTURA_BOTAO+90),
    pygame.Rect(x_esquerda-30, y_linha2-20, LARGURA_BOTAO+70, ALTURA_BOTAO+90),
    pygame.Rect(x_direita-40,  y_linha2-20, LARGURA_BOTAO+70, ALTURA_BOTAO+90),
]

# cor de cada botão (uma cor diferente)
cores_botoes = [VERMELHO, AZUL, AMARELO, VERDE]

# -------------------------------------------------------------
# FUNÇÕES DE DESENHO DA INTERFACE
# -------------------------------------------------------------
def desenhar_fundo():
    """Desenha a imagem de fundo ou uma cor lisa."""
    if usar_imagem_fundo:
        ecra.blit(img_fundo, (0, 0))
    else:
        ecra.fill(BRANCO)

def desenhar_pergunta_pontuacao(cor):
    """Desenha a barra superior com nº da pergunta e pontuação."""
    

    
    

    #nperguntas-----------------------------
    npergunta_info = f"Pergunta: {num_pergunta}/{total_perguntas}"
    sup_nper = fonte_info.render(npergunta_info, True, BRANCO)
    

    rect_nper = sup_nper.get_rect(center=(LARGURA // 2, int(ALTURA * 0.16)))

    size_npergunta = sup_nper.get_size()
    rect_npergunta = ((rect_nper.x-40, rect_nper.y-25), (size_npergunta[0]+80, size_npergunta[1]+100))

    rect_npersub = ((rect_nper.x-20, rect_nper.y-11), (size_npergunta[0]+40, size_npergunta[1]+20))
    
    pygame.draw.rect(ecra, GREY_PURPLE, rect_npergunta, border_radius=8)
    pygame.draw.rect(ecra, WGREY_PURPLE, rect_npersub, border_radius=5)


    pygame.draw.rect(ecra, GREY, rect_npergunta, width=3, border_radius=8)
    pygame.draw.rect(ecra, GREY, rect_npersub, width=2, border_radius=5)

    ecra.blit(sup_nper, rect_nper)

    #pontuação-------------------------
    pontuacao_info = f"Pontuação: {pontuacao}"

    sup_pon = fonte_info.render(pontuacao_info, True, BRANCO)

    rect_pon = sup_pon.get_rect(center=(int(LARGURA-350), int(ALTURA - 570)))

    size_pontuacao = sup_pon.get_size()
    rect_pontuacao = ((rect_pon.x-40, rect_pon.y-25), (size_pontuacao[0]+80, size_pontuacao[1]+80))

    rect_ponsub = ((rect_pon.x-20, rect_pon.y-11), (size_pontuacao[0]+40, size_pontuacao[1]+20))

    pygame.draw.rect(ecra, GREY_PURPLE, rect_pontuacao, border_radius=8)
    pygame.draw.rect(ecra, WGREY_PURPLE, rect_ponsub, border_radius=5)


    pygame.draw.rect(ecra, GREY, rect_pontuacao, width=3, border_radius=8)
    pygame.draw.rect(ecra, GREY, rect_ponsub, width=2, border_radius=5)

    
    ecra.blit(sup_pon, rect_pon)

    #barra de continuação
    altura_barra = 60
    pygame.draw.rect(ecra, BPURPLE, (0, 0, LARGURA, altura_barra))
    pygame.draw.rect(ecra, cor, (0, 0, num_pergunta * (LARGURA / total_perguntas), altura_barra))
    pygame.draw.line(ecra, GREY_PURPLE, (0, altura_barra), (LARGURA, altura_barra), width=3)

def desenhar_pergunta():
    """Desenha a pergunta em grande, centrada na parte superior."""
    sup_pergunta = fonte_pergunta.render(pergunta, True, BRANCO)
    rect_pergunta = sup_pergunta.get_rect(center=(LARGURA // 2, int(ALTURA * 0.25)))

    """Definir scale_rect da pergunta"""
    size_backpergunta = sup_pergunta.get_size()
    rect_backpergunta = ((rect_pergunta.x-50, rect_pergunta.y-50), (size_backpergunta[0]+100, size_backpergunta[1]+100))
    rect_frontpergunta = ((rect_pergunta.x-30, rect_pergunta.y-30), (size_backpergunta[0]+60, size_backpergunta[1]+60))

    
    
    """Desenha scale_rect"""
    pygame.draw.rect(ecra, GREY_PURPLE, rect_backpergunta, border_radius=15)
    pygame.draw.rect(ecra, WGREY_PURPLE, rect_frontpergunta, border_radius=10)

    #border
    pygame.draw.rect(ecra, GREY, rect_backpergunta, width=3, border_radius=15)
    pygame.draw.rect(ecra, GREY, rect_frontpergunta, width=2 ,border_radius=10)

    ecra.blit(sup_pergunta, rect_pergunta)

def desenhar_botoes():
    """Desenha os quatro botões de resposta com texto numa linha, centrado."""
    pygame.draw.rect(ecra, GREY_PURPLE, (x_esquerda-50, y_linha1-50, x_direita*1.53, ALTURA_BOTAO*3+ESP_VERTICAL+30), border_radius=30)
    pygame.draw.rect(ecra, GREY, (x_esquerda-50, y_linha1-50, x_direita*1.53, ALTURA_BOTAO*3+ESP_VERTICAL+30), width=3 ,border_radius=30)
    for i, rect in enumerate(botao_rects):
        # desenhar o botão (retângulo) com cantos arredondados
        pygame.draw.rect(ecra, cores_botoes[i], rect, border_radius=15)
        pygame.draw.rect(ecra, GREY, rect, width=2 ,border_radius=15)

        # desenhar o texto da resposta (uma linha)
        texto = respostas[i]
        textSize = sup_txt.get_size()
        if textSize[0] > 10:
            lenght = len(texto)
            respParte1 = slice(9,2) #ACABARRRRRRRRR
        print(textSize)
        sup_txt = fonte_resposta.render(texto, True, BRANCO)
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            num_pergunta += 1

    # desenhar todos os elementos da interface

    cor = BRANCO
    dificuldade = 2

    match dificuldade:
        case 1:
            cor = VERDE
        case 2:
            cor = AMARELO
        case 3:
            cor = LARANJA
        case 4:
            cor = VERMELHO
    desenhar_fundo()
    desenhar_pergunta_pontuacao(cor)
    desenhar_pergunta()
    desenhar_botoes()

    # atualizar o ecrã
    pygame.display.flip()

pygame.quit()
sys.exit()