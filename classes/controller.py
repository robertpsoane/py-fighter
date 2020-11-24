''' Controller Class


'''

import pygame
from classes.map import Map
from classes.player import Player
from classes.npc import NPC
from classes.camera import Camera
from classes.background import Background

class Controller():
    def __init__(self, game_display, game_screen, screen_dims):
        self.game_display = game_display
        self.game_screen = game_screen
        self.screen_dims = screen_dims
        self.camera = Camera()


    def generateMap(self):

        self.background = Background(self.game_display)
        self.game_map = Map(self.game_display, self.screen_dims, 32)
        self.player = Player(self.game_display, self.game_map, 600, 100)  #Numbers will be changed to actual size later on
        self.enemy = NPC(self.game_display, self.game_map, 100, 100, 'thorsten')

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
                    #self.camera.cameraMove("r")
                if event.key == pygame.K_a:
                    self.player.startMove("l")
                   #self.camera.cameraMove("l")
                if event.key == pygame.K_q:
                    self.player.attack()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.stopMove("right")
                elif event.key == pygame.K_a:
                    self.player.stopMove("left")


    def display(self):

        self.camera.scroll()
        self.background.displayP()
        self.game_map.display()
        self.player.display()
        self.enemy.display()

        # scales the game_display to game_screen. Allows us to scale images
        scaled_surf = pygame.transform.scale(self.game_display, self.screen_dims)
        self.game_screen.blit(scaled_surf, (0, 0))

        # Camera variable to create camera movement


'''
functions to code:

note: all functions have parameter self, but when calling function you don't
pass self
Functions with an asterisk - use the name I've given (__init__ is a default python
name, and display for consistency)

*__init__() - function which runs when you initialise an instance of the
            class.
            Needs to take input of screen, and screen dims

generateMap() - function which makes an instance of map, background, player,
                npc etc at the beginning of a room

*display()  - calls display on all objects.  should call controller.display() in
            the game loop for each iteration, this function displays everything
            to the screen

keyboardInput() - called in the for loop in the game loop - initially used only
                to control player, takes keyboard input and processes it


Note - player is the class for the player, however you can call all methods in
        character on player (eg you can do player.startMove('l'))

Feel free to write any other functions in the class to help make the
 controller more useable etc


'''
