#Handles drawing
import pygame
from board import Board

class Renderer:
    def __init__(self, screen, ui_font, kanji_font):
        self.screen = screen
        self.ui_font = ui_font
        self.kanji_font = kanji_font

    #draw player and enemy slots,more needs to be added later
    def draw_board(self, board):
        self.draw_slots(board.player_slots)
        self.draw_slots(board.enemy_slots)

        #deck (player)
        pygame.draw.rect(self.screen, (120,120,120), board.deck_rect)
        pygame.draw.rect(self.screen, (0,0,0), board.deck_rect, 3)

        # Draw enemy portrait background (red-ish)
        # Draw enemy portrait border (black, thickness 3)
        pygame.draw.rect(self.screen, (200,100,100), board.enemy_rect)
        pygame.draw.rect(self.screen, (0,0,0), board.enemy_rect, 3)

        # Draw player portrait background (blue-ish)
        # Draw player portrait border (black, thickness 3)
        pygame.draw.rect(self.screen, (100,100,200), board.player_rect)
        pygame.draw.rect(self.screen, (0,0,0), board.player_rect, 3)

    # def draw_board(self, player_rect, enemy_rect, deck_rect):
    #     # deck
    #     pygame.draw.rect(self.screen, (120,120,120), deck_rect)
    #     pygame.draw.rect(self.screen, (0,0,0), deck_rect, 3)

    #     # enemy portrait
    #     pygame.draw.rect(self.screen, (200,100,100), enemy_rect)
    #     pygame.draw.rect(self.screen, (0,0,0), enemy_rect, 3)

    #     # player portrait
    #     pygame.draw.rect(self.screen, (100,100,200), player_rect)
    #     pygame.draw.rect(self.screen, (0,0,0), player_rect, 3)

    def draw_slots(self, slots):
        for slot in slots:
            # draw slot border
            pygame.draw.rect(self.screen, (200, 200, 200), slot.rect, 2)

            # if card exists in slot, draw it
            if slot.card:
                slot.card.draw(self.screen, self.kanji_font)

    def draw_cards(self, cards, font):
        for card in cards:
            card.draw(self.screen, font)

    def draw_end_turn_button(self, rect, font):
        pygame.draw.rect(self.screen, (220,220,100), rect)
        pygame.draw.rect(self.screen, (0,0,0), rect, 2)

        text = self.font.render("End", True, (0,0,0))
        text_rect = text.get_rect(center=rect.center)

        self.screen.blit(text, text_rect)