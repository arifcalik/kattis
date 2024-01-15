

def main():
    n = int(input())
    num = n
    while num >= n:
        digits_sum = 0
        num_copy = num
        while num_copy:
            digits_sum += num_copy % 10
            num_copy //= 10

        if(num % digits_sum == 0):
            print(num)
            break
    
        num += 1
            
            
if __name__ == '__main__':
    main()
