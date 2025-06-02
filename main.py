import pygame
import random
from recursos.basicos import limparTela, aguarde
pygame.init()
print("kkkk")
comprimentoTela = 800
larguraTela = 600
larguraIron = 50
comprimentoIron = 330
tela = pygame.display.set_mode((comprimentoTela, larguraTela))
pygame.display.set_caption('Iron Man do Marcão')
relogio = pygame.time.Clock()
branco = (255, 255, 255)
preto = (0, 0, 0)
iron = pygame.image.load('assets/iron.png')
fundoJogo = pygame.image.load('assets/fundoJogo.png')
missel = pygame.image.load('assets/missile.png')
misselSound = pygame.mixer.Sound('assets/missile.wav')
posicaoXIron = 275
posicaoYIron = 400
movimentoXIron = 0
movimentoYIron = 0
velocidadeIron = 50
pygame.mixer_music.load('assets/ironsound.mp3')
pygame.mixer_music.play(-1)
posicaoXmissel = 100
posicaoYmissel = -250
velocidadeMissel = 1
pygame.mixer.Sound.play(misselSound)
pontos = 0
fonte = pygame.font.SysFont('comicsant', 18)
while True:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoXIron = -velocidadeIron  
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoXIron = velocidadeIron
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentoYIron = -velocidadeIron
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN: 
            movimentoYIron = velocidadeIron
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoXIron = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoXIron = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentoYIron = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoYIron = 0
    if posicaoXIron < 0:
        posicaoXIron = 0
    if posicaoXIron + larguraIron > larguraTela:
        posicaoXIron = larguraTela - larguraIron
    if posicaoYIron < 0:
        posicaoYIron = 0
    if posicaoYIron + comprimentoIron > comprimentoTela:
        posicaoYIron = comprimentoTela - comprimentoIron




    tela.fill(branco)
    tela.blit(fundoJogo, (0, 0))
    posicaoYmissel += velocidadeMissel
    if posicaoYmissel > 600:
        posicaoYmissel = -250
        pygame.mixer.Sound.play(misselSound)
        posicaoXmissel = random.randint(0, 800)
        velocidadeMissel += 1
        pontos += 1
    posicaoXIron = posicaoXIron + movimentoXIron
    posicaoYIron = posicaoYIron + movimentoYIron
    
    if iron.colliderect(missel):
        textoDerrota = fonte.render('Você perdeu!!', True, branco)
        tela.blit(textoDerrota, (400, 300))

    tela.blit(missel, (posicaoXmissel, posicaoYmissel))
    textoPontos = fonte.render(f'Pontos: {pontos}', True, branco)
    tela.blit(textoPontos, (10, 10))


    pygame.display.update()
    relogio.tick(60)
