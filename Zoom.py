
def zoom(array, k):
    l = len(array)
    if k <= l:
        for i in range(k, l + 1, k):
            print(array[i - 1], end=' ')
        print()

def main():
    n, k = [int(num) for num in input().split()]
    array = [int(num) for num in input().split()]
    zoom(array, k)
    
if __name__=='__main__':
    main()
