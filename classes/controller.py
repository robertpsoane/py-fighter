''' Controller Class


'''

class Controller:
    def __init__():
        pass


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