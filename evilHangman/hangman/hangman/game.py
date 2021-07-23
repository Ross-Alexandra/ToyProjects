import re

from hangman.hangman.hangman_engine import HangManEngine
from hangman.hangman.hangman_exception import HangmanException

class Game:

    def __init__(self, attempts: int=6, letter_count: int=6, dictionary: str="res/dictionary.txt"):
        self.attempts = attempts
        self._engine = HangManEngine(letter_count, dictionary)

    def play_letter(self, letter):
        self.attempts -= 1

        self._engine.remove_letter(letter)

    def get_board(self):
        return self._engine.language_pattern.replace(".", "_")

    def words_in_play(self):
        return len(self._engine.language)

    def is_game_over(self):
        return "." not in self._engine.language_pattern or self.attempts <= 0

    def game_won(self):
        return "." not in self._engine.language_pattern

def _play_game(send_message, receive_message, attempts, letter_count, dictionary, minimal=False):
    try:
        game = Game(attempts, letter_count, dictionary)
    except HangmanException as e:
        send_message(e)
        exit()

    previous_board = game.get_board()

    while not game.is_game_over():

        if not minimal:
            send_message(f"Current word: {' '.join(previous_board.split())}")
        else:
            send_message(f"key={previous_board}")

        letter_guess = ""
        while not re.match(r"[a-z]$", letter_guess):
            if not minimal:
                send_message("Please select a letter [a-z]: ")
            else:
                send_message("request input")
            letter_guess = str(receive_message()).lower()

        game.play_letter(letter_guess)
        board = game.get_board()
        guess_message = f"You got a letter!" if board != previous_board else f"Nope sorry, not in the word."

        if not minimal:
            send_message(f"{guess_message} You only have {game.attempts} guesses remaining! Good news though, there's only {game.words_in_play()} more words it could possibly be...")
        else:
            send_message(f"attempts={game.attempts};remaning_words={game.words_in_play()}")

        previous_board = board

    if game.game_won():
        if not minimal:
            send_message(f"Congradulations!! You won hangman! The word was: {game.get_board()}")
        else:
            send_message(f"win=true;word={game.get_board()}")

    else:
        if not minimal:
            send_message("Ooooh looks like you're bad at guessing words. Better luck next time!")
        else:
            send_message(f"win=false")