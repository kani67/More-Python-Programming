import sys, pygame    
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 600))

font1 = pygame.font.Font(None, 40)
text = ""
def print_text(font, x, y, text, color= (255,255,0)):
    imgText = font.render(text,True, color)
    screen.blit(imgText, (x,y))



while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        keys = pygame.key.get_pressed()
    
        if keys[K_ESCAPE]:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key <= 256:
            text = (str(event.key) +  " " + str(chr(event.key)))
    screen.fill((0,0,200))    
    
    print_text(font1, 170, 440, text)
        
    pygame.display.update()
    