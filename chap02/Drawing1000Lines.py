# Drawing 1000 Lines
# Python 3.2
import sys
import pygame
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing 1000 Lines")

counter = 0
if counter < 101:
    while True:   
        for event in pygame.event.get():
        
            counter += 1
            if event.type in (QUIT, KEYDOWN):
                sys.exit()
        
    
            screen.fill((0,0,200))
    
        #draw the line
            color = 255,255,0
            width = 5
    
            x1 = random.randint(1, 550)
            y1 = random.randint(1, 450)
            x2 = random.randint(1, 550)
            y2 = random.randint(1, 450)
            pygame.draw.line(screen, color, (x1, y1), (x2 ,y2), width)
    
            pygame.display.update()
else:
    sys.exit()       
    