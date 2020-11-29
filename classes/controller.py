''' Controller Class


'''

import pygame
from classes.map import Map
from classes.player import Player
from classes.npc import NPC
from classes.camera import Camera
from classes.background import Background

class Controller():
    def __init__(self, game_display, game_screen, screen_dims, colour):
        self.game_display = game_display
        self.game_screen = game_screen
        self.screen_dims = screen_dims
        self.colour = colour
        
        
    def play(self):
        self.generateMap()

    def generateMap(self):
        
        self.camera = Camera()
        self.background = Background(self.game_display)
        self.game_map = Map(self.game_display, self.screen_dims, 32)
        # Numbers will be changed to actual size later on
        self.player = Player(self.game_display, self.game_map, 100, 100)
        self.enemy = NPC(self.game_display, self.game_map, 600, 100, 'thorsten')

        self.enemy.addTarget(self.player)
        self.camera.addBack(self.background)
        self.camera.add(self.player)
        self.camera.add(self.enemy)
        self.camera.addMap(self.game_map)

        # Used to assign multiple targets to player
        # TODO: Put in function if/when we have more than one enemy
        #       on the board at any point in time
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self.enemy)


        self.player.addTarget(self.enemy_group)

    def keyboardInput(self, event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.startMove("u")
                if event.key == pygame.K_d:
                    self.player.startMove("r")
                if event.key == pygame.K_a:
                    self.player.startMove("l")
                if event.key == pygame.K_q:
                    self.player.attack()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.stopMove("right")
                elif event.key == pygame.K_a:
                    self.player.stopMove("left")

    def update(self):
        ''' Update function - Used to update positions of characters on 
            screen.

            This was initially encapsulated in the display function,
            however this caused issues when the map functions were 
            tracking characters.  This was due to the fact that some 
            changes to the characters position (such as due to gravity
            and recoil) were being applied after the map had updated.
            To avoid this, update functions were added to characters.
            These are called before we blit to the screen.

            @author: Robert
        '''
        # Updating player and enemy positions
        self.player.update()
        for enemy in self.enemy_group:
            enemy.update()

        # Update camera position
        self.camera.scroll()

    def display(self):

        # Colour screen purple
        self.game_display.fill(self.colour['purple'])

        # Display background and map
        self.background.displayQ()
        self.game_map.display()

        # Display characters
        self.player.display()
        for enemy in self.enemy_group:
            enemy.display()

        # scales the game_display to game_screen. Allows us to scale images
        scaled_surf = pygame.transform.scale(self.game_display, self.screen_dims)
        self.game_screen.blit(scaled_surf, (0, 0))

        # Camera variable to create camera movement