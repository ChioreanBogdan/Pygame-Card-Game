import pygame

class Hand:
    def __init__(self, cards, width, height):
        # List of Card objects in the player's hand
        self.cards = cards

        # Screen size (used to position the hand in the center bottom)
        self.WIDTH = width
        self.HEIGHT = height

        # How far apart cards are horizontally
        self.spacing = 90

        # Maximum angle spread for the fan
        self.max_angle = 30


    def get_hovered(self, mouse_pos):
        """
        Determine which card (if any) the mouse is currently hovering over.
        Returns the card object or None.
        """
        hovered = None

        # Loop through all cards in hand
        for card in self.cards:

            # Create a rectangular hitbox centered on the card
            # (we ignore rotation for simplicity)
            hitbox = pygame.Rect(0, 0, 80, 120)
            hitbox.center = card.pos

            # Check if mouse is inside this hitbox
            if hitbox.collidepoint(mouse_pos):
                hovered = card

        return hovered


    def draw(self, screen, font, dragging_card, mouse_pos):
        """
        Handles EVERYTHING about the hand:
        - finds hovered card
        - calculates fan layout
        - applies hover effects
        - updates positions
        - draws cards
        """

        # First, figure out which card is being hovered
        hovered_card = self.get_hovered(mouse_pos)

        # Total number of cards in hand
        hand_size = len(self.cards)

        # Loop through each card and position it
        for i, card in enumerate(self.cards):

            # Middle index (used to center the fan)
            mid = (hand_size - 1) / 2

            # Offset from center (negative = left, positive = right)
            offset = i - mid

            # Calculate rotation angle based on offset
            angle = -offset * (self.max_angle / max(1, mid))

            # Calculate position in a fan shape
            x = self.WIDTH // 2 + offset * self.spacing - 110
            y = self.HEIGHT - 90 + abs(offset) * 5  # slight curve

            # Default drawing values
            draw_angle = angle
            draw_pos = (x, y)
            scale = 1.0

            # ✨ If this card is hovered (and not being dragged)
            if card == hovered_card and card != dragging_card:
                # Lift it up
                draw_pos = (x, y - 40)

                # Make it straight (no rotation)
                draw_angle = 0

                # Make it slightly bigger
                scale = 1.2

            # If the card is NOT being dragged,
            # we control its position using the fan layout
            if card != dragging_card:
                card.pos = draw_pos
                card.rect.center = draw_pos

            # Finally, draw the card
            if card != dragging_card:
                card.draw(screen, font, draw_angle, scale)