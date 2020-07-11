import pygame
import events as ev
import world
pygame.init()
import render

world.worldGen()
#world.printworld()
#print(world.grid)
render.renderInit()
'''
for x in world.grid:
	for y in x:
		print(str(y)+":"+str(y.entity))
'''
while ev.running:
	for event in pygame.event.get():
		ev.event(event)
	world.tick()
	render.renderTick()
    
