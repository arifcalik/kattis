# https://open.kattis.com/problems/dasblinkenlights
def main():
    p, q, s = list(map(int, input().split()))
    okek = 1
    divisor = 2
    while p > 1 or q > 1:
        if p % divisor == 0 and q % divisor == 0:
            okek *= divisor
            p //= divisor
            q //= divisor
        elif p % divisor == 0:
            okek *= divisor
            p //= divisor
        elif q % divisor == 0:
            okek *= divisor
            q //= divisor
        else:
            if divisor % 2 == 0:
                divisor += 1
            else:
                divisor += 2
    if(okek <= s):
        print("yes")
    else:
        print("no")
            
if __name__=="__main__":
    main()
