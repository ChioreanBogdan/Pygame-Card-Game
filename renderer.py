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

        # render enemy HP text
        enemy_hp_text = self.ui_font.render(str(board.enemy.hp), True, (0, 0, 0))

        # draw bubble
        pygame.draw.circle(self.screen, (255, 255, 255), board.enemy_hp_bubble.center,25)
        pygame.draw.circle(self.screen, (0, 0, 0), board.enemy_hp_bubble.center,25, 2)

        # center text in bubble
        text_rect = enemy_hp_text.get_rect(center=board.enemy_hp_bubble.center)
        self.screen.blit(enemy_hp_text, text_rect)

        # render player HP text
        player_hp_text = self.ui_font.render(str(board.player.hp), True, (0, 0, 0))

        # draw bubble
        pygame.draw.circle(self.screen, (255, 255, 255), board.player_hp_bubble.center,25)
        pygame.draw.circle(self.screen, (0, 0, 0), board.player_hp_bubble.center,25, 2)

        # center text in bubble
        text_rect = player_hp_text.get_rect(center=board.player_hp_bubble.center)
        self.screen.blit(player_hp_text, text_rect)

        # draw end turn button between portraits
        self.draw_end_turn_button(board.end_turn_rect)

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

    def draw_end_turn_button(self, rect):
        pygame.draw.rect(self.screen, (130,130,130), rect)
        pygame.draw.rect(self.screen, (0,0,0), rect, 4)

        text = self.ui_font.render("End Turn", True, (0,0,0))
        text_rect = text.get_rect(center=rect.center)

        self.screen.blit(text, text_rect)