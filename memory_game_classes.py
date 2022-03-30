"""
   CS5001
   Fall 2020
   Priyal Patel
   Final Project: Memory Game


   Helper file that contains all of the classes used in memory_game.py

"""
from turtle import *
import time
import random
from copy import deepcopy
from memory_game_functions import *
import winsound

SCREEN = Screen()


class QuitTurtle(Turtle):
    """
    This is a class that is an object called turtle and is used for
    creating a quit button for the memory game

    Attributes:
        self.x: the x coordinates of the turtle's location
        self.y: the y coordinates of the turtle's location
    """

    def __init__(self, x=0, y=0):
        Turtle.__init__(self)
        self.x = x
        self.y = y
        self.hideturtle()
        self.up()
        self.goto(x, y)
        SCREEN.addshape("quitbutton.gif")
        self.shape("quitbutton.gif")
        self.showturtle()

    def stop_game(self, x, y):
        self.quit_message()
        time.sleep(3)
        quit()

    def quit_message(self):
        pop_up = Turtle()
        pop_up.hideturtle()
        pop_up.up()
        pop_up.goto(50, -50)
        SCREEN.addshape("quitmsg.gif")
        pop_up.shape("quitmsg.gif")
        pop_up.showturtle()


class Cards(Turtle):
    """
    This is a class that is an object called turtle and is used for
    creating cards for the memory game

    Attributes:
        self.flip: current state is set to flase, changed to true when the card is flipped
        self.x: the x coordinates of the card's location
        self.y: the y coordinates of the card's location
        self.card_name: the name of the image for the front of the card
        self.back_of_card: the name of the image for the back of the card
        self.hidden: current state is set to false, changed to true of turtle is hidden
    """

    def __init__(self, x=0, y=0, name='card_back.gif',
                 back_of_card='card_back.gif', flip=False, hidden=False):
        Turtle.__init__(self)
        self.flip = flip
        self.x = x
        self.y = y
        self.card_name = name
        self.back_of_card = back_of_card
        self.hidden = hidden
        self.hideturtle()
        self.up()
        self.goto(x, y)
        SCREEN.addshape(back_of_card)
        SCREEN.addshape(self.card_name)
        self.shape(back_of_card)
        self.showturtle()

    def flip_card(self, x_cord, y_cord, GAME_STATS):
        """
        A method that is in charge of 'flipping' the card. Whenever this method
        is called, the turtle's image is changed to the image assigned to the
        front of the card and the attributes self.flip is set to True.
        The x and y coordinates that are passed into the method are used to determine
        if the card has been clicked and the image change occurs.

        Parameters:
            x_cord: the x coordinate of where the player had clicked
            y_cord: the x coordinate of where the player had clicked

        Returns:
            None
        """
        if not self.hidden:
            left_card = self.x - 50
            right_card = self.x + 50
            top_card = self.y + 75
            bottom_card = self.y - 75

            # compares the x and y coordinates to determine if card was clicked
            if left_card <= x_cord <= right_card and top_card >= y_cord >= bottom_card:
                # plays a recording of card flipping
                winsound.PlaySound("card.wav", winsound.SND_FILENAME)
                self.shape(self.card_name)
                self.showturtle()
                self.flip = True

    def return_to_back(self):
        """
        A method that is in charge of 'flipping' the card back. Whenever this method
        is called, the turtle's image is changed to the original image assigned to the
        back of the card

        Parameters:
            None

        Returns:
            None
        """
        if not self.hidden:
            self.shape(self.back_of_card)
            self.showturtle()

    def __eq__(self, other):
        """
        A method that is compares to cards (objects) and determines if the card_name
        attributes are the same. If they are, true is returned. If they're not, false is returned.

        Parameters:
            None

        Returns:
            True if self.card_name and other.card_name are the same
            False if the names are different
        """
        if self.card_name == other.card_name:
            return True
        return False


class ImagePopUp(Turtle):
    """
    This is a class that is an object called turtle and is used for
    creating various turtles that change into their respective
    image depending on the warning/notification needed

    Attributes:
        self.image: the name of the .gif file passed through the class
    """

    def __init__(self, image):
        Turtle.__init__(self)
        self.image = image
        self.hideturtle()
        self.up()
        self.goto(50, -50)
        SCREEN.addshape(image)
        self.shape(image)
        self.showturtle()
        time.sleep(1.5)
        self.hideturtle()


class GameStats(Turtle):
    """
    This is a class keeps up with the stats of the game. It updates everything
    accordingly and allows for the player name and moves to be used for the
    status part of the memory game

    Attributes:
        self.player_name: the name of the player obtained from get_player_name()
        self.moves: updated every time the player clicks on a card
        self.matches: updated every time a pair of matching cards are found
        self.cards_created: a list of all Cards instances created to represent the cards
    """

    def __init__(self, player_name=0, moves=0, matches=0, cards_created=[]):
        Turtle.__init__(self)
        self.hideturtle()
        self.player_name = player_name
        self.moves = moves
        self.matches = matches
        self.cards_created = cards_created
