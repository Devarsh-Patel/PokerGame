# Entry point of the poker game

import random
from game import Game
from player import Player

class PokerTournament:
    """
    PokerTournament manages a tournament where 5 random players play 10 games,
    each game with a $500 pot. Tracks and reports each player's total winnings.
    """
    def __init__(self, all_player_names):
        """
        Initializes the tournament with 5 randomly selected players.
        :param all_player_names: List of possible player names.
        """
        self.players = [Player(name) for name in random.sample(all_player_names, 5)]
        self.winnings = {player.name: 0 for player in self.players}

    def play_tournament(self, num_games=10, pot=500):
        """
        Plays a series of games, updating each player's winnings.
        :param num_games: Number of games to play.
        :param pot: Dollar amount for each game.
        """
        for _ in range(num_games):
            # Create a new game with the same 5 players
            game = Game()
            game.players = self.players  # Use tournament players
            game.deck = game.deck  # Deck is created in Game's __init__
            # Deal cards and evaluate hands for all players
            game.start_game()
            # Use evaluate_hand from utils or Game for each player
            try:
                # Try to use Game's evaluate_hand if available
                scores = [game.evaluate_hand(player.hand) for player in self.players]
            except AttributeError:
                # Fallback: import evaluate_hand from utils
                from utils import evaluate_hand
                scores = [evaluate_hand(player.hand) for player in self.players]
            max_score = max(score[0] for score in scores)
            winners = [i for i, score in enumerate(scores) if score[0] == max_score]
            split_pot = pot // len(winners)
            # If tie, both (or all) winners get equal share of the pot
            if len(winners) > 1:
                print(f"Tie between: {[self.players[idx].name for idx in winners]}. Each gets ${split_pot}.")
            else:
                print(f"Winner: {self.players[winners[0]].name} gets ${pot}.")
            for idx in winners:
                self.winnings[self.players[idx].name] += split_pot

    def get_winnings_list(self):
        """
        Returns a list of winnings for each player (in order 1-5).
        """
        return [self.winnings[player.name] for player in self.players]

# Example usage:
def main():
    """
    Main function to run the poker tournament.
    """
    all_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
    tournament = PokerTournament(all_names)
    tournament.play_tournament(num_games=10, pot=500)
    winnings = tournament.get_winnings_list()
    print("Players:", [player.name for player in tournament.players])
    print("Winnings (in order 1-5):", winnings)

if __name__ == "__main__":
    main()