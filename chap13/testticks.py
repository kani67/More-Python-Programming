import sys, time, random, math, pygame
from pygame.locals import *
from datetime import datetime, date, time

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))
    
 
  
#main program begins
pygame.init()
screen = pygame.display.set_mode((600,500))
font1 = pygame.font.Font(None, 24)
backbuffer = pygame.Surface((800,600))

white = 255,255,255
red = 220, 50, 50
yellow = 230,230,50
black = 0,0,0

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    
    timer = pygame.time.Clock()
    ticks = pygame.time.get_ticks()
    
    timer.tick(30)
    
    print_text(font1, 200, 200, "TICKS", red)
    
    pygame.draw.circle(screen,red, (400, 300), 40, 5)
    
    pygame.display.update()
    
    
    
    