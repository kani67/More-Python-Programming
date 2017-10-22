import sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *

class BlockSprite(pygame.sprite.Sprite):
    image = None

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        
        if BlockSprite.image is None:
            # This is the first time this class has been
            # instantiated. So, load the image for this and
            # all subsequence instances.
            BlockSprite.image = pygame.image.load("blocks.png")
        self.image = BlockSprite.image
        
        
        self.rect = self.image.get_rect()
        self.rect.topleft = location
        
pygame.init()
screen = pygame.display.set_mode([320, 320])
b = BlockSprite([0, 0]) # put the ball in the top left corner

screen = pygame.display.set_mode([320, 320])
b = BlockSprite([0, 0]) # put the ball in the top left corner
screen.blit(b.image, b.rect)
pygame.display.update()
while pygame.event.poll().type != KEYDOWN:
    pygame.time.delay(10)