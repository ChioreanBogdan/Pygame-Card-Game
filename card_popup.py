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

        #Dark background
        pygame.draw.rect(screen, (80, 80, 80), (150, 50, 500, 500))

        #Border
        pygame.draw.rect(screen, (20, 20, 20), (150, 50, 500, 500),4)