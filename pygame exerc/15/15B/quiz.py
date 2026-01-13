import pygame
import sys
import csv
import random

# -------------------------------------------------------------
# 1. PREPARAÇÃO (SETUP)
# -------------------------------------------------------------
pygame.init()

# Detetamos o tamanho do ecrã para que o jogo se adapte a qualquer monitor
info = pygame.display.Info()
LARGURA = info.current_w
ALTURA = info.current_h

# Criamos a janela em modo ecrã inteiro (igual ao original)
ecra = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
pygame.display.set_caption("Quiz - Tecnologias da Informação")

clock = pygame.time.Clock()

# CORES (Mantivemos as cores originais que estavas a usar)
BRANCO   = (255, 255, 255)
PRETO    = (0, 0, 0)
VERMELHO = (220, 20, 60)
AZUL     = (30, 144, 255)
VERDE    = (34, 139, 34)
AMARELO  = (255, 215, 0)
CINZENTO_ESCURO = (20, 20, 20)

# FONTES (Tamanhos originais)
fonte_pergunta = pygame.font.Font(None, 52)
fonte_resposta = pygame.font.Font(None, 32)
fonte_info     = pygame.font.Font(None, 32)
fonte_final    = pygame.font.Font(None, 72)

# -------------------------------------------------------------
# 2. CARREGAMENTO DOS DADOS (O ficheiro .csv)
# -------------------------------------------------------------
def escolher_12_perguntas():
    """Esta função lê o ficheiro e escolhe 3 perguntas de cada nível."""
    todas = []
    # Abrimos o ficheiro para ler as informações
    with open('perguntas.csv', mode='r', encoding='utf-8') as f:
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

# -------------------------------------------------------------
# 3. A LÓGICA DO "TABULEIRO"
# -------------------------------------------------------------
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
terminou = False

# EXPLICAÇÃO DA LINHA ABAIXO:
# Estamos a pedir os dados da pergunta 0 (a primeira).
# Como a função 'buscar_dados_da_pergunta' nos traz um 'tabuleiro' com 3 itens,
# nós damos nomes a esses 3 itens imediatamente:
pergunta_agora, opcoes_agora, correta_agora = buscar_dados_da_pergunta(indice)



# -------------------------------------------------------------
# 4. DEFINIÇÃO DOS BOTÕES (Layout original)
# -------------------------------------------------------------
LARGURA_BOTAO = int(LARGURA * 0.35)
ALTURA_BOTAO  = int(ALTURA * 0.10)
ESP_VERTICAL  = int(ALTURA * 0.03)

y_linha1 = int(ALTURA * 0.45)
y_linha2 = y_linha1 + ALTURA_BOTAO + ESP_VERTICAL
x_esquerda = int(LARGURA * 0.10)
x_direita  = LARGURA - LARGURA_BOTAO - x_esquerda

botao_rects = [
    pygame.Rect(x_esquerda, y_linha1, LARGURA_BOTAO, ALTURA_BOTAO),
    pygame.Rect(x_direita,  y_linha1, LARGURA_BOTAO, ALTURA_BOTAO),
    pygame.Rect(x_esquerda, y_linha2, LARGURA_BOTAO, ALTURA_BOTAO),
    pygame.Rect(x_direita,  y_linha2, LARGURA_BOTAO, ALTURA_BOTAO),
]
cores_botoes = [AZUL, VERMELHO, VERDE, AMARELO]

# -------------------------------------------------------------
# 5. O CICLO DE JOGO (O Game Loop)
# -------------------------------------------------------------
while True:
    # A. Desenhar o fundo
    ecra.fill(CINZENTO_ESCURO)

    # B. Capturar o que o utilizador faz
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        # Detetar clique nas respostas
        if evento.type == pygame.MOUSEBUTTONDOWN and not terminou:
            pos_rato = pygame.mouse.get_pos()
            for i in range(4):
                if botao_rects[i].collidepoint(pos_rato):
                    # Se clicou na resposta certa, ganha ponto
                    if opcoes_agora[i] == correta_agora:
                        pontos += 1
                    
                    # Passar para a próxima pergunta
                    indice += 1
                    if indice < len(perguntas_do_jogo):
                        # Chamamos o 'estafeta' para trazer a nova pergunta
                        pergunta_agora, opcoes_agora, correta_agora = buscar_dados_da_pergunta(indice)
                    else:
                        terminou = True

    # C. DESENHAR A INTERFACE
    if not terminou:
        # Barra superior com info
        pygame.draw.rect(ecra, PRETO, (0, 0, LARGURA, 60))
        txt_barra = f"Pergunta: {indice + 1}/{len(perguntas_do_jogo)}   |   Acertos: {pontos}"
        img_barra = fonte_info.render(txt_barra, True, BRANCO)
        ecra.blit(img_barra, img_barra.get_rect(midtop=(LARGURA // 2, 15)))

        # Pergunta
        img_p = fonte_pergunta.render(pergunta_agora, True, BRANCO)
        ecra.blit(img_p, img_p.get_rect(center=(LARGURA // 2, int(ALTURA * 0.25))))

        # Botões
        for i in range(4):
            pygame.draw.rect(ecra, cores_botoes[i], botao_rects[i], border_radius=15)
            img_bt = fonte_resposta.render(opcoes_agora[i], True, PRETO)
            ecra.blit(img_bt, img_bt.get_rect(center=botao_rects[i].center))
    else:
        # Ecrã de Resultado Final (Percentagem)
        percentagem = (pontos / len(perguntas_do_jogo)) * 100
        txt_fim = f"RESULTADO: {percentagem:.0f}%"
        img_fim = fonte_final.render(txt_fim, True, AMARELO)
        ecra.blit(img_fim, img_fim.get_rect(center=(LARGURA // 2, ALTURA // 2)))

    # D. Atualizar ecrã
    pygame.display.flip()
    clock.tick(60)