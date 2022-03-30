from memory_game_functions import *
from turtle import *
from PositionService import *
import time
from classes import *

WIDTH = HEIGHT = 1600
SCREEN = Screen()
CARD_WIDTH = 120
CARD_HEIGHT = 170


CARD_NUM = []

from turtle import *
import time
import random

SCREEN = Screen()
CARDS = ['2_of_clubs.gif', '2_of_diamonds.gif', 'jack_of_spades.gif',
         '3_of_hearts.gif', 'ace_of_diamonds.gif', 'king_of_diamonds.gif',
         'queen_of_hearts.gif']


class QuitTurtle(Turtle):
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
    def __init__(self, x=0, y=0):
        Turtle.__init__(self)
        self.x = x
        self.y = y
        self.hideturtle()
        self.up()
        self.goto(x, y)
        SCREEN.addshape("card_back.gif")
        self.shape("card_back.gif")
        self.showturtle()

    def flip_card(self, x, y):
        card = random.randint(0, 6)
        SCREEN.addshape(CARDS[card])
        self.shape(CARDS[card])
        self.showturtle()



def create_background():
    SCREEN.screensize(WIDTH, HEIGHT)
    draw_playing_area()
    draw_status_area()
    draw_leader_board()


def draw_rectangle(board, short, long):
    for i in range(2):
        board.forward(short)
        board.right(90)
        board.forward(long)
        board.right(90)


def draw_playing_area():
    board = Turtle()
    create_individual_space(board, "black", -330, 380, 500, 585)


def open_scoreboard(turtle, row, column):
    with open("leaderboard.txt", 'r') as infile:
        for score in infile:
            turtle.up()
            column -= 30
            turtle.goto(row, column)
            turtle.down()
            turtle.write(score.strip(), font=("Verdana",
                                              10, "normal"))


def draw_leader_board():
    leader = Turtle()
    create_individual_space(leader, "blue", 200, 380, 200, 585)
    leader.up()
    leader.goto(220, 344)
    leader.write("Leaders:", font=("Verdana",
                                   12, "normal"))
    open_scoreboard(leader, 220, 344)


def draw_status_area():
    status = Turtle()
    create_individual_space(status, "black", -330, -240, 500, 50)


def create_individual_space(turtle, pen_color, x, y, short, long):
    turtle.hideturtle()
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.pencolor(pen_color)
    turtle.pensize(5)
    draw_rectangle(turtle, short, long)






def main():
    # gets player's name
    player = SCREEN
    player_name = player.textinput("CS5001 Memory", "Your Name:")
    if player_name is None:
        quit()

    # gets number of cards
    cards = SCREEN
    cards_num = cards.numinput("Set Up", "# of Cards to Play: (8, 10, or 12)",
                               maxval=12, minval=8)
    if cards_num is None:
        quit()

    # keeps asking for cards if card number is 9 or 11
    while cards_num == 9 or cards_num == 11:
        cards_num = cards.numinput("Set Up", "# of Cards to Play: "
                                             "(8, 10, or 12)", maxval=12,
                                   minval=8)
        if cards_num is None:
            quit()

    # creates the initial background for game
    create_background()

    # click event that exits game when quit is clicked. A quit message pops up
    stop = QuitTurtle(250, -265)
    stop.onclick(stop.stop_game)

    card_position = int(cards_num)
    x = -270
    y = 440
    counter = 0
    SCREEN.tracer(0)
    while card_position > 0:
        if counter % 4 == 0:
            y -= 180
            CARD_NUM.append(Cards(x + ((counter % 4) * 120), y))
        else:
            CARD_NUM.append(Cards(x + ((counter % 4) * 120), y))
        counter += 1
        card_position -= 1

    SCREEN.tracer(1)

    score_dict = {"moves": 0, "matches": 0}
    score = Turtle()
    score.hideturtle()
    score.up()
    score.goto(-320, -285)
    score.write(("Status   {} : moves   {} : matches".format(score_dict['moves']
                ,score_dict['matches'])), font=(12))
    mainloop()

def get_deck_name():
    # gets player's name
    deck = SCREEN
    deck_name = deck.textinput("Pick a deck of cards", "Original or Dogs:")
    while deck_name.lower() != "dogs" and deck_name.lower() != "original":
        deck_name = deck.textinput("Pick a deck of cards", "Original or Dogs:")

    if deck_name is None:
        quit()
    if deck_name.upper() == 'DOGS':
        return DOGS
    if deck_name.upper() == 'ORIGINAL':
        return ORIGINAL

    # gets name of deck of cards
    deck_name = get_deck_name()

    from turtle import *
    import time
    import random
    from copy import deepcopy

    SCREEN = Screen()

    class QuitTurtle(Turtle):
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

        def flip_card(self, x_cord, y_cord):
            if self.hidden == False:
                left_card = self.x - 50
                right_card = self.x + 50
                top_card = self.y + 75
                bottom_card = self.y - 75

                if x_cord >= left_card and x_cord <= right_card and y_cord <= top_card and y_cord >= bottom_card:
                    self.shape(self.card_name)
                    self.showturtle()
                    self.flip = True

        def return_to_back(self, x=0, y=0):
            if self.hidden == False:
                self.shape(self.back_of_card)
                self.showturtle()

    class Winner(Turtle):
        def __init__(self):
            Turtle.__init__(self)
            self.hideturtle()
            self.up()
            self.goto(50, -50)
            SCREEN.addshape("winner.gif")
            self.shape("winner.gif")
            self.showturtle()
            time.sleep(1)
            quit()

    class Leaderboard(Turtle):
        def __init__(self):
            Turtle.__init__(self)
            self.hideturtle()
            self.up()
            self.goto(50, -50)
            time.sleep(5)
            SCREEN.addshape("leaderboard_error.gif")
            self.shape("leaderboard_error.gif")
            self.showturtle()
            time.sleep(3)
            self.hideturtle()


main()
