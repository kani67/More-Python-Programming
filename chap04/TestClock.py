import sys, random, time, pygame
from pygame.locals import *

seconds = 10
clock_start = 0
count_seconds = 0
game_over = True
t = 0

pygame.init()

while True:
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x,mouse_y = event.pos
            move_x,move_y = event.rel
        elif event.type == MOUSEBUTTONUP:
            if game_over:          
                game_over = False
                lives = 3
                score = 0
                
        keys = pygame.key.get_pressed()
        
        if keys[K_ESCAPE]:
            sys.exit()
   


    
    if game_over:
        game_over = False
        seconds = 11
        clock_start = time.clock()

    t =  t + 1
    
    
    print("clock start " , clock_start)
    
    current = time.clock() - clock_start
    
    if t > 10:
        sys.exit()
   
   
    
    
   
    
    if seconds-current < 0:
        game_over = True
        print("game over")

    if game_over: 
        sys.exit()
        
        
   