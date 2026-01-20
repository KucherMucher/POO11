import pygame
import sys
import csv
import random
from pygame import mixer


pygame.init()
mixer.init()

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
    img_fundo = pygame.image.load(r'Z:\11F\nao_tocas_grrrrr\forvscode\POO\pygame exerc\15\15_atual\assets\fundo_quiz.jpg') #Z:\\11F\\nao_tocas_grrrrr\\forvscode\POO\pygame exerc\\15\\2.jpg
    img_fundo = pygame.transform.scale(img_fundo, (LARGURA, ALTURA))
    usar_imagem_fundo = True

    # music: snak369 - day 369 in infinite ikea 
    background_music = mixer.music.load(r"assets\369.mp3")
    mixer.music.set_volume(0.3)
    mixer.music.play()

    #sounds
    
    good = mixer.Sound(r"assets\good.mp3")
    bad  = mixer.Sound(r"assets\bad.mp3")
    good_ending = mixer.Sound(r"assets\good_ending.mp3")
    bad_ending  = mixer.Sound(r"assets\bad_ending.mp3")
    
    sound_array = [good, bad, good_ending, bad_ending]

    for i in sound_array:
        i.set_volume(0.3)
    
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
fonte_final    = pygame.font.Font(None, 72)  # da pontuação final





# -------------------------------------------------------------
# DADOS DO QUIZ (EXEMPLO SIMPLES)
# -------------------------------------------------------------
def escolher_12_perguntas():
    """Esta função lê o ficheiro e escolhe 3 perguntas de cada nível."""
    todas = []
    # Abrimos o ficheiro para ler as informações
    with open(r'assets\perguntas.csv', mode='r', encoding='utf-8') as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            todas.append(linha)

    baralho_final = []
    # Para cada nível (1, 2, 3, 4), escolhemos 3 ao calhas
    for lvl in ["1", "2", "3", "4"]:
        daquele_nivel = [p for p in todas if p['Nível'] == lvl]
        if len(daquele_nivel) >= 3:
            escolhidas = random.sample(daquele_nivel, 3)
            baralho_final.extend(escolhidas)
        else:
            baralho_final.extend(daquele_nivel)
    
    return baralho_final

# Criamos a nossa lista de 12 perguntas
perguntas_do_jogo = escolher_12_perguntas()


def buscar_dados_da_pergunta(numero):
    """
    Esta função prepara o 'tabuleiro' para o jogo.
    Ela devolve 3 coisas: O Texto, as Opções e a Resposta Certa.
    """
    dados = perguntas_do_jogo[numero]
    texto = dados['Pergunta']
    correta = dados['Resposta Correta']
    
    # Criamos a lista com as 4 respostas e baralhamos a ordem
    opcoes = [dados['Resposta Correta'], dados['Resposta 2'], 
              dados['Resposta 3'], dados['Resposta 4']]
    random.shuffle(opcoes)
    
    return texto, opcoes, correta

# VARIÁVEIS DE CONTROLO
indice = 0
pontos = 0
finale = False

# EXPLICAÇÃO DA LINHA ABAIXO:
# Estamos a pedir os dados da pergunta 0 (a primeira).
# Como a função 'buscar_dados_da_pergunta' nos traz um 'tabuleiro' com 3 itens,
# nós damos nomes a esses 3 itens imediatamente:
pergunta_agora, opcoes_agora, correta_agora = buscar_dados_da_pergunta(indice)



num_pergunta = 1
total_perguntas = 12

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
    npergunta_info = f"Pergunta: {indice+1}/{total_perguntas}"
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
    pontuacao_info = f"Pontuação: {pontos}"

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
    sup_pergunta = fonte_pergunta.render(pergunta_agora, True, BRANCO)
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
        # desenhar o texto da resposta (uma linha)
        idealNewline = rect.width - 50
        texto = opcoes_agora[i]
        
        words = texto.split(" ")
        lines = []
        current = ""

        for w in words:
            test = current + w + " "
            if fonte_resposta.size(test)[0] > idealNewline:
                lines.append(current)
                current = w + " "
            else:
                current = test

        lines.append(current)

        
        center = rect.center
        
        lineHeight = 50
        totalTextHeight = len(lines) * lineHeight
        startY = center[1] - totalTextHeight // 2  # vertically center the block of lines

        for idx, line in enumerate(lines):
            sup_txt = fonte_resposta.render(line, True, BRANCO)
            rect_txt = sup_txt.get_rect(centerx=center[0])  # horizontally center
            rect_txt.y = startY + idx * lineHeight + 10       # vertical position
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

        #mixer control
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            mixer.music.set_volume(mixer.music.get_volume() + 0.05)
            for i in sound_array:
                i.set_volume(i.get_volume() + 0.05)
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            mixer.music.set_volume(mixer.music.get_volume() - 0.05)
            for i in sound_array:
                i.set_volume(i.get_volume() - 0.05)

        
        #
        if event.type == pygame.KEYDOWN and not finale:
            if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                num_pergunta+=1
                
                response = int(pygame.key.name(event.key))
                if opcoes_agora[response-1] == correta_agora:
                    good.play()
                    pontos += 1
                else:
                    bad.play()
                
                indice += 1
                if indice < len(perguntas_do_jogo):
                    pergunta_agora, opcoes_agora, correta_agora = buscar_dados_da_pergunta(indice)
                else:
                    finale = True
        if not finale:
            if indice == 0:
                cor = VERDE
            
            match (indice):
                case 3:
                    cor = AMARELO
                case 6:
                    cor = LARANJA
                case 9:
                    cor = VERMELHO
            desenhar_fundo()
            desenhar_pergunta_pontuacao(cor)
            desenhar_pergunta()
            desenhar_botoes()

        else:
            # Ecrã de Resultado Final (Percentagem)
            desenhar_fundo()
            percentagem = (pontos / len(perguntas_do_jogo)) * 100
            txt_fim = f"RESULTADO: {percentagem:.0f}%"
            img_fim = fonte_final.render(txt_fim, True, AMARELO)
            ecra.blit(img_fim, img_fim.get_rect(center=(LARGURA // 2, ALTURA // 2)))

            if percentagem < 50:
                bad_ending.play()
            else:
                good_ending.play()

    if mixer.music.get_busy() == False:
            mixer.music.play(start=1.56)

        
        
    

    # atualizar o ecrã
    pygame.display.flip()

mixer.quit()
pygame.quit()
sys.exit()
