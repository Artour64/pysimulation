import pygame
import events as ev
import world as w
pygame.init()
import render as r

world = w.World()
world.worldGen()
r.world=world
#world.print()
#print(world.grid)
r.renderInit()
'''
for x in world.grid:
	for y in x:
		print(str(y)+":"+str(y.entity))
'''


while ev.running:
	for event in pygame.event.get():
		ev.event(event)
	world.tick()
	r.renderTick()
    
