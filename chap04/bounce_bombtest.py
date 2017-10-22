import sys, random, pygame, math
from pygame.locals import *

pos_x = 300
pos_y = 460
bomb_x = random.randint(0,500)
bomb_y = -50
vel_y = 0.1       
vel_x = 0.2
pos_y = 460

white = 255, 255, 255

mouse_x = mouse_y = 0


screen = pygame.display.set_mode((600,500))



while True:


	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		elif event.type == MOUSEMOTION:
			mouse_x, mouse_y = event.pos
			move_x, move_y = event.rel	
	
	keys = pygame.key.get_pressed()
	
	if keys[K_ESCAPE]:
		sys.exit()
	
	screen.fill((0,0,100))
	
	
	bomb_y += vel_y
	bomb_x += vel_x
	
	if bomb_y > 500:
		bomb_x = random.randint(0, 500)
		bomb_y = -50 
	elif bomb_y > pos_y:
		if bomb_x > mouse_x and bomb_x < mouse_x + 120:
			bomb_x = random.randint(0, 500) + vel_x
			bomb_y = -50     
			
	print("y ", bomb_y)
	print("x ", bomb_x)
	pygame.draw.circle(screen, white, (int(bomb_x),int(bomb_y)), 30, 0)
	
	pygame.display.update()
