"""
Other modules
import <module>
from <module...> import <object>
"""
from bigmodule.base import Base


class Deck(Base):
    num = 2

    def __init__(self, total_cards, faces):
        """Default initialize method

        """
        self.total_cards = total_cards
        self.faces = faces

        # Include base class implementation
        super().__init__(total_cards)

    def show(self):
        print(self.num, self.total_cards)
