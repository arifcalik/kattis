
def main():
    n = int(input())
    for _ in range(n):
        set_number, decimal = [num for num in input().split()]
        for digit in list(decimal):
            if digit >= '8':
                octal = 0
                break
        else:
            octal = int(decimal, 8)
        print(set_number, octal, int(decimal, 10), int(decimal, 16))
        

if __name__=='__main__':
    main()
