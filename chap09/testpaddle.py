import sys, time, random, math, pygame, LevelData
from pygame.locals import *
from MyLibrary import *

movex = 0

screen = pygame.display.set_mode((800,600))

class Game():
    
    def __init__(self):   
        pygame.init()
        
        pygame.display.set_caption("Katarina's Refactor Block Breaker Game")
        
        pygame.mouse.set_visible(False)
        
        self.font = pygame.font.Font(None, 36)
        
        

        self.window_alpha = pygame.Surface((800,600))
        self.window_alpha.fill((255,255,0))

        self.transp_alpha = 0
        self.timer = pygame.time.Clock()
        
        self.ticks = 0
        
        self.levels = LevelData.level_data()
        self.level = 0
        
        
        
        self.block_image = pygame.image.load("blocks.png").convert_alpha()
        self.block_group = pygame.sprite.Group()
        self.image = self.block_image
        self.x = 0
        self.y = 0
        self.bx =0
        self.by = 0
        self.num = 0
        
        
class Paddle():
    
    def __init__(self):
        
        self.paddle_group = pygame.sprite.Group()
        self.paddle = MySprite()
        self.paddle.load("paddle.png")
        self.paddle.position = 400, 540
        self.paddle_group.add(self.paddle)
        self.movex = 0
        self.waiting = True   
        
    def move_paddle(self):
        self.paddle_group.update(Game.ticks, 50)    
        
        
g = Game()
p = Paddle

while True:
    g.timer.tick(30)
    g.ticks = pygame.time.get_ticks()
  
    screen.fill((50,50,100))
   
    for event in pygame.event.get():
        if event.type == QUIT: 
            sys.exit()
           
    keys = pygame.key.get_pressed()
     
    if keys[K_ESCAPE]: 
        sys.exit()
    
     

    p.move_paddle()   
    p.paddle_group.draw(screen)
 
 
        