#Handles drawing
import pygame

class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def draw_board(self, player_rect, enemy_rect, deck_rect):
        # deck
        pygame.draw.rect(self.screen, (120,120,120), deck_rect)
        pygame.draw.rect(self.screen, (0,0,0), deck_rect, 3)

        # enemy portrait
        pygame.draw.rect(self.screen, (200,100,100), enemy_rect)
        pygame.draw.rect(self.screen, (0,0,0), enemy_rect, 3)

        # player portrait
        pygame.draw.rect(self.screen, (100,100,200), player_rect)
        pygame.draw.rect(self.screen, (0,0,0), player_rect, 3)


    def draw_slots(self, slots):
        for slot in slots:
            pygame.draw.rect(self.screen, (200,200,200), slot.rect, 2)


    def draw_cards(self, cards, font):
        for card in cards:
            card.draw(self.screen, font)


    def draw_end_turn_button(self, rect, font):
        pygame.draw.rect(self.screen, (220,220,100), rect)
        pygame.draw.rect(self.screen, (0,0,0), rect, 2)

        text = self.font.render("End", True, (0,0,0))
        text_rect = text.get_rect(center=rect.center)

        self.screen.blit(text, text_rect)