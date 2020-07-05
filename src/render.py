import pygame
import world as w
import numpy as np
tileSize=32
tileTotal=tileSize+1;

#icon = pygame.image.load("snake-clip.png")
#pygame.display.set_icon(icon)
#screen.blit(icon, (50, 50))

xGridTotal=w.worldX*tileTotal
yGridTotal=w.worldY*tileTotal

sizebartop=50
sizebarbottom=50
sizebarleft=50
sizebarright=50

wc=(sizebarleft,sizebartop)

screenX=xGridTotal+sizebarright+sizebarleft
screenY=yGridTotal+sizebartop+sizebarbottom

#icon = pygame.image.load("snake-clip.png")
#pygame.display.set_icon(icon)
#screen.blit(icon, (50, 50))

font = pygame.font.Font('freesansbold.ttf', 32)

screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Mytrix")

bgcolor=(50,50,50)
clrwhite=(255, 255, 255)

bgcolor=(50,50,50)
clrwhite=(255, 255, 255)

def renderInit():
	screen.fill(bgcolor)
	renderGridBorder()
	pygame.display.update()

def renderGridBorder():
	for x in range(w.worldX):
		pygame.draw.line(screen,clrwhite,np.add(wc,(x*tileTotal,0)),np.add(wc,(x*tileTotal,yGridTotal)),1)
	for y in range(w.worldY):
		pygame.draw.line(screen,clrwhite,np.add(wc,(0,y*tileTotal)),np.add(wc,(xGridTotal,y*tileTotal)),1)
	pygame.draw.line(screen,clrwhite,np.add(wc,(0,yGridTotal)),np.add(wc,(xGridTotal,yGridTotal)),1)
	pygame.draw.line(screen,clrwhite,np.add(wc,(xGridTotal,0)),np.add(wc,(xGridTotal,yGridTotal)),1)
	
def renderTick():
	#text
	text = font.render("Hello Text", True, clrwhite)
	screen.blit(text, (10, 10))
	
	pygame.display.update()
