import sys, math, getcolor, random, time
import pygame 
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))

vel = 0.05
count = 0

x1 = 200
y1 = 0
x2 = 150
y2 = 100

game_over = True
start_angle = math.radians(20)
end_angle = math.radians(60)
width = 8
font1 = pygame.font.Font(None, 24)
pos_y = 460

def print_text(font, x, y, text, color=(255,255,255)):
	imgText = font.render(text, True, color)
	screen.blit(imgText, (x,y))


while True:
	
	position = x1,y1,x2,y2
	
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		elif event.type == MOUSEBUTTONUP:
			if game_over:
				game_over = False
					
	keys = pygame.key.get_pressed()
	
	if keys[K_ESCAPE]:
		sys.exit()
	
	
	screen.fill((0,0,100)) 
	
	
	
	if game_over:
		print_text(font1, 100, 200, "<CLICK TO PLAY>") 
	else:
		y1 += vel
		
		
		if y1 > 460:
			y1 = 0
			y2 = 100
				
		color = getcolor.get_color("none" , True)
		
		
		
		pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
		
		

	pygame.display.update()