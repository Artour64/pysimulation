import pygame
import events as ev
import world as w
pygame.init()
import render as r

world = w.World()
world.worldGen()
r.world=world
r.renderInit()

while ev.running:
	for event in pygame.event.get():
		ev.event(event)
	world.tick()
	r.renderTick()
    
