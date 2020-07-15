import pygame
pygame.init()
import events as ev

import world as w
world = w.World()
#world.makeGrid(3,2)
world.worldGen()

import render as r
r.world=world
r.renderInit()
r.renderFirst()

while ev.running:
	for event in pygame.event.get():
		ev.event(event)
	world.tick()
	r.renderTick()
    
