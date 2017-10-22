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
        self.game_over = False
        self.font = pygame.font.Font(None, 36)
        self.window_alpha = pygame.Surface((800,600))
        self.window_alpha.fill((224,255,255))
        self.transp_alpha = 0
    
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
        
        
    
    def move_mouse(self):
        
        for event in pygame.event.get():
            if event.type == QUIT: 
                sys.exit()
            elif event.type == MOUSEMOTION:
                self.movex,self.movey = event.rel
            elif event.type == MOUSEBUTTONUP:
                if g.waiting:
                    g.waiting = False
                    b.reset_ball()
            elif event.type == KEYUP:
                if event.key == K_RETURN: 
                    g.goto_next_level()
                    
    
    def pressed_keys(self):
        
       
        if keys[K_SPACE]:
            if g.waiting:
                g.waiting = False
                b.reset_ball()
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

    
class Ball():
    
    def __init__(self):
        self.ball = MySprite()
        self.ball_group = pygame.sprite.Group()
       
        self.ball.load("ball.png")
        self.ball.position = 400,300
        self.ball_group.add(self.ball)
        
        
        self.lives = 4       
        self.score = 0
        
        self.bx = 0
        self.by = 0
        self.px = 0
        self.py = 0
        
    def move_ball(self):
        self.ball_group.update(g.ticks, 50)    
    
        if g.waiting:        
            self.ball.X = p.paddle.X + 40
            self.ball.Y = p.paddle.Y - 20
           
    
        self.ball.X += self.ball.velocity.x
        self.ball.Y += self.ball.velocity.y
        
        
        if self.ball.X < 0:
            print("2")
            self.ball.X = 0
            self.ball.velocity.x *= -1
        elif self.ball.X > 780:
            print("3")
            self.ball.X = 780
            self.ball.velocity.x *= -1
        if self.ball.Y < 0:
            print("4")
            self.ball.Y = 0
            self.ball.velocity.y *= -1
        elif self.ball.Y > 580:
            print("5") #missed paddle
            g.waiting = True
            self.lives -= 1
            if self.lives < 1:
                g.game_over = True
        
                
    def collision_ball_paddle(self):
        
        if pygame.sprite.collide_rect(self.ball, p.paddle):
            self.ball.velocity.y = -abs(self.ball.velocity.y)
            self.bx = self.ball.X + 8
            self.by = self.ball.Y + 8
            self.px = p.paddle.X + p.paddle.frame_width/2
            self.py = p.paddle.Y + p.paddle.frame_height/2
        
        if self.bx < self.px: #left side of paddle?
            self.ball.velocity.x = -abs(self.ball.velocity.x)
        else: #right side of paddle?
            self.ball.velocity.x = abs(self.ball.velocity.x)
    
    
    
    
    def reset_ball(self):
        self.ball.velocity = Point(4.5, -7.0)
          
g = Game()
p = Paddle()
b = Ball()
g.load_level()



while True:
    
    g.timer.tick(30)
    g.ticks = pygame.time.get_ticks()
    

    p.move_mouse()
    
    #handle key presses
    keys = pygame.key.get_pressed()
    
    if keys[K_ESCAPE]: 
        sys.exit()
    
    if not g.game_over:
        g.update_blocks()
        p.move_paddle()
        b.move_ball()
        b.collision_ball_paddle()
        #collision_ball_blocks()
    
    screen.fill((0,0,255))


    g.transp_alpha += 1
    g.window_alpha.set_alpha(g.transp_alpha)
    screen.blit(g.window_alpha,(0,0))    
   
    
    g.block_group.draw(screen)
    
    p.paddle_group.draw(screen)
    
    b.ball_group.draw(screen)
    
    print_text(g.font, 0, 0, "SCORE " + str(b.score))
    print_text(g.font, 200, 0, "LEVEL " + str(g.level+1))
    print_text(g.font, 400, 0, "BLOCKS " + str(len(g.block_group)))
    print_text(g.font, 670, 0, "BALLS " + str(b.lives))
    
    if g.game_over:
        print_text(g.font, 300, 380, "G A M E   O V E R")
    
    pygame.display.update()
    