class Player:
    """
    Player class represents a poker player.
    Stores the player's name and their current hand.
    """
    def __init__(self, name):
        """
        Initializes a Player object with a name and an empty hand.
        :param name: Name of the player.
        """
        self.name = name
        self.hand = []
        self.chips = 100  # Starting chips for the player

    def place_bet(self, amount):
        if amount > self.chips:
            raise ValueError("Insufficient chips to place bet.")
        self.chips -= amount
        return amount

    def receive_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def evaluate_hand(self):
        # Placeholder for hand evaluation logic
        return "Hand evaluation logic not implemented."

    def __str__(self):
        return f"Player {self.name} with chips: {self.chips} and hand: {self.hand}"