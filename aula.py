import pygame
from pygame.locals import *
from sys import exit
from random import randint

# iniciar as funções e variáveis da biblioteca pygame
pygame.init()

pygame.mixer.music.set_volume(0.3)
musica_de_fundo = pygame.mixer.music.load("sounds/background music.mp3")
pygame.mixer.music.play(-1)

som_colisao = pygame.mixer.Sound("sounds/som_colisao.wav")  # todos os arquivos além da musica de fundo, devem ter extensao .wav

# criar a tela e suas dimensões
largura_tela = 1280
altura_tela = 720
posicao_x = int(largura_tela/2)
posicao_y = int(altura_tela/2)
x_verde = randint(0, 1240)
y_verde = randint(0, 670)
vida = 5

fonte = pygame.font.SysFont("arial", 40, bold=True)

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("The legend of Jonathan")

relogio = pygame.time.Clock()

while True:
    mensagem = f"Vida: {vida}"
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    
    # controlar a framerate do jogo
    relogio.tick(165)

    # atualizar a tela para manter o fundo sempre preto
    tela.fill((0, 0, 0))

    # detectar eventos dentro do jogo, como jogador apertar uma tecla
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                posicao_x -= 20
            if event.key == K_d or event.key == K_RIGHT:
                posicao_x += 20
            if event.key == K_w or event.key == K_UP:
                posicao_y -= 20
            if event.key == K_s or event.key == K_DOWN:
                posicao_y += 20'''

    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        posicao_x -= 6
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        posicao_x += 7
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
        posicao_y -= 7
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
        posicao_y += 7

    # dsenhar um retângulo na tela: ("lugar onde ele vai ser criado", "cor", "'pos_x', 'pos_y', 'comprimento', 'largura_tela'")
    retangulo_vermelho = pygame.draw.rect(tela, (255, 0, 0), (posicao_x, posicao_y, 40, 50))
    retangulo_verde = pygame.draw.rect(tela, (0, 255, 0), (x_verde, y_verde, 40, 50))

    if retangulo_vermelho.colliderect(retangulo_verde):
        x_verde = randint(0, 1240)
        y_verde = randint(0, 670)
        vida -= 1
        som_colisao.play()

        if vida == 0:
            pygame.quit()
            exit()

    if posicao_x >= largura_tela:
        posicao_x = 0
    elif posicao_x <= 0:
        posicao_x = largura_tela

    if posicao_y >= altura_tela:
        posicao_y = 0
    elif posicao_y <= 0:
        posicao_y = altura_tela

    tela.blit(texto_formatado, (50, 40))

    # atualizar a tela do jogo a cada iteração do loop principal
    pygame.display.update()