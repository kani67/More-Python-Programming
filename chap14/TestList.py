import sys, time, random, math, pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((700,650))
class Inventory():

    def __init__(self): 
    
        self.font1 = pygame.font.SysFont("Courier New", size=18, bold=True)
        self.font2 = pygame.font.SysFont("Courier New", size=14, bold=True)
        self.inventory_list = ["leather   ", "sword   ", "plate male   " , "cloth   "]
        self.inv_len = 0
        self.imgText = ""
        self.inv_pos_x = 50

    def print_text(self, font, x, y, text, color=(255,255,255), target=None): #CHANGE
        self.imgText = font.render(text, True, color)
        screen.blit(self.imgText, (x,y))
                
    def print_inventory(self):
        str1 = ''.join(self.inventory_list)
         
        
        self.print_text(self.font2, 50, 590, str1)
               


while True:
    
    i = Inventory()
    screen.fill((0,0,100))
    
    for event in pygame.event.get():
        if event.type == QUIT: 
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE: 
                sys.exit()


    i.print_inventory()

    
    pygame.display.update()