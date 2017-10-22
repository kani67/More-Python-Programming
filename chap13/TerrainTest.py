import sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *


class Terrain():
    def __init__(self, min_height, max_height, total_points):
        self.min_height = min_height
        self.max_height = max_height
        self.total_points = total_points+1
        self.grid_size = 800 / total_points
        self.height_map = list()
        self.height = (self.max_height + self.min_height) / 2
        self.height_map.append(self.height)
    
        for n in range(total_points ):
            self.height = random.randint(min_height, max_height)        
            self.height_map.append( int(self.height) )    
            
        
    def draw(self, surface):
        last_x = 0
        for n in range( 1, self.total_points ):
            #draw circle at current point
            self.height = 600 - self.height_map[n]
            x_pos = int(n * self.grid_size)
            pos = (x_pos, self.height)
            
            color = (255,255,255)
            pygame.draw.circle(surface, color, pos, 4, 1)
            last_height = 600 - self.height_map[n-1]
            last_pos = (last_x, last_height)
            pygame.draw.line(surface, color, last_pos, pos, 2)
            last_x = x_pos 
            
def game_init():
    global screen, backbuffer, font, timer, crosshair, crosshair_group, terrain

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    backbuffer = pygame.Surface((800,600))
    pygame.display.set_caption("Test terrain")
    font = pygame.font.Font(None, 30)
    timer = pygame.time.Clock()    
    terrain = Terrain(100, 120, 50)       

game_init()    

while True:   
    
    
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
    
    backbuffer.fill((20,20,120))

    #draw the terrain
    terrain.draw(backbuffer)
    
    screen.blit(backbuffer, (0,0))
    
    pygame.display.update()