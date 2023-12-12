ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shift(word, key):
    MAX_INDEX = len(ALPHABET)
    encrypted_word = ""
    for i, c in enumerate(word):
        if i % 2:
            encrypted_word += ALPHABET[(ALPHABET.index(c) + ALPHABET.index(key[i])) % MAX_INDEX]
        else:
            encrypted_word += ALPHABET[(ALPHABET.index(c) - ALPHABET.index(key[i]) + MAX_INDEX) % MAX_INDEX]

    return encrypted_word

def main():    
    word = input()
    key = input()    
    print(shift(word, key))

if __name__=='__main__':
    main()
