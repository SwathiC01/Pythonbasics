import itertools
import string
import time
from typing import Union

def common_guess(word: str) -> str:
    with open('words.txt', 'r') as words:
        word_list: list[str] = words.read().splitlines()

    for i, match in enumerate(word_list):
        if word == match:
            return f'Common match: {match} (#{i})'
        
def brute_force(word: str, length: int, digits: bool = False, symbols: str = False) -> Union[str, None]:
    chars = string.ascii_lowercase

    if digits:
        chars+=string.digits

    if symbols:
        chars+=string.punctuation

    attemps=0
    for guess in itertools.product(chars, repeat=length):
        attemps+=1
        guess: str = ''.join(guess)

        if guess==word:
            return f'"{word}" was cracked in {attemps} guesses'
        
        print(guess, attemps)
        

def main():
    print('Searching....')
    password: str = 'abc1'

    start_time: float = time.perf_counter()

    common_match = common_guess(password)
    if common_match:
        print(common_match)
    else:
        cracked=brute_force(password, length=4, digits=False, symbols=False)
        if cracked:
            print(cracked)
        else:
            print("There was no match...")

    end_time: float = time.perf_counter()
    print(round(end_time-start_time, 2), 's')

if __name__ == '__main__':
    main()