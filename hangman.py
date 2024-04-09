import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''' + "\n", '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''' + "\n", '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''' + "\n", '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''' + "\n", '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''' + "\n", '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''' + "\n", '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= ''' + "\n"]

words_list = [
    'fine',
    'standard',
    'disappointment',
    'general',
    'appear',
    'complain',
    'handy',
    'response',
    'effort',
    'dinner',
    ]

class Hangman:
    def __init__(self):
        self.letter = ""
        self.word = self.get_word()
        self.spaces = self.get_spaces()
        self.count_guesses = 0
        self.word_map = self.get_word_map()
        self.used_letters = set()

    def start_game(self):
        print(self.show_picture(self.count_guesses))
        self.letter = input("Guess a letter: ")
        self.letter_check(self.letter)
        self.check_guess()
        if "".join(self.spaces) == self.word:
            return f'Congrats you won! The word was {self.word}'
        elif self.count_guesses < len(HANGMANPICS):
            return self.start_game()
        else:
            return f'Game over, word was {self.word}'

    def letter_check(self, letter):
        while not self.letter.isalpha() or len(self.letter) != 1 or self.letter in self.used_letters:
            if self.letter in self.used_letters:
                self.letter = input("You have already entered this letter. Please enter a new letter: ")
            else:
                self.letter = input("Please enter a valid letter. Please guess a letter: ")
        return self.letter
    
    def get_word(self):
        print(random.randint(0,len(words_list)))
        self.word = words_list[random.randint(0,len(words_list)-1)]
        return self.word

    def get_word_map(self):
        w_map = {}
        for i in range(len(self.word)):
            if self.word[i] in w_map:
                w_map[self.word[i]] += [i]
            else:
                w_map[self.word[i]] = [i]
        return w_map
    
    def get_spaces(self):
        self.spaces = list(len(self.word) * ("_"))
        return self.spaces
    
    def show_picture(self,count_guesses):
        return f'{HANGMANPICS[self.count_guesses]} {" ".join(self.spaces)}'
    
    def check_guess(self):
        if self.letter in self.word_map:
            for i in self.word_map[self.letter]:
                self.spaces[i] = self.letter
        else:
            self.count_guesses += 1
        self.used_letters.add(self.letter)

h = Hangman()
print(h.start_game())
