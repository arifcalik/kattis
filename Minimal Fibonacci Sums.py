
fibs38 = (
1,
2,
3,
5,
8,
13,
21,
34,
55,
89,
144,
233,
377,
610,
987,
1597,
2584,
4181,
6765,
10946,
17711,
28657,
46368,
75025,
121393,
196418,
317811,
514229,
832040,
1346269,
2178309,
3524578,
5702887,
9227465,
14930352,
24157817,
39088169,
63245986,
102334155,
165580141,
267914296,
433494437,
701408733,)

# helper one
def fibonacci(n):
    num1 = 0
    num2 = 1
    i = 0
    while i < n:
        # print(f"{num1+num2}")
        num1, num2 = num2, num1 + num2
        i += 1

def find_max_fibo(number):
    for i in range(len(fibs38) - 1, 0, -1):
        if number >= fibs38[i]:
            return i

def find_min_sum(number):
    series = []
    i = find_max_fibo(number)
    while number:
        if fibs38[i] <= number:
            number -= fibs38[i]
            series.append(fibs38[i])            
        else:
            i -= 1
    
    for fib in series[::-1]:
        print(fib, end=' ')

def main():
    num = int(input())
    find_min_sum(num)

if __name__=="__main__":
    main()

    
