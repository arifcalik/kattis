
def main():
    nums = [int(num) for num in input().split()]
    order = input()
    A, B, C = sorted(nums)

    dic = {'A':A, 'B':B, 'C':C}
    print(dic[order[0]], dic[order[1]], dic[order[2]])

    
if __name__ == '__main__':
    main()
