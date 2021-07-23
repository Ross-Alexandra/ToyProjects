import argparse

from hangman.framework.socket_server import HangmanServer
from hangman.hangman import play_game

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A fun game of hangman... with a twist!")
    parser.add_argument("-a", "--attempts", type=int, default=6, help="The number of attempts a player gets")
    parser.add_argument("-c", "--letter-count", type=int, default=6, help="The number of letter a word should have")
    parser.add_argument("-d", "--dictionary", type=str, default="hangman/hangman/res/dictionary.txt", help="The file to load the dictionary from")
    parser.add_argument("-s", "--server", action="store_true", help="Run a socket server rather than a CLI interface.")

    args = parser.parse_args()

    if args.server:
        print("Starting the hangman server")
        HangmanServer().listen()
    else:
        play_game(print, input, args.attempts, args.letter_count, args.dictionary, minimal=False)
