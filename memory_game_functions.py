"""
   CS5001
   Fall 2020
   Priyal Patel
   Final Project: Memory Game


   Helper file that contains all of the functions used in memory_game.py

"""
from turtle import *
import time
from memory_game_classes import *
import winsound

DEFAULT = ['2_of_clubs.gif', '2_of_diamonds.gif', 'jack_of_spades.gif',
           '3_of_hearts.gif', 'ace_of_diamonds.gif', 'king_of_diamonds.gif',
           'queen_of_hearts.gif']

GAME_STATS = GameStats()

WIDTH = HEIGHT = 1600
CARD_WIDTH = 120
CARD_HEIGHT = 170


def get_player_name() -> None:
    """
    Creates a dialog box to get the player's name. Is stored in a class attribute

    Parameters:
        None

    Return:
        None
    """
    player = SCREEN
    player_name = player.textinput("CS5001 Memory", "Your Name:")
    if player_name is None:
        quit()
    GAME_STATS.player_name = player_name


def get_num_of_cards() -> int:
    """
    Creates a dialog box to get the number of cards. The options are:
    8, 10, or 12 cards. If the number of cards picks is 9 or 11, the
    number is defaulted to the next even number in line. An image
    pops up to warn player of the change in game.

    Parameters:
        None

    Return:
        card_num (int): number of cards needed for playing
    """
    cards = SCREEN
    cards_num = cards.numinput("Set Up", "# of Cards to Play: (8, 10, or 12)",
                               maxval=12, minval=8)
    if cards_num is None:
        quit()

    # makes changes to card_num if 9 or 11 is entered
    if cards_num == 9 or cards_num == 11:
        ImagePopUp('card_warning.gif')
        if cards_num == 9:
            cards_num = 10
        else:
            cards_num = 12

    if cards_num is None:
        quit()
    return cards_num


def get_deck_name() -> list:
    """
    opens a file called memory.cfg and reads the file into a list.
    If the file is missing or does not exist, the default deck is used,

    Parameters:
        None

    Return:
        deck: a list of image names stored as strings
    """
    deck = []
    try:
        with open("memory.cfg", 'r') as infile:
            for card_in_deck in infile:
                deck.append(card_in_deck.strip())
            if len(deck) < 6:
                FileWarning()
                quit()
            return deck
    except FileNotFoundError:
        ImagePopUp('file_error.gif')
        deck = DEFAULT
        return deck


def create_background() -> None:
    """
    Creates the background of the game by calling specific functions.
    The screen is opened up to full screen mode when the background is made.

    Parameters:
        None

    Return:
        None
    """
    SCREEN.screensize(WIDTH, HEIGHT)
    SCREEN.setup(width=1.0, height=1.0)
    draw_playing_area()
    draw_status_area()
    draw_leader_board()


def draw_rectangle(turtle: object, short: int, long: int) -> None:
    """
    Creates the appropriate rectangle according to the dimensions specified

    Parameters:
        turtle: passes an object that draws the rectangle
        short: the width of the rectangle
        long: the length of the rectangle

    Return:
        None
    """
    for i in range(2):
        turtle.forward(short)
        turtle.right(90)
        turtle.forward(long)
        turtle.right(90)


def draw_playing_area() -> None:
    """
    Passes the dimensions needed for where the cards will be placed
    to create_individual_space

    Parameters:
        None

    Return:
        None
    """
    board = Turtle()
    board.speed(10)
    create_individual_space(board, "black", -330, 380, 500, 585)


def open_scoreboard(turtle: object, row: int, column: int) -> None:
    """
    Opens a file called leaderboard.txt and writes out the player's names and their scores
    on the leaderboard. If the file does not exist, an image pops up and the leaderboard is
    left empty. Scores are not kept for that round.

    Parameters:
        turtle: an object that writes the player's stats
        row and column: passed to give the turtle a starting point on where to begin writing

    Return:
        None
    """
    try:
        with open("leaderboard.txt", 'r') as infile:
            for player in infile:
                turtle.up()
                column -= 30
                turtle.goto(row, column)
                turtle.down()
                turtle.write(player.strip(), font=("Verdana", 10, "normal"))

    except FileNotFoundError:
        ImagePopUp('leaderboard_error.gif')


def draw_leader_board() -> None:
    """
    Passes the dimensions needed for where the leader board will be
    to create_individual_space

    Parameters:
        None

    Return:
        None
    """
    leader = Turtle()
    leader.speed(10)
    create_individual_space(leader, "blue", 200, 380, 200, 585)
    leader.up()
    leader.goto(220, 344)
    leader.write("Leaders:", font=("Verdana",
                                   12, "normal"))

    # calls a function that writes the player's name on the leader board
    open_scoreboard(leader, 220, 344)


