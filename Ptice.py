
ADRIAN_SEQ = "ABC"
BRUNO_SEQ = "BABC"
GORAN_SEQ = "CCAABB"

def main():
    n = int(input())
    keys = list(input())
    total_adrian = 0
    total_bruno = 0
    total_goran = 0
    for i, letter in enumerate(keys):
        total_adrian += int(letter == ADRIAN_SEQ[i % len(ADRIAN_SEQ)])
        total_bruno += int(letter == BRUNO_SEQ[i % len(BRUNO_SEQ)])
        total_goran += int(letter == GORAN_SEQ[i % len(GORAN_SEQ)])

    maxi = max(total_adrian, total_bruno, total_goran)
    print(maxi)
    if total_adrian == maxi:
        print('Adrian')
    if total_bruno == maxi:
        print('Bruno')
    if total_goran == maxi:
        print('Goran')
        
if __name__ == '__main__':
    main()
