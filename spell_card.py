from card import Card

class SpellCard(Card):
    def __init__(self, kanji, cost, x, y, font, effects):
        super().__init__(kanji, cost, x, y, font)

        self.effects = effects