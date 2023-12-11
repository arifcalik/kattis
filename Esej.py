# https://open.kattis.com/problems/esej
import random

MIN_SIZE_WORD = 6 # to guarantee unique words are more than maxi/2 use not 1char
MAX_SIZE_WORD = 15
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def create_word():
    width = random.randint(MIN_SIZE_WORD, MAX_SIZE_WORD)
    word = ""
    i = 0
    while i < width:
        word += random.choice(ALPHABET)
        i += 1
    return word

def main():
    while True:
        mini, maxi = [int(num) for num in input().split()]
        num_words = 0
        while num_words < (mini + maxi) // 2:
            print(create_word(), end=' ')
            num_words += 1
        print()
        
if __name__=="__main__":
    main()

    
