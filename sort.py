# https://open.kattis.com/problems/sort
import logging

def setup():
    logging.basicConfig(level=logging.INFO)

        
def main():
    setup()
    n, maxi = list(map(int, input().split()))

    freq = {}
    for num in list(map(int, input().split())):
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    logging.debug(f"DEBUG: Found freq={freq}")
    
    sorted_freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
    logging.debug(f"DEBUG: Found sorted_freq={sorted_freq}")
    for num, f in sorted_freq.items():
        print(f"{num} "*f, end='')
    
if __name__=="__main__":
    main()

