
import sys, time, random, math, pygame
from pygame.locals import *


pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Caption')
pygame.mouse.set_visible(0)

x = 50
y = 50
font = pygame.font.Font(None, 12)
event_text = "" 

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))
    
    


while True:

    

    #handle events
    for event in pygame.event.get():
       
        if event.type == KEYUP or event.type == KEYDOWN:
            event_text = str(event)
    
    
    
            
    keys = pygame.key.get_pressed()
    
    
    if keys[K_ESCAPE]:
        sys.exit()
    
    if event.type == QUIT:
        sys.exit()
                
    screen.fill((50,50,100))
  
    
    
    
    print_text(font,x, y, event_text)
    
    pygame.display.update()
    
    
   