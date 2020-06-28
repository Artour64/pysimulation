import pygame
import numpy as np

pygame.init()

#GUI dimensions

worldX=32
worldY=16

tileSize=32
tileTotal=tileSize+1;

xGridTotal=worldX*tileTotal
yGridTotal=worldY*tileTotal

sizebartop=50
sizebarbottom=50
sizebarleft=50
sizebarright=50

wc=(sizebarleft,sizebartop)

screenX=xGridTotal+sizebarright+sizebarleft
screenY=yGridTotal+sizebartop+sizebarbottom

bgcolor=(50,50,50)
clrwhite=(255, 255, 255)
font = pygame.font.Font('freesansbold.ttf', 32)

screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Mytrix")

screen.fill(bgcolor)

#icon = pygame.image.load("snake-clip.png")
#pygame.display.set_icon(icon)
#screen.blit(icon, (50, 50))

def render():
	#background
	screen.fill(bgcolor)
	#grid
	for x in range(worldX):
		pygame.draw.line(screen,clrwhite,np.add(wc,(x*tileTotal,0)),np.add(wc,(x*tileTotal,yGridTotal)),1)
	for y in range(worldY):
		pygame.draw.line(screen,clrwhite,np.add(wc,(0,y*tileTotal)),np.add(wc,(xGridTotal,y*tileTotal)),1)
	pygame.draw.line(screen,clrwhite,np.add(wc,(0,yGridTotal)),np.add(wc,(xGridTotal,yGridTotal)),1)
	pygame.draw.line(screen,clrwhite,np.add(wc,(xGridTotal,0)),np.add(wc,(xGridTotal,yGridTotal)),1)
	
	#text
	text = font.render("Hello Text", True, (255, 255, 255))
	screen.blit(text, (10, 10))
	
	pygame.display.update()

running = True;
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False;
		# key control
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				print("Left key pressed")
			elif event.key == pygame.K_RIGHT:
				print("Right key pressed")
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				print("Left key released")
			elif event.key == pygame.K_RIGHT:
				print("Right key released")
	render()
    
