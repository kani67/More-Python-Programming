# Drawing Ellipses
# Python 3.2
import sys
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Ellipses")
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0,0,200))
    
    #draw an ellipse
    color = 255,255,0
    rect = [225, 150, 50, 100]
    width = 7
    pygame.draw.ellipse(screen, color, rect, width)
    #ellipse(Surface, color, Rect, width=0)
    #pygame.draw.ellipse(screen, red, [225, 10, 50, 20], 2)
    pygame.display.update()

