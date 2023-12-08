#https://open.kattis.com/problems/perket
from itertools import combinations
 

def min_diff(ingredients):
    min_diff = 100000000
    for i in range(1, len(ingredients) + 1):
        comb = combinations(ingredients, i)
        sourness = 1
        bitterness = 0

        for j in list(comb):
            # print (j)
            for item in j:
                sourness *= item[0]
                bitterness += item[1]

            diff = abs(bitterness - sourness)
            sourness = 1
            bitterness = 0

            if diff < min_diff:
                min_diff = diff

    return min_diff

def main():
    n = int(input())
    ingredients = []
    for _ in range(n):
        sourness, bitterness = [int(num) for num in input().split()]
        ingredients.append((sourness, bitterness))

    print(min_diff(ingredients))
        
if __name__=='__main__':
    main()


