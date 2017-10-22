import sys, time, random, math, pygame, LevelData
from pygame.locals import *
from MyLibrary import *


levels = LevelData.level_data()

pygame.init()
screen = pygame.display.set_mode((800,600))

block_image = pygame.image.load("blocks.png")

block_group = pygame.sprite.Group()

block_group.empty() #reset block group

count = 0


level = 0
timer = pygame.time.Clock()

def load_level():
    global count
    
    for bx in range(0, 12):
        for by in range(0,10):
            count += 1
            
            block = MySprite()
            block.set_image(block_image, 58, 28, 4)
            x = 40 + bx * (block.frame_width+1)
            y = 60 + by * (block.frame_height+1)
            block.position = x,y

            #read blocks from level data
            num = levels[level][by*12+bx]
            block.first_frame = num-1
            block.last_frame = num-1
            if num > 0: #0 is blank
                print(count)
                block_group.add(block)

def update_blocks():
    block_group.update(ticks, 50)

load_level()
count = 0

while True:
    
    timer.tick(30)
    ticks = pygame.time.get_ticks()
    screen.fill((50,50,100))
    
    for event in pygame.event.get():
        if event.type == QUIT: 
            sys.exit()
    
    keys = pygame.key.get_pressed()

    if keys[K_ESCAPE]: 
        sys.exit()
    
    
    update_blocks()

    block_group.draw(screen)
    
    
    pygame.display.update()