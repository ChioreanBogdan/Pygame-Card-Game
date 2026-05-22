from entity import Entity

class Player(Entity):
    def __init__(self, name, hp=25):
        super().__init__(name,hp)

        # game zones
        self.hand = []
        self.deck = []
        self.graveyard = []