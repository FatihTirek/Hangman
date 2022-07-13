from colorama import Fore, Style, init

def guessWord(word : str, lives : int):
    while True:
        inp = input('Your guess: ')

        if not inp.isalpha():
            print(f'\n{Fore.LIGHTRED_EX}Only alpha{Style.RESET_ALL}')
            continue
        elif inp.lower() == word:
            return True
        else:
            return lives - 2


def getIndexes(word : str, letter : str):
    indexes = list()

    for i in range(len(word)):
        if word[i] == letter:
            indexes.append(i)
    
    return indexes


def start(word : str):
    init()
    final_word = (len(word) * '_ ').split()
    used_letters = []
    lives = 10

    print(f'{Fore.LIGHTYELLOW_EX}Info: {Style.RESET_ALL}If you can\'t guess the word correctly you will lose 2 lives\n')

    while True:
        print(Fore.LIGHTBLUE_EX + ' '.join(final_word) + Style.RESET_ALL)
        if len(used_letters) != 0:
            print(Fore.LIGHTGREEN_EX + '\nUsed letters: ' + ','.join(used_letters) + Style.RESET_ALL)
        inp = input('\nEnter a letter: (Enter 1 to guess the word) -> ')
        print()

        if inp == '1':
            result = guessWord(word, lives)
            if result is True:
                print('\nWell Done :)')
                break
            else:
                used_letters.append(inp.lower())
                if result < 0:
                    print(f'\n{Fore.LIGHTRED_EX}Game Over, you have consumed all your lives{Style.RESET_ALL}\n')
                    print(f'{Fore.LIGHTMAGENTA_EX}Word was: {word}{Style.RESET_ALL}')
                    break
                else:
                    lives = result
                    print(f'{Fore.LIGHTGREEN_EX}Try again, remaining lives: {lives}{Style.RESET_ALL}\n')
                    continue
        elif not inp.isalpha():
            print(f'{Fore.LIGHTRED_EX}Only alpha!{Style.RESET_ALL}\n')
            continue
        elif len(inp) != 1:
            print(f'{Fore.LIGHTRED_EX}Only one letter{Style.RESET_ALL}\n')
            continue
        else:
            letter = inp.lower()
            used_letters.append(letter)
            indexes = getIndexes(word, letter)

            if len(indexes) == 0:
                if lives == 0:
                    print(f'{Fore.LIGHTRED_EX}Game Over, you have consumed all your lives{Style.RESET_ALL}\n')
                    print(f'{Fore.LIGHTMAGENTA_EX}Word was: {word}{Style.RESET_ALL}')
                    break
                lives -= 1
                print(f'{Fore.LIGHTGREEN_EX}Try again, remaining lives: {lives}{Style.RESET_ALL}\n')
                continue
            else:
                for i in range(len(word)):
                    if i in indexes:
                        final_word[i] = letter
                        
                if ''.join(final_word) == word:
                    print(Fore.LIGHTBLUE_EX + ' '.join(final_word) + Style.RESET_ALL)
                    print('\nWell Done :)')
                    break