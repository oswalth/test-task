import json

alph = 'abcdefghijklmnopqrstuvwxyz'
vocabulary = {}
with open('words_alpha.txt', 'r') as f_obj:
    for line in f_obj:
        letter = line[0]
        if letter in list(vocabulary.keys()):
            vocabulary[letter].append(line.rstrip('\n\r'))
        else:
            vocabulary[letter] = [line.rstrip('\n\r')]

with open('vocabulary.json', 'w') as file_obj:
    json.dump(vocabulary, file_obj)