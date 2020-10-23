'''
Pyfighter Playground

A script for testing objects in isolation.
'''

### Library Imports
import pygame
import json
from classes.displaystring import DisplayString

######################### DELETE WHEN PLAYER CONTROLER CLASS IS MADE ###################
from pygame.locals import * # <<<<<<<FOR FUTURE REF KEYDOWN/KEYUP WONT WORK WIHTOUT THIS
########################################################################################

def pyfighterGame():

###################### DELETE WHEN PLAYER CONTROLER CLASS IS MADE #####################
	move_right = False
	move_left = False
	player_image = pygame.image.load('graphics/char_idle/idler1.png')
	player_gravity = 0
###################### DELETE WHEN PLAYER CONTROLER CLASS IS MADE #####################

	player_loc = [50,50]
	### Important Game Variables from JSON
	with open('json/config.JSON') as config_file:
		config = json.load(config_file)

	# Colour tuples and font sizes
	colour = config['colour']
	font_size = config['font_size']

	# Important screen variables
	screen_width = config['screen_dims'][0]
	screen_height = config['screen_dims'][1]
	max_fps = config['max_fps']
	game_name = config['game_name']

	### Setting up Screen and clock
	game_screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption(game_name)
	clock = pygame.time.Clock()

	### Setting up game loop
	run_me = True

	while run_me:
		# Limit frame rate
		clock.tick(max_fps)

		# Get/action events
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				# Detecting user pressing quit button, if X pressed,
				# break loop and quit screen.
				run_me = False

	############ TEMP MOVEMENT CONTROL FOR CHAR - REMOVE WHEN CHAR/CONTROL CLASS IS CREATED ######
			if event.type == KEYDOWN:
				if event.key == K_RIGHT:
					move_right = True
				if event.key == K_LEFT:
					move_left = True
			if event.type == KEYUP:
				if event.key == K_RIGHT:
					move_right = False
				if event.key == K_LEFT:
					move_left = False
	#############################################################################################

		# Refresh screen
		game_screen.fill(colour['blue'])

		### Code to re-display items on screen will go here ###


	############################# DELETE WHEN PLAYER CLASS IS MADE ###################
		game_screen.blit(player_image, player_loc)

		if player_loc[1] > screen_height-player_image.get_height():
			player_gravity = 0
		else:
			player_gravity += 0.15
		player_loc[1] += player_gravity


		if move_right == True:
			player_loc[0] += 4
		if move_left == True:
			player_loc[0] -= 4
	##################################################################################
		# Flip to display
		pygame.display.flip()


pyfighterGame()