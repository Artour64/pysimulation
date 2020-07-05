import pygame
import events as ev
import world
pygame.init()
import render

render.renderInit()

while ev.running:
	for event in pygame.event.get():
		ev.event(event)
	render.renderTick()
    
