''' Controller Class


'''

import pygame
from classes.map import Map
from classes.player import Player
from classes.npc import NPC
from classes.camera import Camera
from classes.background import Background
from classes.text import Text
from screens.gameover import gameOver
from screens.pause import pauseScreen

class Controller():
    def __init__(self, game_display, game_screen, screen_dims, colour):
        self.run = True
        self.game_display = game_display
        self.game_screen = game_screen
        self.screen_dims = screen_dims
        self.colour = colour
        self.setupScore()
        self.initialGame()

    def setupScore(self):
        self.score_string = Text(self.game_screen, (100, 100), 20, 'Score = 0')

    def setupCameraMap(self):
        self.camera = Camera()
        self.background = Background(self.game_display)
        self.game_map = Map(self.game_display, self.screen_dims, 32)

    def setupPlayer(self):
        self.player = Player(self.game_display, self.game_map, 100, - 100)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

    def generateLevel(self):
        self.enemy = NPC(self.game_display, self.game_map, 600, - 100, 'thorsten')

        self.enemy.addTarget(self.player_group)
        self.camera.addBack(self.background)
        self.camera.add(self.player)
        self.camera.add(self.enemy)
        self.camera.addMap(self.game_map)

        # Used to assign multiple targets to player
        # TODO: Put in function if/when we have more than one enemy
        #       on the board at any point in time
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self.enemy)

        self.characters = pygame.sprite.Group()
        self.characters.add(self.player)
        for enemy in self.enemy_group:
            self.characters.add(enemy)

        self.player.addTarget(self.enemy_group)
    
    def resetPlayer(self):
        self.player.changeMap(self.game_map)
        self.player.center = 100, 100

    def initialGame(self):
        self.setupCameraMap()
        self.setupPlayer()
        self.generateLevel()

    def newGame(self):
        self.setupCameraMap()
        self.resetPlayer()
        self.generateLevel()
    
    def levelComplete(self):
        width, height = self.game_screen.get_width() // 2, self.game_screen.get_height() // 2
        level_complete1 = Text(self.game_screen, (width, height - 40), 30, 'Level Complete')
        level_complete2 = Text(self.game_screen, (width, height), 30, 'Press Space to continue')
        level_complete1.display()
        level_complete2.display()
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
                    waiting = False
                if event.type == pygame.QUIT:
                    waiting = False
                    self.run = False

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
                if event.key == pygame.K_ESCAPE:
                    self.player.updateState('idle', self.player.state[1])
                    self.player.x_y_moving = False
                    pauseScreen(self.game_screen)
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
        for character in self.characters:
            character.update()

        # Update camera position
        self.camera.scroll()

        if self.player.alive == False:
            gameOver()

        for enemy in self.enemy_group:
            if enemy.rect.bottom > self.screen_dims[1]:
                enemy.kill()
            if enemy.alive == False:
                self.camera.addWeapon(enemy.arms)
                enemy.kill()

        if len(self.enemy_group) == 0:
            self.levelComplete()
            self.newGame()

        self.score_string.text = f'Score = {self.player.score}'
        
        

    def display(self):

        # Colour screen purple
        self.game_display.fill(self.colour['purple'])

        # Display background and map
        self.background.displayQ()
        self.game_map.display()

        # Display characters
        for character in self.characters:
            character.display()

        # scales the game_display to game_screen. Allows us to scale images
        scaled_surf = pygame.transform.scale(self.game_display, self.screen_dims)
        self.game_screen.blit(scaled_surf, (0, 0))

        self.score_string.display()

        # Camera variable to create camera movement
