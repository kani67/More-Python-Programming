import sys, time, pygame
from pygame.locals import *

pygame.init()

timer = pygame.time.Clock()

ticks = pygame.time.get_ticks()
start_seconds = int(ticks) / 1000
seconds = 0
logfile = open("logfile.log" , "w")

while True:
    
    ticks = pygame.time.get_ticks()
    seconds = int(ticks) / 1000
    a = seconds - start_seconds
    text1 = "start " + str(a) + "\n"
    logfile.write(text1)
    if seconds - start_seconds > 10:
        
        start_seconds = int(ticks) / 1000
        text2 = "if statement " + str(seconds) + " " +  str(start_seconds) + "\n"
        
        logfile.write(text2)
    

logfile.close()