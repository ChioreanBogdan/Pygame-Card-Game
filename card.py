import pygame  # import the library
from kanji import Kanji #import Kanji class

class Card:
    def __init__(self, kanji, cost, x, y, font):
        self.kanji = kanji
        self.cost = cost
        
        # 🔥 Interaction box (used for clicking, dragging, slots)
        self.rect = pygame.Rect(x, y, 80, 120)

        # 🎯 Visual anchor (used for fan + rotation drawing)
        self.pos = (x, y)

        # 🎨 optional but useful later
        self.font = font

        # 🧠 state (useful for later mechanics)
        self.slot = None        # which slot it's in (if any)
        self.is_dragging = False

    def draw(self, surface, font, angle=0, scale=1.0):

        # 1. scale size
        width = int(80 * scale)
        height = int(120 * scale)

        # 2. create card surface
        card_surf = pygame.Surface((80, 120), pygame.SRCALPHA)

        # 3. draw ON CARD SURFACE (NOT screen)
        pygame.draw.rect(card_surf, (180, 180, 180), (0, 0, 80, 120))
        pygame.draw.rect(card_surf, (0, 0, 0), (0, 0, 80, 120), 2)

        # 4. draw text ON CARD SURFACE
        char_surf = font.render(self.kanji.symbol, True, (0, 0, 0))
        char_rect = char_surf.get_rect(center=(40, 60))
        card_surf.blit(char_surf, char_rect)

        # 5. rotate the FULL card
        rotated = pygame.transform.rotate(card_surf, angle)

        # 6. place it using pos (THIS is correct anchor)
        new_rect = rotated.get_rect(center=self.pos)

        # 7. draw to screen
        surface.blit(rotated, new_rect)

    