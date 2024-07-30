from TicTacTocGame import TicTacToeGame

if __name__ == "__main__":
    game = TicTacToeGame()
    game.initialize_game()
    print("Game winner is:", game.start_game())
