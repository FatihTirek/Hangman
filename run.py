from random import randint
from main import start
from words import word_list

while True:
    print('\n1-) Start\n2-) Exit')

    inp = input('no: ')

    if inp == '1':
        word_rank = randint(0,573)
        word = word_list[word_rank].td.text
        start(word)
    else:
        quit()