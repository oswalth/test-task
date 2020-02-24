import pickle
import random
from collections import deque
import json


class Hasher:
    def __init__(self, variants_number=1, words_limit=None, separator=''):
        self.words_limit = words_limit
        self.variants_number = variants_number
        self.variants = []
        self.hashed_alphas = []
        self.separator = separator
        self.load_dict()


    def load_dict(self):
        with open('vocabulary.json', 'r') as f_obj:
            self.dictionary = json.load(f_obj)
            self.keys = list(self.dictionary.keys())


    def hasher(self, value_to_hash):
        hash_val = hash(pickle.dumps(value_to_hash))
        hashed = str(hash_val if hash_val > 0 else hash_val * (-1))
        i = 0
        random.seed(hashed[-3:])
        while i < len(hashed) and len(self.hashed_alphas) <= self.words_limit:

            if 1 <= int(hashed[i]) <= 2 and int(hashed[i] + hashed[i + 1]) <= 24:
                letter = self.keys[int(hashed[i] + hashed[i + 1])]
                self.hashed_alphas.append(self.dictionary[letter][random.randrange(self.dictionary[letter].__len__())])
                i += 2
                continue
            letter = self.keys[int(hashed[i])]
            self.hashed_alphas.append(self.dictionary[letter][random.randrange(self.dictionary[letter].__len__())])
            i += 1
        self.output()
        

    def output(self):
        items = deque(self.hashed_alphas)
        for i in range(self.variants_number):
            print('Variant #{} is {}'.format(i + 1, self.separator.join(x.capitalize() for x in items)))
            items.rotate(1)


if __name__ == '__main__':
    hasher = Hasher(2, 5, separator='_')
    hasher.hasher({'vasya': ['antot', [25, True]]})