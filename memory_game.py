"""
   CS5001
   Fall 2020
   Priyal Patel
   Final Project: Memory Game

   A program that implements a simple memory game with different card decks

   Helper files:
   memory_game_classes.py : contains all of the classes used in memory_game.py
   memory_game_functions.py : contains all of the functions used in memory_game.py
   
"""
from memory_game_functions import *


def main():
    # gets name of player
    get_player_name()

    # gets number of cards
    cards_num = get_num_of_cards()

    # gets name of card deck
    deck_name = get_deck_name()

    # create the background: playing area,leaderboard and status
    create_background()

    # click event that exits game when quit is clicked. A quit message pops up
    stop = QuitTurtle(250, -265)
    stop.onclick(stop.stop_game)

    # makes the turtles that will have shapes representing the cards
    make_cards(cards_num, deck_name)

    # if a click is on the card, the card is flip card
    SCREEN.onclick(find_pair)

    # the player's original stats are updated
    check_stats()

    mainloop()


if __name__ == "__main__":
    main()
