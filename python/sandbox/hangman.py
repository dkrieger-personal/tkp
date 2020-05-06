import random
import json

class Game:
    def __init__(self, word):
        self.word = word
        self.guesses = {}

    def done(self):
        for m in self.status():
            if not m:
                return False
        return True

    def status(self):
        match = []
        for i in range(0, len(self.word)):
            if self.word[i] in self.guesses:
                match.append(True)
            else:
                match.append(False)
        return match

    def add_guess(self, letter):
        if letter not in self.guesses:
            self.guesses[letter] = True
            return True
        return False

    def __str__(self):
        s = ''
        m = self.status()
        for i in range(0, len(self.word)):
            if m[i]:
                s += word[i]
            else:
                s += '-'
        s += "    ("
        s += str(len(list(self.guesses)))
        s += " guesses)"
        return s


def get_word():
    with open('wordsapi_sample.json', encoding='utf-8') as f:
        words = json.load(f)
    index = random.randint(0, len(list(words)) - 1)
    while True:
        word = str(list(words)[index])
        if word.isalpha():
            return word
        index = (index + 1) % len(list(words))


def get_guess():
    while True:
        l = input('guess-->')
        if len(l) == 1 and l.isalpha():
            return l.lower()
        print("Guesses must be single letters between a and z")


if __name__ == '__main__':

    random.seed()
    word = get_word()
    print('Your word has this many letters: ', len(word))

    game = Game(word)

    while not game.done():
        guess = get_guess()
        if not game.add_guess(guess):
            print("You already guessed that")
            print(game)
            continue

        print(game)


