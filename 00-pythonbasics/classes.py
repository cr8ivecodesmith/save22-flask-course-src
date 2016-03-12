HELLO = 'WORLD'

class Base:
    def __init__(self, total_cards):
        """Default initialize method

        """
        self.total_cards = total_cards + 5
        # other initialize implementations


# Defines class
class Deck(Base):
    num = 2

    def __init__(self, total_cards, faces):
        """Overrides base class initialize method

        """
        self.total_cards = total_cards
        self.faces = faces

        # Include base class implementation
        super().__init__(total_cards)

    def show(self):
        print(self.num, self.total_cards)

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.faces)

"""
# Instantiates a class
cards = Deck(total_cards=5, faces='Spade')

# Use the class
cards.show()
print(cards.total_cards)
print(cards.faces)
"""
