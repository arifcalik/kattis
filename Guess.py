# https://open.kattis.com/problems/guess
import logging

def setup():
    logging.basicConfig(level=logging.INFO)

def guess_number():
    higher = 1000
    lower = 1

    while True:
        guess = (higher + lower) // 2
        print(guess)
        feedback = input()
        if feedback == "correct":
            return
        elif feedback == "higher":
            lower = guess + 1
        elif feedback == "lower":
            higher = guess - 1
        
def main():
    setup()
    guess_number()

if __name__=="__main__":
    main()

