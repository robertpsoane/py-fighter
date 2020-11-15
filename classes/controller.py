''' Controller Class


'''

import pygame
from classes.map import Map
from classes.player import Player
from classes.npc import NPC


class Controller():
    def __init__(self, game_screen, screen_dims):
        self.game_screen = game_screen
        self.screen_dims = screen_dims

    def generateMap(self):
        self.game_map = Map(self.game_screen, self.screen_dims)
        self.player = Player(self.game_screen, self.game_map, 600, 100)  #Numbers will be changed to actual size later on
        self.enemy = NPC(self.game_screen, self.game_map, 100, 100)
        self.enemy.addTarget(self.player)

    def keyboardInput(self, event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.startMove("u")
                if event.key == pygame.K_d:
                    self.player.startMove("r")
                if event.key == pygame.K_a:
                    self.player.startMove("l")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.stopMove("right")
                elif event.key == pygame.K_a:
                    self.player.stopMove("left")

    def display(self):
        self.game_map.generateMap()
        self.player.display()
        self.enemy.display()


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
