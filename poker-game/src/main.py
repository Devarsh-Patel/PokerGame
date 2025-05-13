# Entry point of the poker game

from game import Game

def main():
    """
    Main function to start the poker game.
    Creates a Game instance and starts the game.
    """
    game = Game()
    game.start_game()

if __name__ == "__main__":
    # Run the main function if this script is executed directly
    main()