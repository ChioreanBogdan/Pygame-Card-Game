class Kanji:
    def __init__(self, symbol, meaning=None, on_readings=None, kun_readings=None):
        self.symbol = symbol

        # use [] if nothing provided
        self.meaning = meaning or []
        self.on = on_readings or []
        self.kun = kun_readings or []