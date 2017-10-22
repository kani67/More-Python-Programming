import sys, time, random, math, pygame, LevelData
from pygame.locals import *
from MyLibrary import *



pygame.init()
screen = pygame.display.set_mode((800,600))

class Game():
    
    def __init__(self):
        
        self.levels = LevelData.level_data()
        self.block_image = pygame.image.load("blocks.png")
        self.block_group = pygame.sprite.Group()
        self.block_group.empty() #reset block group
        self.ticks = 0
        self.level = 0
        self.timer = pygame.time.Clock()
        self.x = 0
        self.y = 0
        self.block = MySprite()
        self.num = 0
        self.waiting = True
    
    
    def load_level(self):
        
        for bx in range(0, 12):
            for by in range(0,10):
                self.block = MySprite()
                self.block.set_image(self.block_image, 58, 28, 4)
                self.x = 40 + bx * (self.block.frame_width+1)
                self.y = 60 + by * (self.block.frame_height+1)
                self.block.position = self.x,self.y
                
            #read blocks from level data
                self.num = self.levels[self.level][by*12+bx]
                self.block.first_frame = self.num-1
                self.block.last_frame = self.num-1
                if self.num > 0: #0 is blank
                    self.block_group.add(self.block)

    def goto_next_level(self): 
        self.level += 1
        if self.level > len(self.levels)-1: 
            self.level = 0
        self.load_level()

    def update_blocks(self):
        #all blocks gone?
        if len(self.block_group) == 0: #all blocks gone?
            self.goto_next_level()   
            self.waiting = True
        self.block_group.update(self.ticks, 50)    



class Paddle():
    
    def __init__(self):
        
        self.paddle_group = pygame.sprite.Group()
        self.paddle = MySprite()
        self.paddle.load("paddle.png")
        self.paddle.position = 400, 540
        self.paddle_group.add(self.paddle)
        self.movex = 0
        self.movey = 0
        self.waiting = True   
        
    
    def move_mouse(self):
        
        for event in pygame.event.get():
            if event.type == QUIT: 
                sys.exit()
            elif event.type == MOUSEMOTION:
                self.movex,self.movey = event.rel
            elif event.type == MOUSEBUTTONUP:
                if self.waiting:
                    self.waiting = False
                #reset_ball()
            elif event.type == KEYUP:
                if event.key == K_RETURN: 
                    g.goto_next_level()
                    
    
    def pressed_keys(self):
        
        
        if keys[K_SPACE]:
            if self.waiting:
                self.waiting = False
            #reset_ball()
        elif keys[K_LEFT]: 
            self.paddle.velocity.x = -10.0
        elif keys[K_RIGHT]: 
            self.paddle.velocity.x = 10.0    
        else:
            if self.movex < -2: 
                self.paddle.velocity.x = self.movex
            elif self.movex > 2: 
                self.paddle.velocity.x = self.movex       
            else:
                self.paddle.velocity.x = 0    
          
        
            
    def move_paddle(self):
        
        self.paddle_group.update(g.ticks, 50)    
        self.pressed_keys()
                 
        self.paddle.X += self.paddle.velocity.x
    
        if self.paddle.X < 0: 
            self.paddle.X = 0
        elif self.paddle.X > 710: 
            self.paddle.X = 710    

    
        
             
g = Game()
p = Paddle()
g.load_level()

while True:
    
    g.timer.tick(30)
    g.ticks = pygame.time.get_ticks()
    

    p.move_mouse()
    
    #handle key presses
    keys = pygame.key.get_pressed()
    
    if keys[K_ESCAPE]: 
        sys.exit()

    screen.fill((50,50,100))

    
   
    g.update_blocks()
    
    
    
    g.block_group.draw(screen)
    
    p.move_paddle()
    p.paddle_group.draw(screen)
    
    
    
    
    pygame.display.update()