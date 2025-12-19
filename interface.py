def interface(
        dealer_hand:list, player_hand:list, 
        dealer_win:bool, player_win:bool,
        score_player:int, score_dealer:int,
        player_bust:bool, dealer_bust:bool,
        player_blackjack:bool, dealer_blackjack:bool,
    )->bool:
    '''
    Diplay the interface/menu for the player
    
    :param dealer_hand: A list of str with the dealer cards
    :type dealer_hand: list
    :param player_hand: A list of str with the player cards
    :type player_hand: list
    :param dealer_win: If the dealer win
    :type dealer_win: bool
    :param player_win: If the player win
    :type player_win: bool
    :param score_player: The actual score of the player
    :type score_player: int
    :param score_dealer: The actual score of the dealer
    :type score_dealer: bool
    :param player_bust: Description
    :type player_bust: bool
    :param dealer_bust: Description
    :type dealer_bust: bool
    :param player_blackjack: Description
    :type player_blackjack: bool
    :param dealer_blackjack: Description
    :type dealer_blackjack: bool
    :return: If the player want another card
    :rtype: bool
    '''
    FIRST_DEALER_CARD = 0
    LOGO = """
            .------.            _     _            _    _            _    
            |A_  _ |.          | |   | |          | |  (_)          | |   
            |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
            | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
            |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
            `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\__|
                  |  \/ K|                            _/ |                
                  `------'                           |__/           
        """

    print(LOGO)
    print(f"Dealer's hand: {dealer_hand[FIRST_DEALER_CARD]}")
    print(f"Your hand: {' , '.join(player_hand)}")

    if dealer_win:
        print(f"You lost, the dealer won with a score of: {score_dealer}")
    elif player_win:
        print(f"You won with a score of: {score_player}!")
    elif player_blackjack:
        print("You win, you got a black jack")
    elif dealer_blackjack:
        print("You lost, the dealer got a blackjack")
    elif dealer_bust:
        print("The dealer busted, you win")
    elif player_bust:
        print("You busted, you lost")

    while True:
        reponse_joueur = input("Would you like to draw antoher card (y/n)?")
        if reponse_joueur == "y":
            return True
        elif reponse_joueur == "n":
            return False