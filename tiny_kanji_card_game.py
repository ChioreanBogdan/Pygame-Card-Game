import pygame  # import the library
from card import Card #import Card class
from slot import Slot #import Slot class
from hand import Hand #import Hand class
from kanji import Kanji #import Kanji class
from kanji_database import KANJI_DB
from player import Player #import Player class
from turn_manager import TurnManager #import TurnManager
from renderer import Renderer
from board import Board

pygame.init()  # initialize pygamefrom board import Board

print("testin")

kanji_font = pygame.font.SysFont("MS Gothic", 48)  # None = default font, 48 = size
ui_font = pygame.font.SysFont("Arial", 28)

#Create turn manager object
turn_manager = TurnManager()

# --- Settings ---
WIDTH = 800
HEIGHT = 600

#Made End Turn button rect
end_turn_rect = pygame.Rect(WIDTH - 220, HEIGHT // 2 - 30, 140, 60)

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Name of window
pygame.display.set_caption("Tiny Card Game")

#Create renderer object,this handles graphics
renderer = Renderer(screen, ui_font, kanji_font)

dragging_card = None
# Main loop

#Create 2 Player objects
player = Player("Player")
enemy = Player("Enemy")

#Create board object
board = Board(WIDTH,HEIGHT,player,enemy)

# Draw one card
#card_rect = pygame.Rect(100, 400, 80, 120)  # x, y, width, height
my_card = Card(KANJI_DB["火"], 1, 100, 400, kanji_font)

my_card2 = Card(KANJI_DB["山"], 1, 180, 400, kanji_font)

running = True

player.deck = ["火", "山", "水", "木", "金"]

player_hand_cards = []
hand = Hand(player_hand_cards, WIDTH, HEIGHT)
player_cards = []

hand_for_card1 = Card(KANJI_DB["火"], 1, 100, 400, kanji_font)
hand_for_card2 = Card(KANJI_DB["山"], 1, 100, 400, kanji_font)
hand_for_card3 = Card(KANJI_DB["水"], 1, 100, 400, kanji_font)
hand.cards.append(hand_for_card1)
hand.cards.append(hand_for_card2)
hand.cards.append(hand_for_card3)

#This is the center bottom of the screen
HAND_Y = HEIGHT - 120
HAND_CENTER_X = WIDTH // 2

#We space cards and rotate slightly
spacing = 90
start_x = HAND_CENTER_X - (len(hand.cards) - 1) * spacing // 2

max_angle = 30  # total spread

#This is only for testing purposes and must be changed later
#player_cards.append(my_card)
#player_cards.append(my_card2)

while running:
        
    screen.fill((255, 255, 255))  # fill the screen with white

    # draw player slots+enemy slots
    renderer.draw_board(board)
 
    #my_card.draw(screen,kanji_font)
    #my_card2.draw(screen,kanji_font)

    mouse_pos = pygame.mouse.get_pos()

    for card in player_cards:
        if card != dragging_card:   # don't double-draw dragged card
            card.draw(screen, kanji_font)

    if dragging_card:
        dragging_card.draw(screen, kanji_font)

    hand.draw(screen, kanji_font, dragging_card, mouse_pos)

    pygame.display.flip()  # update the screen (otherwise what we draw appears only in memory,not on the screen)

    for event in pygame.event.get():
        # if event.type == pygame.MOUSEMOTION:
        #     print("MOUSEMOTION detected!", event.pos)
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     print("Mouse down!", event.pos)
        if event.type == pygame.QUIT:  # clicking the X closes the window
            running = False
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:  # left mouse button
        #         #mouse_pos = pygame.mouse.get_pos()
        #         if my_card.rect.collidepoint(event.pos):
        #             print("Card clicked!")
        #             dragging_card = my_card 

        # If the user presses any mouse button
        elif event.type == pygame.MOUSEBUTTONDOWN:  

            # Check if it was the left mouse button (1 = left click)
            if event.button == 1:  

                                # click on deck
                if board.deck_rect.collidepoint(event.pos):

                    if len(player.deck) > 0:

                        card_name = player.deck.pop()
                        kanji_obj = KANJI_DB[card_name]

                        new_card = Card(kanji_obj,1,200,400,kanji_font)

                        hand.cards.append(new_card)

                # Check if the mouse click was inside the card's rectangle
                for player_card in reversed(player_cards + hand.cards):

                    if player_card.rect.collidepoint(event.pos):
                        dragging_card = player_card

                        dragging_card.old_slot = None
                        # if this card was in a slot, empty that slot
                        for slot in board.player_slots:
                            if slot.card is dragging_card:
                                slot.card = None
                        #print("Started dragging " + dragging_card.name)
                                break
                        # Start dragging this card

                #Check if mouse was inside "End turn" button rectangle
                if board.end_turn_rect.collidepoint(event.pos):
                    turn_manager.end_turn()
                    print(f"Turn number = {turn_manager.current_turn}")

        # If the mouse is moved
        elif event.type == pygame.MOUSEMOTION: 
            #print("Mouse motion detected") 
            # Only do this if a card is currently being dragged
            if dragging_card:  

                # Move the card's center to the current mouse position
                dragging_card.pos = event.pos
                dragging_card.rect.center = event.pos
                #print("Dragging to:", event.pos)
                #print("Dragging:", dragging_card.name, "at", dragging_card.rect.topleft)

        # If the user releases a mouse button
        elif event.type == pygame.MOUSEBUTTONUP:  

            #Aici am ramas 13/04/2026
            # Check if it was the left mouse button
            if event.button == 1:
                if dragging_card:

                    placed_in_slot = False  # track if we snapped it

                    # Try to place in a slot
                    for slot in board.player_slots:
                        if slot.rect.collidepoint(dragging_card.pos):
                             # only allow empty slots
                            if slot.card is not None:
                                continue
                            
                            dragging_card.pos = slot.rect.center
                            dragging_card.rect.center = slot.rect.center
                            slot.card = dragging_card

                            # remove from hand so Hand.draw stops managing it
                            if dragging_card in hand.cards:
                                hand.cards.remove(dragging_card)

                            if dragging_card not in player_cards:
                                player_cards.append(dragging_card)

                            placed_in_slot = True
                            break

                    # 🔥 If NOT placed in any slot → remove from all slots
                    
                    if not placed_in_slot:
                        if dragging_card.old_slot:
                            dragging_card.old_slot.card = dragging_card
                            dragging_card.pos = dragging_card.old_slot.rect.center
                            dragging_card.rect.center = dragging_card.old_slot.rect.center

                dragging_card = None

#pygame.quit()

#screen.fill((255, 255, 255))  # fill the screen with white
#my_card.draw(screen,font)
#my_card2.draw(screen,font)

pygame.display.flip()  # update the screen (otherwise what we draw appears only in memory,not on the screen)
