from entity import Entity

class Player(Entity):
    def __init__(self, name, hp=25):
        super().__init__(hp)
        self.name = name

        # health
        self.hp = hp

        # future-proof
        self.status_effects = []

        # game zones
        self.hand = []
        self.deck = []
        self.graveyard = []