from hangman.hangman.hangman_exception import HangmanException

class HangManEngine:

    def __init__(self, letter_count, dictionary):
        self.language_pattern = "." * letter_count
        self.language = self.parse_dictionary(dictionary, letter_count)

        if len(self.language) <= 0:
            raise HangmanException(f"No words found of length {letter_count} in {dictionary}")

    @staticmethod
    def parse_dictionary(dictionary, word_length):
        try:
            with open(dictionary, "r") as dictionary_file:
                language = dictionary_file.readlines()
        except:
            return []

        return [x.strip() for x in language if len(x) == word_length]

    def get_key(self, word, letter_guess):
        key = []

        for index, letter in enumerate(word):
            if self.language_pattern[index] != ".":
                key.append(self.language_pattern[index])
            elif letter == letter_guess:
                key.append(letter)
            else:
                key.append(".")

        return "".join(key)

    def remove_letter(self, letter):
        """ Implement a naive solution wihtout using trees as there deadline is too quick."""

        potential_new_languages = {}

        # Iterate through all the words in the current language
        # and find a new language largest language.
        # Languages are determined by all combonations and permutations
        # of patterns of letter for all words of letter_count length 
        for word in self.language:

            # Rebuild the word replacing every letter which doesn't match letter 
            # is replaced with a .
            key = self.get_key(word, letter)

            if potential_new_languages.get(key, None) is not None:
                potential_new_languages[key].append(word)
            else:
                potential_new_languages[key] = [word]

        language_lengths = {len(value): key for key, value in potential_new_languages.items() }

        largest_language_key = language_lengths[max(language_lengths.keys())]

        self.language_pattern = largest_language_key
        self.language = potential_new_languages[largest_language_key]