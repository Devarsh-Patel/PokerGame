import random
from collections import Counter

# List of possible suits and ranks in a standard deck
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def create_deck():
    """
    Creates and shuffles a standard 52-card deck.
    :return: A shuffled list of cards.
    """
    deck = [f"{rank} of {suit}" for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck

def deal_cards(deck, num_players, cards_per_player):
    """
    Deals cards to players from the deck.
    :param deck: The deck to deal from.
    :param num_players: Number of players.
    :param cards_per_player: Number of cards per player.
    :return: List of hands, one per player.
    """
    return [deck[i*cards_per_player:(i+1)*cards_per_player] for i in range(num_players)]

def evaluate_hand(hand):
    """
    Evaluates a poker hand and returns a tuple with a numeric score and hand name.
    :param hand: List of cards in the player's hand.
    :return: Tuple (score, hand_name).
    """
    ranks = [card.split(' ')[0] for card in hand]
    rank_counts = Counter(ranks)
    counts = sorted(rank_counts.values(), reverse=True)
    if counts == [4, 1]:
        return (7, "Four of a Kind")
    elif counts == [3, 2]:
        return (6, "Full House")
    elif counts == [3, 1, 1]:
        return (3, "Three of a Kind")
    elif counts == [2, 2, 1]:
        return (2, "Two Pair")
    elif counts == [2, 1, 1, 1]:
        return (1, "One Pair")
    else:
        return (0, "High Card")