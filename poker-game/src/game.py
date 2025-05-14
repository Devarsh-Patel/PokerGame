from player import Player
from utils import create_deck, deal_cards, evaluate_hand

class Game:
    """
    Game class manages the overall flow of the poker game.
    Handles player creation, deck management, dealing cards,
    evaluating hands, and determining the winner.
    """
    def __init__(self):
        """
        Initializes the Game object:
        - Creates two Player instances.
        - Creates a new shuffled deck.
        """
        self.players = [Player("Player 1"), Player("Player 2")]
        self.deck = create_deck()

    def start_game(self, game_number=None):
        """
        Starts the poker game:
        - Creates and shuffles a new deck.
        - Deals 5 cards to each player.
        - Evaluates each player's hand.
        - Prints the hands and determines the winner.
        :param game_number: Optional, the current game number for display.
        """
        if game_number is not None:
            print(f"\n--- Game {game_number} ---")
        else:
            print("\n--- Poker Game ---")
        self.deck = create_deck()
        hands = deal_cards(self.deck, len(self.players), 5)
        for i, player in enumerate(self.players):
            player.hand = hands[i]
            print(f"{player.name}'s hand: {player.hand}")

        scores = []
        for player in self.players:
            score = evaluate_hand(player.hand)
            scores.append(score)
            print(f"{player.name}'s hand rank: {score[1]}")

        # Compare scores and determine the winner
        if scores[0][0] > scores[1][0]:
            print(f"\n{self.players[0].name} wins!")
        elif scores[0][0] < scores[1][0]:
            print(f"\n{self.players[1].name} wins!")
        else:
            print("\nIt's a tie!")