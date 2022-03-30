for i in range(int(cards_num /2)):
    CARD_NUM[i] = Cards(-260 + i*120, 170)
    CARD_NUM[i].onclick(CARD_NUM[i].flip_card)

    CARD_NUM[2*i] = Cards(-260 + i * 120, -100)
    CARD_NUM[2*i].onclick(CARD_NUM[2*i].flip_card)
if cards_num == 8:
    SCREEN.tracer(0)
    card_one = Cards(-270, 260)
    card_two = Cards(-270 + 120, 260)
    card_three = Cards(-270 + 120 * 2, 260)
    card_four = Cards(-270 + 120 * 3, 260)

    card_five = Cards(-270, 80)
    card_six = Cards(-270 + 120, 80)
    card_seven = Cards(-270 + 120 * 2, 80)
    card_eight = Cards(-270 + 120 * 3, 80)
    SCREEN.tracer(1)

    card_one.onclick(card_one.flip_card)
    card_two.onclick(card_two.flip_card)
    card_three.onclick(card_three.flip_card)
    card_four.onclick(card_four.flip_card)
    card_five.onclick(card_five.flip_card)
    card_six.onclick(card_six.flip_card)
    card_seven.onclick(card_seven.flip_card)
    card_eight.onclick(card_eight.flip_card)

if cards_num == 10:
    SCREEN.tracer(0)
    card_one = Cards(-270, 260)
    card_two = Cards(-270 + 120, 260)
    card_three = Cards(-270 + 120 * 2, 260)
    card_four = Cards(-270 + 120 * 3, 260)

    card_five = Cards(-270, 80)
    card_six = Cards(-270 + 120, 80)
    card_seven = Cards(-270 + 120 * 2, 80)
    card_eight = Cards(-270 + 120 * 3, 80)

    card_nine = Cards(-270, -120)
    card_ten = Cards(-270 + 120, -120)
    SCREEN.tracer(1)

if cards_num == 12:
    SCREEN.tracer(0)
    card_one = Cards(-270, 260)
    card_two = Cards(-270 + 120, 260)
    card_three = Cards(-270 + 120 * 2, 260)
    card_four = Cards(-270 + 120 * 3, 260)

    card_five = Cards(-270, 80)
    card_six = Cards(-270 + 120, 80)
    card_seven = Cards(-270 + 120 * 2, 80)
    card_eight = Cards(-270 + 120 * 3, 80)

    card_nine = Cards(-270, -100)
    card_ten = Cards(-270 + 120, -100)
    card_eleven = Cards(-270 + 120 * 2, -100)
    card_twelve = Cards(-270 + 120 * 3, -100)
    SCREEN.tracer(1)