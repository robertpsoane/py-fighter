''' Pyfighter (working title)

A Steampunk 2D streetfighting game built with PyGame.

[ More details to go here before release :), big it up and that! ]

Produced as an MSc Computer Science project by R. Soane,
S. Mistrey and R. Danevicius
'''

### Library Imports
import pygame
import json
from classes.displaystring import DisplayString

######################### DELETE WHEN PLAYER CLASS IS MADE ###################
player_image = pygame.image.load('graphics/char_idle/idler1.png')
##############################################################################

def pyfighterGame():
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

		# Refresh screen
		game_screen.fill(colour['blue'])

		### Code to re-display items on screen will go here ###


		######################### DELETE WHEN PLAYER CLASS IS MADE ###################
		game_screen.blit(player_image, (50, 50))

		##############################################################################
		# Flip to display
		pygame.display.flip()
