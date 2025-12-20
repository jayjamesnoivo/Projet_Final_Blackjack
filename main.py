from cartes import create_deck, deal_cards
from interface import *
from score import *

def main():
    dealer_hand = []
    player_hand = []
    player_score = 0
    dealer_score = 0
    game_over = False
    deck = create_deck()
    dealer_win = False
    player_win = False
    player_bust = False
    dealer_bust = False
    player_blackjack = False
    dealer_blackjack = False

    while not game_over:
        if len(player_hand) < 2: # First draw, each have 2 cards
            player_hand.append(deal_cards(deck))
            dealer_hand.append(deal_cards(deck))

        player_hand.append(deal_cards(deck))
        dealer_hand.append(deal_cards(deck))
        # player_hand = [10,11,5] # Used for test
        dealer_score =  calculate_score(dealer_hand)
        player_score = calculate_score(player_hand)
        
        dealer_result = check_hand_result(dealer_score)
        player_result = check_hand_result(player_score)
        display_hands(dealer_hand, player_hand, game_over)

        game_over = True
        
        if player_result == "blackjack":
            player_blackjack = True
            special_result = True
        elif dealer_result == "blackjack":
            dealer_blackjack = True
            special_result = True
        elif player_result == "bust":
            player_bust = True
            special_result = True
        elif dealer_result == "bust":
            dealer_bust = True
            special_result = True
        else:
            game_over = False
            special_result = False

        if not game_over:
            game_over = want_to_draw()
            # print(game_over)
        if game_over and not special_result:
            if player_score - 21 > dealer_score - 21:
                player_win = True
            else:
                dealer_win = True
        if game_over:
            display_result(dealer_win, player_win, player_score, dealer_score,
                           player_bust, dealer_bust, player_blackjack,
                           dealer_blackjack)
            display_hands(dealer_hand, player_hand, game_over)
main()