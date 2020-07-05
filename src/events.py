import pygame
running=True
def event(event):
	if event.type == pygame.QUIT:
		global running
		running = False
	# key control
	if event.type == pygame.KEYDOWN:
		pass
		'''
		if event.key == pygame.K_LEFT:
			print("Left key pressed")
		elif event.key == pygame.K_RIGHT:
			print("Right key pressed")
		'''
	if event.type == pygame.KEYUP:
		pass
		
		if event.key == pygame.K_LEFT:
			print("Left key released")
		elif event.key == pygame.K_RIGHT:
			print("Right key released")
		
