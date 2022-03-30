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

    def __eq__(self, other):
        if self.card_name == other.card_name:
            return True
        return False