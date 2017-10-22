import sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *


 


screen = pygame.display.set_mode((12*64,9*64))                                 
                              
                            
backbuffer = pygame.Surface((screen.get_rect().width, screen.get_rect().height))

class Food(MySprite):
    def __init__(self):
        MySprite.__init__(self)
        self.image = pygame.Surface((16,16)).convert_alpha()
        self.image.fill((255,255,255,0))
        pygame.draw.circle(self.image, (250,250,50), (8,8), 8, 0)
        self.set_image(self.image)
        MySprite.update(self, 0, 30) #create frame image
        self.food_x = random.randint(0,23) * 16
        self.food_y = random.randint(0,17) * 16

    def create_food(self):
        self.food_group = pygame.sprite.Group()
    
        self.food_group.add(food)    

class Game():
   
    def __init__(self):
        pygame.init()
        self.x = 0
        self.y = 0

        self.white = 255,255,255
        self.yellow = 250,250,250
        self.width = 64
        self.height = 64


food = Food()


game = Game()


while True:
    
    backbuffer.fill((20,50,20)) 
    screen.blit(backbuffer, (0,0))
    
    
    food.create_food()  
    
    
    food.food_group.draw(screen)
    
    for event in pygame.event.get():
        if event.type == QUIT: 
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: 
        sys.exit()

      
    
    
    for rx in range(0, 12):
        
        for ry in range(0,9):
            game.x = rx * (game.width)
            game.y = ry * (game.height)
            
            pygame.draw.rect(screen, (game.white), (game.x,game.y, game.width, game.height), 1)
            
         
    
    
    
    
    #backbuffer.fill((20,50,20)) 
    
    
    #screen.blit(backbuffer, (0,0))
    
    
    
            
    pygame.display.update()                                