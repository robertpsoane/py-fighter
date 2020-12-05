''' Intro Screen

Providing a screen for the intro cut scene.

Used w3schools info on reading files:
https://www.w3schools.com/python/python_file_open.asp

'''

import pygame
import os

from classes.text import Text

story_location = 'other_data/intro_story.txt'

def introScreen(screen, controller):
    ''' Produces the intro cut scene based on star wars
    '''
    # Get important screen variables
    height = screen.get_height()
    width = screen.get_width()
    
    # Make story objects
    story = open(story_location, 'r')
    
    title = []
    main_story = []

    # Setup screen position
    x_position = width // 2
    title_y = height // 2 - 20
    main_y = height // 2
    # Extracting relevant text
    for line in story:
        if line[0:5] == 'TITLE':
            title_element = line[6:-1]
            title.append(
                Text(screen, (x_position, title_y), 40, title_element, 'blue')
            )
            title_y += 50
        elif line[0:4] == 'MAIN':
            main_element = line[5:-1]
            main_story.append(
                Text(screen, (x_position, main_y), 20, main_element, 'yellow')
            )
            main_y += 30

    title_count = 100
    
    # load clock
    clock = pygame.time.Clock()

    run_scene = True
    while run_scene:
        clock.tick(controller.clock_delay)

        # Get/action events
        for event in pygame.event.get():
            # Send each event to the start menu
            if event.type == pygame.QUIT:
                # Detecting user pressing quit button, if X pressed,
                # break loop and quit screen.
                run_scene = False
                controller.run = False
            elif (event.type == pygame.KEYDOWN) and \
                        (event.key == pygame.K_ESCAPE):
                run_scene = False
        
        screen.fill('black')

        if title_count > 0:
            for element in title:
                element.display()
                title_count -= 1
        else:
            for element in main_story:
                element.display()
                element.y -= 1

        if main_story[-1].y == 0:
            run_scene = False
       
        

        pygame.display.flip()
        
        