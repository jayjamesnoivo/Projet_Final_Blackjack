ACE = 11
BLACKJACK = 21


def calculate_score(hand:list) -> int:
    """
    Calculate the score of a hand, handle Aces and detect Blackjack.
    
    :param hand: The hand of the dealer or the player
    :return: Score of the hand
    :rtype: int
    """
    score = sum(hand)

    #Adjust Aces (11 -> 1) if score exceeds 21
    while ACE in hand and score > BLACKJACK:
        index_ace = hand.index (ACE)
        hand[ACE] = 1 
        score = sum(hand)

    return score


def check_hand_result(score:int) -> str:
    """
    Determine if hand is bust, blackjack or normal.
    
    :param score: Score of the hand
    :return: Result of the hand ("blackjack", bust" or "normal")
    :rtype: str
    """
    if score == BLACKJACK:
        return "blackjack"
    elif score > BLACKJACK:
        return "bust"
    else:
        return "normal"

