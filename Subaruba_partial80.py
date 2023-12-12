#https://open.kattis.com/problems/subaruba
#https://en.wikipedia.org/wiki/Ubbi_dubbi
import random

VOWELS_LOWER = "aeiouy"
VOWELS_UPPER = "AEIOUY"

def encrypt(word):
    encrypted_word = ""
    for c in word:
        if c in VOWELS_LOWER:
            encrypted_word += "ub" + c
        elif c in VOWELS_UPPER:
            encrypted_word += "Ub" + c.lower()            
        else:
            encrypted_word += c
    return encrypted_word

def decrypt(word):
    decrypted_word = ""
    previous_index = 0
    capital = False
    for i, c in enumerate(word):
        if i < len(word) - 2:
            if (c == "u" or c == "U") and word[i + 1] == "b" and word[i + 2] in VOWELS_LOWER:
                decrypted_word += word[previous_index:i]    
                previous_index = i + 2
            if c == "U":
                capital = True
    decrypted_word += word[previous_index:]
    if capital:
        decrypted_word = decrypted_word.capitalize()    
    return decrypted_word
    
def main():
    mode = input()
    num_inputs = int(input())
    for _ in range(num_inputs):
        line = input().split()
        if mode == "D":
            for word in line:
                print(encrypt(word), end=" ")
        elif mode == "A":
            for word in line:
                print(decrypt(word), end=" ")
        else:
            print("Wrong mode")
        print()
                
        
if __name__=="__main__":
    main()

    
