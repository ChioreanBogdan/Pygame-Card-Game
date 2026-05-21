import pygame
from slot import Slot

class Board:
    def __init__(self, width, height):
        self.player_slots = []
        self.enemy_slots = []

        slot_width = 80
        slot_height = 120
        slot_margin = 20
        start_x = 50

        # PLAYER SLOTS
        y = height - 300

        for i in range(5):
            x = start_x + i * (slot_width + slot_margin)
            slot = Slot(pygame.Rect(x, y, slot_width, slot_height), None)
            self.player_slots.append(slot)

        # ENEMY SLOTS (same idea, different y)
        y_enemy = 150

        for i in range(5):
            x = start_x + i * (slot_width + slot_margin)
            slot = Slot(pygame.Rect(x, y_enemy, slot_width, slot_height), None)
            self.enemy_slots.append(slot)

        # Portrait size (width and height in pixels)
        # Used for enemy and Player portraits
        portrait_width = 140
        portait_height = 140

        # player deck rectangle
        self.deck_rect = pygame.Rect(width - 250, height - 180, 80, 120)

        # enemy portrait rectangle
        # X position:
        # Start at right edge (WIDTH),
        # move left by portrait width,
        # then move left 30 more pixels (margin)
        # Y position:
        # 40 pixels from the top
        self.enemy_rect = pygame.Rect(width - portrait_width - 30, 40, portrait_width, portait_height)

        # player portrait rectangle
        self.player_rect = pygame.Rect(width - portrait_width - 30, height-portait_height-40, portrait_width, portait_height)

