import sys
import pygame
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Drawing Lines")

color = 255, 255, 0
x1= 600
y1= 100
x2= 800
y2 = 100

x11 = 0
y11= 100
x22 = 200
y22= 100

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0,0,200))
        
    pygame.draw.line(screen, color, (x1 ,y1  ), (x2 , y2), 20)
    
    pygame.draw.line(screen, color, (x11 ,y11  ), (x22 , y22), 20)
    
    pygame.display.update()