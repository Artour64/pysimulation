import pygame
import numpy as np
import events as ev
pygame.init()

#GUI dimensions

worldX=32
worldY=24

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

#icon = pygame.image.load("snake-clip.png")
#pygame.display.set_icon(icon)
#screen.blit(icon, (50, 50))

def renderInit():
	screen.fill(bgcolor)
	renderGridBorder()
	pygame.display.update()

def renderGridBorder():
	for x in range(worldX):
		pygame.draw.line(screen,clrwhite,np.add(wc,(x*tileTotal,0)),np.add(wc,(x*tileTotal,yGridTotal)),1)
	for y in range(worldY):
		pygame.draw.line(screen,clrwhite,np.add(wc,(0,y*tileTotal)),np.add(wc,(xGridTotal,y*tileTotal)),1)
	pygame.draw.line(screen,clrwhite,np.add(wc,(0,yGridTotal)),np.add(wc,(xGridTotal,yGridTotal)),1)
	pygame.draw.line(screen,clrwhite,np.add(wc,(xGridTotal,0)),np.add(wc,(xGridTotal,yGridTotal)),1)
	
def renderTick():
	#text
	text = font.render("Hello Text", True, clrwhite)
	screen.blit(text, (10, 10))
	
	pygame.display.update()


renderInit()

while ev.running:
	for event in pygame.event.get():
		ev.event(event)
	renderTick()
    
