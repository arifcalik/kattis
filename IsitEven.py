https://open.kattis.com/problems/isiteven
def main():
    n, k = [int(num) for num in input().split()]
    counts_divisor2 = 0
    for _ in range(n):
        num = int(input())
        while True:
            if num % 2 == 0:
                counts_divisor2 += 1
                num //= 2
            else:
                break
        if counts_divisor2 >= k:
            print(1)
            return
    print(0)
    
if __name__ == '__main__':
    main()
