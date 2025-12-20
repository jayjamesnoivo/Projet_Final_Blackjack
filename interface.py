def display_result(
        dealer_win:bool, player_win:bool,
        score_player:int, score_dealer:int,
        player_bust:bool, dealer_bust:bool,
        player_blackjack:bool, dealer_blackjack:bool,
    ):
    '''
    Diplay the interface/menu for the player
    
    :param dealer_win: If the dealer win
    :type dealer_win: bool
    :param player_win: If the player win
    :type player_win: bool
    :param score_player: The actual score of the player
    :type score_player: int
    :param score_dealer: The actual score of the dealer
    :type score_dealer: bool
    :param player_bust: If the player have more than 21 score
    :type player_bust: bool
    :param dealer_bust: If the dealer have more than 21 score
    :type dealer_bust: bool
    :param player_blackjack: if the player have a score of 21
    :type player_blackjack: bool
    :param dealer_blackjack: If the dealer have a score of 21
    :type dealer_blackjack: bool
    '''
    if dealer_win:
        print(f"You lost, the dealer won with a score of: {score_dealer}")
    elif player_win:
        print(f"You won with a score of: {score_player}!")
    elif player_blackjack:
        print("You win, you got a black jack")
    elif dealer_blackjack:
        print("You lost, the dealer got a blackjack")
    elif dealer_bust:
        print(f"The dealer busted with a score of {score_dealer}, you win")
    elif player_bust:
        print(f"You busted with a score of {score_player}, you lost")

def want_to_draw()->bool:
    '''
    Docstring for want_to_draw
    
    :param game_over: If it's a game over
    :type game_over: bool
    :return: If the player want another card
    :rtype: bool
    '''
    while True:
        player_answer = input("Would you like to draw antoher card (y/n)? ")
        if player_answer == "y":
            return False
        elif player_answer == "n":
            return True
        else:
            print("Wrong input, try again!")

def display_hands(dealer_hand:list, player_hand:list,game_over:bool):
    '''
    Docstring for display_hands
    
    :param dealer_hand: A list of str with the dealer cards
    :type dealer_hand: list
    :param player_hand: A list of str with the player cards
    :type player_hand: list
    '''
    FIRST_DEALER_CARD = 0
    if not game_over:
        print(f"Dealer's hand: {dealer_hand[FIRST_DEALER_CARD]}")
    else:
        print(f"Dealer's hand: {dealer_hand}")
    print(f"Your hand: {player_hand}")