def draw_status_area() -> None:
    """
    Passes the dimensions needed for where player's stats are kept
    to create_individual_space

    Parameters:
        None

    Return:
        None
    """
    status = Turtle()
    status.speed(10)
    create_individual_space(status, "black", -330, -240, 500, 50)


def create_individual_space(turtle: object, pen_color: str, x: int, y: int,
                            short: int, long: int) -> None:
    """
    Passes the dimensions to rectangle to determine where to make the rectangle
    and how big to make it

    Parameters:
        turtle: object needed to draw rectangle
        pen_color: changes color of ink according the rectangle
        x: x coordinate of where turtle needed to go to draw the rectangle
        y: y coordinate of where turtle needed to go to draw the rectangle

    Return:
        None
    """
    turtle.hideturtle()
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.pencolor(pen_color)
    turtle.pensize(5)
    draw_rectangle(turtle, short, long)


def make_cards(cards_num: int, deck_name: list) -> None:
    """
    Creates a deck of cards the size of cards_num and uses images stored in the list deck_name:
    The deck of cards made a pairs of cards that are stored in a new list in the
    class game stats attribute

    Parameters:
        cards_num: the number of cards the player picked to play with
        deck_name: a list of image names

    Return:
        None
    """

    # calls a function to make the pairs of each card picked
    final_cards = make_duplicates(cards_num, deck_name)
    num_of_cards = int(cards_num)
    card_x = -270
    card_y = 440
    SCREEN.tracer(0)
    GAME_STATS.cards_created = []
    make_deck(final_cards, num_of_cards, card_x, card_y)
    SCREEN.tracer(1)


def make_duplicates(cards_num: int, deck_name: list) -> list:
    """
    Makes the pairs for each card picked

    Parameters:
        cards_num: the number of cards the player picked to play with
        deck_name: a list of image names

    Return:
        final_cards: card pairs stored in random indices
    """
    # creates duplicate names of cards based on number of cards picked
    duplicate_cards = []
    for i in range(len(deck_name)):
        duplicate_cards.append(deck_name[i])
    random.shuffle(duplicate_cards)

    # creates pairs of each card
    final_cards = []
    for i in range(int(cards_num / 2)):
        final_cards.append(duplicate_cards[i])
        final_cards.append(duplicate_cards[i])
    random.shuffle(final_cards)
    return final_cards


def make_deck(final_cards, num_of_cards, card_x, card_y):
    """
    Makes the instances of Cards and stores them in a list. The instances of Cards
    are turtles which are in the image of the back of the cards and are used to
    place the 'cards' in the correct arrangement based on the number of cards picked
    by the player. The x and y coordinates of where the turtles need to go are
    used to create rows and columns for the cards

    Parameters:
        num_of_cards: the number of cards the player picked to play with
        final_cards: card pairs stored in random indices
        GAME_STATS.cards_created: a game stats attribute used to store the instances of Cards
        card_x: the card's center x coordinate
        card_y: the card's center y coordinate

    Return:
        None
    """
    counter = 0
    back_of_card = ['card_back.gif']
    # populates a list of Cards(class) and arranges cards on board
    while num_of_cards > 0:
        # makes the columns
        if counter % 4 == 0:
            card_y -= 180
            GAME_STATS.cards_created.append(
                Cards(card_x + ((counter % 4) * 120), card_y,
                      final_cards[counter],
                      back_of_card[0]))

        # makes the rows
        else:
            GAME_STATS.cards_created.append(
                Cards(card_x + ((counter % 4) * 120), card_y,
                      final_cards[counter],
                      back_of_card[0]))

        counter += 1
        num_of_cards -= 1


def find_pair(x_cord: int, y_cord: int) -> None:
    """
    Whenever the player clicks on the screen, a function called onclick passes x and y coordinates
    to this function to determine if the place clicked is within the dimensions of the card.
    If the click was within the card's dimensions, the Card attributes are changed accordingly.
    If a click is made on the card, gamestats attribute moves is updated and a pair matched
    updates the gamestats matches.

    Parameters:
        x_cord: x coordinate for player's click on screen
        y_cord: y coordinate for player's click on the screen

    Return:
        None
    """
    # used to keep track of two cards
    card_pair = []

    for i in range(len(GAME_STATS.cards_created)):
        # calls the flip card method for Cards to determine if card should be flipped
        GAME_STATS.cards_created[i].flip_card(int(x_cord), int(y_cord), GAME_STATS)

        flipped_card = GAME_STATS.cards_created[i].flip
        if flipped_card:
            card_pair.append(i)

        if len(card_pair) == 2:
            GAME_STATS.moves += 1
            if GAME_STATS.cards_created[card_pair[0]].card_name == \
                    GAME_STATS.cards_created[card_pair[1]].card_name:
                update_card_attributes(card_pair)
                break

            else:
                card_pair = original_card_attributes(card_pair)

    # clears status and updates according to recent moves and matches
    GAME_STATS.clear()
    check_stats()
    if GAME_STATS.matches == (len(GAME_STATS.cards_created)) / 2:
        # if a player is found, the leaderboard is updated and the game quits
        update_player_name()

        # plays a sound recording if player wins
        winsound.PlaySound("victory.wav", winsound.SND_FILENAME)
        ImagePopUp('winner.gif')
        quit()


