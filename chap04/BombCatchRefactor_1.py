# Bomb Catcher Game
# Chapter 4

import sys, random, time, pygame, getcolor, tokenize
from pygame.locals import *

screen = pygame.display.set_mode((600,500))
                    
                    
class Game():
    
    def __init__(self):    
        pygame.display.set_caption("Bomb Catching Game")
        self.game_over = True
        self.mouse_x = self.mouse_y = 0
        self.pos_x = 300
        self.pos_y = 460
        self.seconds = 5
        self.clock_start = 0
        pygame.init()
        pygame.mouse.set_visible(False)
        self.lives = 3
        self.score = 0
        self.check_where = False
        
    def print_text(self, font, x, y, text, color):     
        imgText = font.render(text, True, color)  
        screen.blit(imgText, (x,y))
        
        
    def get_font1(self):
        pygame.font.init()
        self.font1 = pygame.font.Font(None, 24)
        font1 = self.font1
        return font1

    
    def check_event(self):
        for event in pygame.event.get():       
            if event.type == QUIT:
                sys.exit()
            elif event.type == MOUSEMOTION:
                self.mouse_x, self.mouse_y = event.pos
                self.move_x, self.move_y = event.rel
            elif event.type == MOUSEBUTTONUP:
                if self.game_over:
                    self.game_over = False
                    self.score = 0
                    self.lives = 3
                    
        self.keys = pygame.key.get_pressed()
            
        if self.keys[K_ESCAPE]:
            sys.exit()
        
        
            
class Bomb():
    def __init__(self):
        self.miss_flag = False
        self.pos_x = 300
        self.pos_y = 460
        self.bomb_x = random.randint(0,500)
        self.bomb_y = -50
        self.vel_y = 0.1       
        self.seconds = 3    
        self.clock_start = 0
        
    def draw_bomb(self): 
        
        black = getcolor.get_color("black", False)
        yellow = getcolor.get_color("yellow", False)
        
        pygame.draw.circle(screen, black, (self.bomb_x-4,int(self.bomb_y)-4), 30, 0)
        pygame.draw.circle(screen, yellow, (self.bomb_x,int(self.bomb_y)), 30, 0)
            
    def catch_bomb(self, playgame, x_pos):
        self.bomb_y += self.vel_y      
    
        if self.bomb_y > 500:   
            self.miss_flag = True       
            self.bomb_x = random.randint(0, 500)
            self.bomb_y = -50
            playgame.lives -= 1
            self.seconds = 4
            self.clock_start = time.clock()
            if playgame.lives == 0:
                playgame.game_over = True
        elif self.bomb_y > self.pos_y:  
            
            self.miss_flag = False
            
            if self.bomb_x > x_pos and self.bomb_x < x_pos + 120:           
                playgame.score += 10
                self.bomb_x = random.randint(0, 500)
                self.bomb_y = -50     

    def show_boom(self, playgame, missed):
        red = getcolor.get_color("red", False)
        
        
        if missed:
            current = time.clock() - self.clock_start       
            
            if self.seconds - current > 0:
                playgame.print_text(font1, 250, 200, "BOOM!" , red) 
            elif self.seconds - current < 0:
                self.miss_flag = False
        
            self.bomb_x = random.randint(0, 500)
            self.bomb_y = -50                       



class Basket():
    #set basket position
    def basket_pos(self, x_pos):    
        self.pos_x = x_pos
        self.pos_y = 460
        if self.pos_x < 0:
            self.pos_x = 0
        elif self.pos_x > 500:
            self.pos_x = 500
    
    def draw_basket(self):        
        black = getcolor.get_color("black", False)
        red = getcolor.get_color("red", False)#draw basket
        pygame.draw.rect(screen, black, (self.pos_x-4,self.pos_y-4,120,40), 0)
        pygame.draw.rect(screen, red, (self.pos_x,self.pos_y,120,40), 0)

    
    

def main():
    
    while True:
        
        screen.fill((0,0,100)) 
        white = getcolor.get_color("white", False)
        playgame.check_event()
       
               
        if  playgame.game_over:                   
            playgame.print_text(font1, 100, 200, "<CLICK TO PLAY>", white)
            
        else:   
            
            missed = start_bomb.miss_flag      
            
            if not missed:
                start_bomb.draw_bomb()
              
            x_pos = playgame.mouse_x      
            start_bomb.catch_bomb(playgame,x_pos)  
            
            
            
            
            start_basket.basket_pos(x_pos)    
            start_basket.draw_basket()
            
           
            
            start_bomb.show_boom(playgame, missed)   
             
        
        playgame.print_text(font1, 0, 0, "LIVES: " + str(playgame.lives), white)

    #print score
        playgame.print_text(font1, 500, 0, "SCORE: " + str(playgame.score), white)
        pygame.display.update()
 
playgame =  Game()
font1 = playgame.get_font1()
start_bomb = Bomb()  
start_basket = Basket()    
main()    

