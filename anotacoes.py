import pygame

# criar a tela
tela = pygame.display.set_mode((1280, 720))

# desenhar figuras geometricas
pygame.draw.rect(tela, (255, 0, 0), (200, 300, 40, 50))
pygame.draw.circle(tela, (0, 0, 255), (400, 300), 40)
pygame.draw.line(tela, (255, 255, 0), (300, 0), (300, 720), 5)