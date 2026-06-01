import pygame
from slot import Slot
from card import Card #import Card class

class Board:
    def __init__(self, width, height,player,enemy):

        self.width = width
        self.height = height

        self.player = player
        self.enemy = enemy

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

        # make a little bubble rect left of enemy portrait
        self.enemy_hp_bubble = pygame.Rect(self.enemy_rect.left-20, self.enemy_rect.centery+40, 70, 40)

        # make a little bubble rect left of player portrait
        self.player_hp_bubble = pygame.Rect(self.player_rect.left-20, self.player_rect.centery+40, 70, 40)

        #Rect for end turn button position
        self.end_turn_rect = pygame.Rect(
            width -180,
            height // 2 - 35,
            150,
            50
                                        )
        
    def start_drag(self, card):
        self.dragging_card = card

        # if in slot, temporarily free it
        for slot in self.player_slots:
            if slot.card == card:
                slot.card = None

    def release_drag(self, card, pos, hand):
        placed = False

        for slot in self.player_slots:
            if slot.rect.collidepoint(pos) and slot.card is None:
                slot.card = card
                card.rect.center = slot.rect.center
                placed = True
                break

        if not placed:
            # snap back logic
            if card in hand.cards:
                card.pos = card.original_pos
                card.rect.center = card.original_pos
            else:
                for slot in self.player_slots:
                    if slot.card == card:
                        card.rect.center = slot.rect.center
                        break