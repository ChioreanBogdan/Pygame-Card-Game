import pygame  # import the library
from card import Card #import Card class
from slot import Slot #import Slot class
from hand import Hand #import Hand class
from kanji import Kanji #import Kanji class
from kanji_database import KANJI_DB
from player import Player #import Player class
from turn_manager import TurnManager #import TurnManager
from renderer import Renderer

pygame.init()  # initialize pygame

kanji_font = pygame.font.SysFont("MS Gothic", 48)  # None = default font, 48 = size
ui_font = pygame.font.SysFont("Arial", 28)

#Import turn manager
turn_manager = TurnManager()

# --- Settings ---
WIDTH = 800
HEIGHT = 600

#Made End Turn button rect
end_turn_rect = pygame.Rect(WIDTH - 220, HEIGHT // 2 - 30, 140, 60)

# Portrait size (width and height in pixels)
# Used for enemy and Player portraits
PORTRAIT_WIDTH = 140
PORTRAIT_HEIGHT = 140

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tiny Card Game")

#Create renderer object,this handles graphics
renderer = Renderer(screen)

# Player field slots (bottom of the screen)
player_slots = []
enemy_slots = []
slot_width = 80
slot_height = 120
slot_margin = 20
start_x = 50

#create rectangles for player and enemy slots
y = HEIGHT - 300  # some distance above the player portrait

for i in range(5):  # 5 slots
    x = start_x + i * (slot_width + slot_margin)
    new_player_slot= Slot(pygame.Rect(x, y, slot_width, slot_height),None)
    player_slots.append(new_player_slot)

y = 150  # below the enemy portrait
for i in range(5):
    x = start_x + i * (slot_width + slot_margin)
    new_enemy_slot=Slot(pygame.Rect(x, y, slot_width, slot_height),None)
    enemy_slots.append(new_enemy_slot)


    # Create enemy portrait rectangle (top right)

enemy_rect = pygame.Rect(WIDTH - PORTRAIT_WIDTH - 30, 40, PORTRAIT_WIDTH, PORTRAIT_HEIGHT)
                                  # X position:
                                  # Start at right edge (WIDTH),
                                  # move left by portrait width,
                                  # then move left 30 more pixels (margin)
                               # Y position:
                                  # 40 pixels from the top
    
                  # rectangle width
                   # rectangle height


# Create player portrait rectangle (bottom right)

player_rect = pygame.Rect(WIDTH - PORTRAIT_WIDTH - 30, HEIGHT - PORTRAIT_HEIGHT - 40,     PORTRAIT_WIDTH,PORTRAIT_HEIGHT)
                          # Same X position as enemy
    
                            # Y position:
                                     # Start at bottom (HEIGHT),
                                     # move up by portrait height,
                                     # move up 40 more pixels (margin)
#create a rectangle for the deck
deck_rect = pygame.Rect(WIDTH-250, HEIGHT - 180, 80, 120)

dragging_card = None
# Main loop

#Create 2 Player objects
player = Player("Player")
enemy = Player("Enemy")

# Draw one card
#card_rect = pygame.Rect(100, 400, 80, 120)  # x, y, width, height
my_card = Card(KANJI_DB["火"], 1, 1, 1, 100, 400, kanji_font)

my_card2 = Card(KANJI_DB["山"], 1, 1, 1, 180, 400, kanji_font)

running = True

player.deck = ["火", "山", "水", "木", "金"]

player_hand_cards = []
hand = Hand(player_hand_cards, WIDTH, HEIGHT)
player_cards = []

hand_for_card1 = Card(KANJI_DB["火"], 1, 1, 1, 100, 400, kanji_font)
hand_for_card2 = Card(KANJI_DB["山"], 1, 1, 1, 100, 400, kanji_font)
hand_for_card3 = Card(KANJI_DB["水"], 1, 1, 1, 100, 400, kanji_font)
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
player_cards.append(my_card)
player_cards.append(my_card2)

while running:
        
    screen.fill((255, 255, 255))  # fill the screen with white

    # draw deck
    pygame.draw.rect(screen, (120,120,120), deck_rect)
    pygame.draw.rect(screen, (0,0,0), deck_rect, 3)

    # Draw enemy portrait background (red-ish)
    pygame.draw.rect(screen, (200, 100, 100), enemy_rect)

    # Draw enemy portrait border (black, thickness 3)
    pygame.draw.rect(screen, (0, 0, 0), enemy_rect, 3)

    # render enemy HP text
    enemy_hp_text = ui_font.render("25", True, (0, 0, 0))

    # make a little bubble rect left of enemy portrait
    enemy_hp_bubble = pygame.Rect(enemy_rect.left-20, enemy_rect.centery+40, 70, 40)

    # draw bubble
    pygame.draw.circle(screen, (255, 255, 255), enemy_hp_bubble.center,25)
    pygame.draw.circle(screen, (0, 0, 0), enemy_hp_bubble.center,25, 2)

    # center text in bubble
    text_rect = enemy_hp_text.get_rect(center=enemy_hp_bubble.center)
    screen.blit(enemy_hp_text, text_rect)

    # Draw player portrait background (blue-ish)
    pygame.draw.rect(screen, (100, 100, 200), player_rect)

    # Draw player portrait border
    pygame.draw.rect(screen, (0, 0, 0), player_rect, 3)

    # render player HP text
    player_hp_text = ui_font.render("25", True, (0, 0, 0))

    # make a little bubble rect left of player portrait
    player_hp_bubble = pygame.Rect(player_rect.left-20, player_rect.centery+40, 70, 40)

    # draw bubble
    pygame.draw.circle(screen, (255, 255, 255), player_hp_bubble.center,25)
    pygame.draw.circle(screen, (0, 0, 0), player_hp_bubble.center,25, 2)

    # center text in bubble
    text_rect = player_hp_text.get_rect(center=player_hp_bubble.center)
    screen.blit(player_hp_text, text_rect)
 
    # draw player slots
    for slot in player_slots:
        pygame.draw.rect(screen, (200,200,200), slot.rect, 2)  # light gray border
        if slot.card:
            slot.card.draw(screen, kanji_font)

    # draw enemy slots
    for slot in enemy_slots:
        pygame.draw.rect(screen, (200,200,200), slot.rect, 2)


    my_card.draw(screen,kanji_font)
    my_card2.draw(screen,kanji_font)

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
                if deck_rect.collidepoint(event.pos):

                    if len(player.deck) > 0:

                        card_name = player.deck.pop()
                        kanji_obj = KANJI_DB[card_name]

                        new_card = Card(kanji_obj,1,1,1,200,400,kanji_font)

                        hand.cards.append(new_card)

                # Check if the mouse click was inside the card's rectangle
                for player_card in reversed(player_cards + hand.cards):

                    hitbox = pygame.Rect(player_card.pos[0] - 40,
                                        player_card.pos[1] - 60,
                                        80, 120)

                    if hitbox.collidepoint(event.pos):
                        dragging_card = player_card

                        # if this card was in a slot, empty that slot
                        for slot in player_slots:
                            if slot.card == dragging_card:
                                slot.card = None
                        #print("Started dragging " + dragging_card.name)
                        break
                        # Start dragging this card

                        

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
                    for slot in player_slots:
                        if slot.rect.collidepoint(dragging_card.pos):
                             # only allow empty slots
                            if slot.card is None:
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
                        for slot in player_slots:
                            if slot.card == dragging_card:
                                slot.card = None

                dragging_card = None

#pygame.quit()

#screen.fill((255, 255, 255))  # fill the screen with white
#my_card.draw(screen,font)
#my_card2.draw(screen,font)


pygame.display.flip()  # update the screen (otherwise what we draw appears only in memory,not on the screen)
