from card import Card

class CreatureCard(Card):
    def __init__(self, kanji, cost, attack, hp, x, y, font):
        super().__init__(kanji, cost, attack, hp, x, y, font)

        self.hp = hp
        self.status_effects = []