class Player:
    """
    Player class represents a poker player.
    Stores the player's name, current hand, and chip count.
    Provides methods for betting, receiving cards, clearing hand, and hand evaluation.
    """

    def __init__(self, name):
        """
        Initializes a Player object with a name, empty hand, and starting chips.
        :param name: Name of the player.
        """
        self.name = name
        self.hand = []         # List to store the player's current hand (cards)
        self.chips = 100       # Starting chips for the player

    def place_bet(self, amount):
        """
        Deducts the bet amount from the player's chips if sufficient chips are available.
        Raises ValueError if the player tries to bet more chips than they have.
        :param amount: Amount to bet.
        :return: The bet amount.
        """
        if amount > self.chips:
            raise ValueError("Insufficient chips to place bet.")
        self.chips -= amount
        return amount

    def receive_card(self, card):
        """
        Adds a card to the player's hand.
        :param card: Card to add (string).
        """
        self.hand.append(card)

    def clear_hand(self):
        """
        Clears the player's hand for a new round.
        """
        self.hand = []

    def evaluate_hand(self):
        """
        Placeholder for hand evaluation logic.
        Should be replaced with actual hand evaluation in the future.
        :return: String indicating evaluation status.
        """
        return "Hand evaluation logic not implemented."

    def __str__(self):
        """
        Returns a string representation of the player, including name, chips, and hand.
        """
        return f"Player {self.name} with chips: {self.chips} and hand: {self.hand}"