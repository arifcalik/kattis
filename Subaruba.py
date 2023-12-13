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
    l = len(word)
    i = 0
    while i < l:
        if not capital and word[i] == "U":
            capital = True        
        if i < l - 2 and (word[i] == "u" or word[i] == "U") and word[i + 1] == "b" and word[i + 2] in VOWELS_LOWER:
            decrypted_word += word[i + 2]
            i += 3
        else:
            decrypted_word += word[i]
            i += 1
    # decrypted_word += word[-1:]
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

"""
SPOILER ALERT:

As has been mentioned a few times in the past, Sara is rather odd. Sara and her best friend were both in Kubópavogur College. They conversed frequently, whether the subject was their studies, entertainment or their peers. 

Since certain topics were sensitive, Sara did not want the people around them to understand what was being discussed. Sara studied languages and was therefore quite adept at learning languages few people would understand. She could not use any language at all though. It had to be rare that another person at her school could understand conversations in that language. Thus, Sara decided common spoken languages should be avoided, for example Icelandic, English, French or other languages that may be the native language of some people. 

Sara searched for an encryption method instead. Contemporary encryption methods were mostly based on number theory. Since she was not a math whiz she searched for other methods. 

Sara found the language game Ubbi dubbi and decided to use it to encrypt her conversations. The game involved adding a ub in front of each vowel sound. Sara put a lot of effort into learning to speak Icelandic in an encrypted manner and then took the time to teach her friend. Sara and her friend speak and understand the encrypted language fluently. 

Hannes is also a friend of Sara and sometimes she speaks the encrypted language to him. Unfortunately, he has a harder time with the language. He understand the rules but needs a little more time to translate back and forth. Therefore, Hannes decides he needs a program to help him encrypt and decrypt his communication with Sara. 

Luckily, Hannes graduated as a computer scientist and knowns how to program. As fate would have it, he is busy writing software which prevents aircraft collisions. He asks you to complete this task for him. Can you write the program?
"""

    
