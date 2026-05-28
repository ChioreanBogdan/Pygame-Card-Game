from card import Card

class CreatureCard(Card):
    def __init__(self, kanji, cost, hp, x, y, font, attack=0):
        super().__init__(kanji, cost, hp, x, y, font)

        self.attack = attack