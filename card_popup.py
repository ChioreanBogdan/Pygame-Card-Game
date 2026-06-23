import pygame  # import the library

class CardPopup:
    def __init__(self):
        self.active = False
        self.card = None

    def open(self, card):
        self.active = True
        self.card = card

    def close(self):
        self.active = False
        self.card = None

    def handle_event(self, event):
        pass

    def draw(self, screen):
        if not self.active:
            return

        pygame.draw.rect(screen, (200, 200, 200), (200, 100, 400, 300))