def update_card_attributes(card_pair: list) -> None:
    """
    A function to update the various attributes of the class Cards if a match is found

    Parameters:
        card_pair: a list that contains the indices of the card pairs clicked on

    Return:
        None
    """
    # prevents card from flipping again
    GAME_STATS.cards_created[card_pair[0]].flip = False
    GAME_STATS.cards_created[card_pair[1]].flip = False
    time.sleep(0.5)
    GAME_STATS.cards_created[card_pair[0]].hideturtle()
    GAME_STATS.cards_created[card_pair[1]].hideturtle()
    # keeps card hidden
    GAME_STATS.cards_created[card_pair[0]].hidden = True
    GAME_STATS.cards_created[card_pair[1]].hidden = True
    GAME_STATS.matches += 1


def original_card_attributes(card_pair: list) -> None:
    """
    A function to update the various attributes of the class Cards if a match is not found

    Parameters:
        card_pair: a list that contains the indices of the card pairs clicked on

    Return:
        None
    """
    # makes sure card is returned to back images
    GAME_STATS.cards_created[card_pair[0]].flip = False
    GAME_STATS.cards_created[card_pair[1]].flip = False
    time.sleep(1)
    # changes turtle image to back of image
    GAME_STATS.cards_created[card_pair[0]].return_to_back()
    GAME_STATS.cards_created[card_pair[1]].return_to_back()
    card_pair = []
    return card_pair


def check_stats() -> None:
    """
    A function that updates the status portion of the game

    Parameters:
        None

    Return:
        None
    """
    GAME_STATS.up()
    GAME_STATS.goto(-320, -285)

    GAME_STATS.write("Status:   guesses: {}   matches: {}".format(
        int(GAME_STATS.moves), GAME_STATS.matches), font=12)


def update_player_name():
    """
    A function to update the player's final score by calling and function called remove_lowest_player
    and writes the updated leaderboard list to the file leaderboard.txt

    Parameters:
        None

    Return:
        None
    """
    try:
        player_list = remove_lowest_player(GAME_STATS.moves,
                                           GAME_STATS.player_name)
        with open("leaderboard.txt", 'w') as scores:
            for i in range(len(player_list)):
                scores.write(f"{player_list[i][0]} : {player_list[i][1]}")
                scores.write("\n")

    except FileNotFoundError:
        pass


def remove_lowest_player(points: int, name: str) -> list:
    """
    A function that opens a file called leaderboard.txt and reads the information
    line by line into a list. The scores of the previous players are stored in another list
    and the player's current score is compared to the previous list. If the previous player
    list has more than 6 players and the player's scores are higher than the name in 6th place
    or higher, the name and score in position 6 is removed. The updated list of names is returned,


    Parameters:
        points: the moves stored in gamestats attribute moves
        name: the player's name stored in the gamestats attribute player_name

    Return:
        player_score_tracker: a list of player names and their respective scores
    """
    player_score_tracker = []

    # creates a list of previous players
    lowest_player = open("leaderboard.txt", "r")
    for line in lowest_player:
        player_score_tracker.append(line.strip().replace(":", "").split())

    # creates a list of only scores
    score_tracker = []
    for i in range(len(player_score_tracker)):
        score_tracker.append(player_score_tracker[i][0])

    # if player scores are less than any of the other scores, the index is saved
    minimum_index = len(score_tracker) - 1
    for j in range(len(score_tracker) - 1, -1, -1):
        if points < int(score_tracker[j]):
            minimum_index = j

    # if previous player's list has less than 6 names, player's stats are added
    if len(player_score_tracker) < 6:
        player_score_tracker.insert(minimum_index, [points, name])

    # removes lowest player in list and adds player's stats to the correct index
    else:
        if points < int(score_tracker[len(score_tracker) - 1]):
            player_score_tracker.insert(minimum_index, [points, name])
            player_score_tracker.pop()

    return player_score_tracker
