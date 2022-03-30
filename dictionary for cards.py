card_position = {}
back_of_card = ['card_back.gif']
# populates a list of Cards(class)
while pairs_of_cards > 0:
    if counter % 4 == 0:
        y -= 180
        card = Cards(x + ((counter % 4) * 120), y,
                     final_cards[counter], back_of_card[0])
        card_position[card] = card.card_name

        # flips cards over
        # card_position[counter].onclick(card_position[counter].flip_card)

    else:
        card = Cards(x + ((counter % 4) * 120), y,
                     final_cards[counter], back_of_card[0])
        card_position[card] = card.card_name
        # flips cards over
        # card_position[counter].onclick(card_position[counter].flip_card)

    counter += 1
    pairs_of_cards -= 1
SCREEN.tracer(1)
print(card_position.keys())
print(card_position.values())