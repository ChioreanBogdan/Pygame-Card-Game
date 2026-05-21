#py tiny_kanji_card_game.py
import pygame  # import the library

class Slot:
    def __init__(self, rect,card= None):
        self.rect = rect
        self.card = None  # what card is in this slot (None = empty)
