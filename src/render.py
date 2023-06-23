import pygame
import world as w
import numpy as np

import tileEnvironment as tenv

world=0#placeholder, set in main.py

showGrid = True
showGrid = False

tileSize=32
tileTotal=tileSize;
if showGrid:
	tileTotal += 1

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

sizebartop=0
sizebarbottom=0
sizebarleft=0
sizebarright=0

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
	
	#tileTotal=tileSize+1;
	
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

def renderTileOld(t):
	for c in t.entity:
		image=pygame.image.load("src/images/entities/"+c.pic)
		cord=(t.x, t.y)
		cord=np.multiply(tileTotal,cord)
		cord=np.add(to,cord)
		screen.blit(image, cord)
		#print(c)

def renderTileLite(t):
	image=pygame.image.load("src/images/tiles/"+t.env.type+".png")
	cord=(t.x, t.y)
	cord=np.multiply(tileTotal,cord)
	cord=np.add(to,cord)
	screen.blit(image, cord)

def renderTile(t):
	image=pygame.image.load("src/images/tiles/"+t.env.type+".png")
	cord=(t.x, t.y)
	cord=np.multiply(tileTotal,cord)
	cord=np.add(to,cord)
	screen.blit(image, cord)
	
	renderCorners(t, cord)
	
	renderAdjCorners(t)

def renderAdjCorners(t):
	offsets = (
		(0,1),(0,-1),(1,0),(-1,0)
		,(1,1),(-1,1),(1,-1),(-1,-1)
	)
	
	#offsets = []
	#for x in range(-5,5):
	#	for y in range(-5,5):
	#		offsets.append((x,y))
	
	for c in offsets:
		t1 = np.add((t.x,t.y),c)
		cord = t1
		cord=np.multiply(tileTotal,cord)
		cord=np.add(to,cord)
		t1=world.tileAt(t1[0],t1[1])
		renderCorners(t1, cord)
	

def renderCorners(t, cord):
	if t == None:
		return
	if t.env.type in tenv.corners:
		renderTileLite(t)
		renderTopLeftCorner(t, cord)
		renderTopRightCorner(t, cord)
		renderBottomRightCorner(t, cord)
		renderBottomLeftCorner(t, cord)

def getCorner(cord,s1,s2):
	global world
	
	t1 = np.add(cord,s1)
	t1 = world.tileAt(t1[0],t1[1])
	if t1 == None:
		return None
	
	t1 = t1.env.type
	if not t1 in tenv.corners:
		return None
	
	t2 = np.add(cord,s2)
	t2 = world.tileAt(t2[0],t2[1])
	if t2 == None:
		return None
		
	t2 = t2.env.type
	if t1 != t2:
		return None
	
	return t2

def renderTopLeftCorner(t,cord):
	corner = getCorner((t.x,t.y),(0,-1),(-1,0))
	if corner == None:
		return
	
	i0=pygame.image.load("src/images/corners/"+corner+".png")
	screen.blit(i0, cord)
	
def renderTopRightCorner(t,cord):
	global world
	corner = getCorner((t.x,t.y),(0,-1),(1,0))
	if corner == None:
		return
	
	t1 = (1,-1)
	t1 = np.add((t.x,t.y),t1)
	t1 = world.tileAt(t1[0],t1[1])
	if t1 != None:
		if t1.env.type == t.env.type:
			return
	
	i0=pygame.image.load("src/images/corners/"+corner+".png")
	i1=pygame.transform.rotate(i0,270)
	screen.blit(i1, cord)
	
def renderBottomRightCorner(t,cord):
	corner = getCorner((t.x,t.y),(0,1),(1,0))
	if corner == None:
		return
	
	i0=pygame.image.load("src/images/corners/"+corner+".png")
	i1=pygame.transform.rotate(i0,180)
	screen.blit(i1, cord)
	
def renderBottomLeftCorner(t,cord):
	global world
	corner = getCorner((t.x,t.y),(0,1),(-1,0))
	if corner == None:
		return
		
	t1 = (-1,1)
	t1 = np.add((t.x,t.y),t1)
	t1 = world.tileAt(t1[0],t1[1])
	if t1 != None:
		if t1.env.type == t.env.type:
			return
	
	i0=pygame.image.load("src/images/corners/"+corner+".png")
	i1=pygame.transform.rotate(i0,90)
	screen.blit(i1, cord)
	

def renderFirst():
	screen.fill(bgcolor)
	renderGridBorder()
	renderTiles()
	pygame.display.update()

def renderGridBorder():
	global showGrid
	if not showGrid:
		return
	for x in range(world.worldX):
		pygame.draw.line(screen,clrwhite,np.add(wc,(x*tileTotal,0)),np.add(wc,(x*tileTotal,yGridTotal)),1)
	for y in range(world.worldY):
		pygame.draw.line(screen,clrwhite,np.add(wc,(0,y*tileTotal)),np.add(wc,(xGridTotal,y*tileTotal)),1)
	pygame.draw.line(screen,clrwhite,np.add(wc,(0,yGridTotal)),np.add(wc,(xGridTotal,yGridTotal)),1)
	pygame.draw.line(screen,clrwhite,np.add(wc,(xGridTotal,0)),np.add(wc,(xGridTotal,yGridTotal)),1)
	
def renderTick():
	#text
	#text = font.render("Hello Text", True, clrwhite)
	#screen.blit(text, (10, 10))
	#renderTiles()
	pygame.display.update()
