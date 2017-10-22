# Test of The Trivia Game
# Chapter 3

import sys, pygame
from pygame.locals import *

total = 0
score = 0
current = 0
white = 255,255,255
green = 0,255,0


trivia_data = ("trivia_data.txt")
filename = trivia_data
f = open(filename, "r")
trivia_data = f.readlines()
f.close()
data = []
        #count and clean up trivia data
for text_line in trivia_data:
    data.append(text_line.strip())
    total += 1
    print(text_line)
        #get correct answer out of data (first)
correct = int(data[current+5])

print("correct ", correct)        
        

      
colors = [white,white,white,white]
colors[correct-1] = green
print("colors ", colors)
score += 1
     
if event.key == pygame.K_Q:
   print("You pressed Q")             



