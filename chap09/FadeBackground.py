import sys, time, random, math, pygame
from pygame.locals import *


pygame.init()

screen = pygame.display.set_mode((640, 480))
window_alpha = pygame.Surface((640,480))
window_alpha.fill((224,255,255))

window_alpha.set_alpha(1)

pygame.display.set_caption('Pygame fading')
#pygame.mouse.set_visible(0)
  
transp_alpha = 0




while True:
    
    screen.fill((0,0,255))
    
    transp_alpha += 0.1
    
    window_alpha.set_alpha(transp_alpha)
    window_alpha.fill((224,255,255))
    
    screen.blit(window_alpha,(0,0))
    
    for event in pygame.event.get():
            
        keys = pygame.key.get_pressed()
    
    if keys[K_ESCAPE]:
        sys.exit()
    
    if event.type == QUIT:
        sys.exit()
    
    
    

    pygame.display.update()