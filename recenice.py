# https://open.kattis.com/problems/recenice
import logging

MAX = 1000
numbers_text = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "10":"ten",
    "11":"eleven",
    "12":"twelve",
    "13":"thirteen",
    "14":"fourteen",
    "15":"fifteen",
    "16":"sixteen",
    "17":"seventeen",
    "18":"eighteen",
    "19":"nineteen",
    "20":"twenty",
    "30":"thirty",
    "40":"forty",
    "50":"fifty",
    "60":"sixty",
    "70":"seventy",
    "80":"eighty",
    "90":"ninety",
    "100":"onehundred",
    "200":"twohundred",
    "300":"threehundred",
    "400":"fourhundred",
    "500":"fivehundred",
    "600":"sixhundred",
    "700":"sevenhundred",
    "800":"eighthundred",
    "900":"ninehundred",
}

def setup():
    logging.basicConfig(level=logging.INFO)

def verbal(num):
    verbal = ""
    if num <= 20:
        verbal += numbers_text[str(num)]
    elif num < 100:
        tens = num // 10
        ones = num % 10
        
        verbal += numbers_text[str(tens*10)]
        if ones != 0:
            verbal += numbers_text[str(ones)]
            
    elif num < 1000:
        hundreds = num // 100
        ones = num % 10
        if num % 100 > 20:
            tens = num % 100 - ones
        else:
            tens = num % 100
            ones = 0
        
        verbal += numbers_text[str(hundreds*100)]
        if tens != 0:
            verbal += numbers_text[str(tens)]        
        if ones != 0:
            verbal += numbers_text[str(ones)]
            
    return verbal
        
def match_number(words):
    total_len = 0
    i_replace = 0
    for index, word in enumerate(words):
        if word != "$":
            total_len += len(word)
        else:
            i_replace = index        
    logging.debug(f"DEBUG: total_len={total_len}")

    for i in range(total_len + 1, MAX):
        if total_len + len(verbal(i)) == i:
            logging.debug(f"DEBUG: Found len={i}")
            words[i_replace] = verbal(i) 
            return i

def main():
    setup()
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for word in words:
        logging.debug(f"DEBUG: word={word}")
        
    res = match_number(words)
    for word in words:
        print(word, end=' ')

if __name__=="__main__":
    main()

