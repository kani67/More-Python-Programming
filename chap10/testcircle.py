import sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *


pygame.init()
screen = pygame.display.set_mode((800,600))

color = 10,10,20
radius = 60
color2 = 255,255,0 
x = 0.01
y = 0.02
xpos = 200
ypos = 200 
while True:
    screen.fill((50,50,100))
    
    
    
    
    
    
   
    
  
    
    
    xpos += x
    ypos += y
   
    
    pygame.draw.circle(screen, color, (int(xpos), int(ypos)), radius, 4)
    pygame.draw.circle(screen, color2, (int(xpos),int(ypos)), radius, 0)
    
    for event in pygame.event.get():
        if event.type == QUIT: 
            sys.exit()
    keys = pygame.key.get_pressed()
    
    if keys[K_ESCAPE]: 
        sys.exit()
    
    pygame.display.update()