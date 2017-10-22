import sys, random, time, pygame
from pygame.locals import *




pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Bomb Catching Game")
font1 = pygame.font.Font(None, 24)
pygame.mouse.set_visible(False)
white = 255,255,255
red = 220, 50, 50
yellow = 230,230,50
black = 0,0,0


clock_start = 0
mouse_x = mouse_y = 0

pos_x = 300
pos_y = 460

bomb_x = random.randint(0,500)
bomb_y = -50
#vel_y = 0.7
vel_y = 0.2
counter = 0


class Game():

    def __init__(self):    
        self.game_over = True
        self.mouse_x = self.mouse_y = 0
        self.pos_x = 300
        self.pos_y = 460
        self.seconds = 5
        self.clock_start = 0
        self.lives = 3
        self.score = 0
        self.button = " "
        self.event_type = " "
    
    def print_text(self, font, x, y, text, color=(255,255,255)):
        imgText = font.render(text, True, color)
        screen.blit(imgText, (x,y))
    
    def check_event(self):
        for event in pygame.event.get():
            
            
            if event.type == QUIT:
                self.even_type = event.type
                sys.exit()
            elif event.type == MOUSEMOTION:
                self.even_type = event.type
                self.mouse_x,self.mouse_y = event.pos
                self.move_x,self.move_y = event.rel
                  
            elif event.type == MOUSEBUTTONUP:
                if self.game_over:
                    self.game_over = False
                    self.lives = 3
                    self.score = 0
                          
        self.keys = pygame.key.get_pressed()
        
        if self.keys[K_ESCAPE]:
            sys.exit()
    
        screen.fill((0,0,100))
         



while True:
    
    playgame = Game()
    
    playgame.check_event()
   
    
    if playgame.game_over:
        playgame.print_text(font1, 100, 200, "<CLICK TO PLAY>", white) 
    else:
        bomb_y += vel_y
        
        #has the player missed the bomb?
        if bomb_y > 500:
            
            bomb_x = random.randint(0, 500)
            bomb_y = -50
            playgame.lives -= 1
            if playgame.lives == 0:
                playgame.game_over = True
        #see if player has caught the bomb
        elif bomb_y > pos_y:
            
            if bomb_x > pos_x and bomb_x < pos_x + 120:
                playgame.score += 10
                bomb_x = random.randint(0, 500)
                bomb_y = -50
        
        #draw the bomb
        
       
        pygame.draw.circle(screen, black, (bomb_x-4,int(bomb_y)-4), 30, 0)
        pygame.draw.circle(screen, yellow, (bomb_x,int(bomb_y)), 30, 0)
    
    
        #set basket position
        pos_x = mouse_x
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 500:
            pos_x = 500
        #draw basket

        pygame.draw.rect(screen, black, (pos_x-4,pos_y-4,120,40), 0)
        pygame.draw.rect(screen, red, (pos_x,pos_y,120,40), 0)

    #print # of lives
    playgame.print_text(font1, 0, 0, "LIVES: " + str(playgame.lives))

    #print score
    playgame.print_text(font1, 500, 0, "SCORE: " + str(playgame.score))
    #pygame.draw.circle(screen, yellow, (100,200), 30, 0)

    pygame.display.update()
             