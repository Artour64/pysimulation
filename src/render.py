import pygame
import world as w
import numpy as np

world=0#placeholder, set in main.py

tileSize=32
tileTotal=tileSize+1;

#icon = pygame.image.load("snake-clip.png")
#pygame.display.set_icon(icon)
#screen.blit(icon, (50, 50))

#defaults as placeholders, set in renderInit() 
xGridTotal=w.worldX*tileTotal
yGridTotal=w.worldY*tileTotal

sizebartop=50
sizebarbottom=50
sizebarleft=50
sizebarright=50

wc=(sizebarleft,sizebartop)
to=np.add(wc,(1,1))

screenX=xGridTotal+sizebarright+sizebarleft
screenY=yGridTotal+sizebartop+sizebarbottom

#icon = pygame.image.load("snake-clip.png")
#pygame.display.set_icon(icon)
#screen.blit(icon, (50, 50))

font = pygame.font.Font('freesansbold.ttf', 32)

screen=pygame.display.set_mode((screenX, screenY))#placeholder, set in renderInit()


bgcolor=(50,50,50)
clrwhite=(255, 255, 255)

def renderInit():
	global tileTotal
	global xGridTotal
	global yGridTotal
	global wc
	global to
	global screenX
	global screenY
	global screen
	
	tileTotal=tileSize+1;
	
	xGridTotal=world.worldX*tileTotal
	yGridTotal=world.worldY*tileTotal
	
	wc=(sizebarleft,sizebartop)
	to=np.add(wc,(1,1))

	screenX=xGridTotal+sizebarright+sizebarleft
	screenY=yGridTotal+sizebartop+sizebarbottom
	
	screen = pygame.display.set_mode((screenX, screenY))
	pygame.display.set_caption("Mytrix")

def renderTiles():
	for x in world.grid:#x is row
		for y in x:#y is tile
			renderTile(y)

def renderTile(t):
	for c in t.entity:
		image=pygame.image.load("src/images/entities/"+c.pic)
		cord=(t.x, t.y)
		cord=np.multiply(tileTotal,cord)
		cord=np.add(to,cord)
		screen.blit(image, cord)
		#print(c)

def renderFirst():
	screen.fill(bgcolor)
	renderGridBorder()
	renderTiles()
	pygame.display.update()

def renderGridBorder():
	for x in range(world.worldX):
		pygame.draw.line(screen,clrwhite,np.add(wc,(x*tileTotal,0)),np.add(wc,(x*tileTotal,yGridTotal)),1)
	for y in range(world.worldY):
		pygame.draw.line(screen,clrwhite,np.add(wc,(0,y*tileTotal)),np.add(wc,(xGridTotal,y*tileTotal)),1)
	pygame.draw.line(screen,clrwhite,np.add(wc,(0,yGridTotal)),np.add(wc,(xGridTotal,yGridTotal)),1)
	pygame.draw.line(screen,clrwhite,np.add(wc,(xGridTotal,0)),np.add(wc,(xGridTotal,yGridTotal)),1)
	
def renderTick():
	#text
	text = font.render("Hello Text", True, clrwhite)
	screen.blit(text, (10, 10))
	
	pygame.display.update()
