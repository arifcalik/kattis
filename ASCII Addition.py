#https://open.kattis.com/problems/asciiaddition
digits_encoded = [
    [ 
        'xxxxx',
        'x...x',
        'x...x',
        'x...x',
        'x...x',
        'x...x',        
        'xxxxx',
],
    [ 
        '....x',
        '....x',
        '....x',
        '....x',
        '....x',
        '....x',     
        '....x',   
],
    [ 
        'xxxxx',
        '....x',
        '....x',        
        'xxxxx',
        'x....',
        'x....',        
        'xxxxx',
],
    [ 
        'xxxxx',
        '....x',
        '....x',        
        'xxxxx',
        '....x',
        '....x',
        'xxxxx',        
],
    [ 
        'x...x',
        'x...x',
        'x...x',        
        'xxxxx',
        '....x',
        '....x',
        '....x',        
],
    [ 
        'xxxxx',
        'x....',
        'x....',        
        'xxxxx',
        '....x',
        '....x',        
        'xxxxx',        
],
    [ 
        'xxxxx',
        'x....',
        'x....',        
        'xxxxx',
        'x...x',
        'x...x',        
        'xxxxx',
],
        [ 
        'xxxxx',
        '....x',
        '....x',
        '....x',
        '....x',
        '....x',
        '....x',
],
        [ 
        'xxxxx',
        'x...x',
        'x...x',        
        'xxxxx',
        'x...x',
        'x...x',        
        'xxxxx',
],
    [ 
        'xxxxx',
        'x...x',
        'x...x',        
        'xxxxx',
        '....x',
        '....x',        
        'xxxxx',
],
    [ 
        '.....',
        '..x..',
        '..x..',        
        'xxxxx',
        '..x..',
        '..x..',       
        '.....',
],     
]

MAX_ROWS = 7
MAX_COLUMNS = 5

def display_sum(number):
    for row in range(MAX_ROWS):
        for i, digit in enumerate(number):
            if i < len(number) - 1:
                print(digits_encoded[int(digit)][row], end='.')
            else:
                print(digits_encoded[int(digit)][row])
        

def construct_digits(line, digits, row_index):
    col_index = 0
    while col_index < len(line) - 1:
        row_str = line[col_index:col_index + MAX_COLUMNS]
        if not row_index:
            digit = []
            digit.append(row_str)
            digits.append(digit)
        else:
            digits[col_index // 6].append(row_str)
            
        col_index += MAX_COLUMNS + 1

def decode_digits(digits):
    number1 = ""
    number2 = ""
    number = ""
    for digit in digits:
        for i, digit_encoded in enumerate(digits_encoded):
            if all(x == y for x, y in zip(digit, digit_encoded)):
                if i != 10:
                    number += str(i)
                    break
                else:
                    number1 = number
                    number = ""
    number2 = number
    return (int(number1) + int(number2))
    

def main():
    digits = []
    for i in range(MAX_ROWS):
        line = input()  #multiple of 5 ascii chars of . or x
        construct_digits(line, digits, i)

    result = decode_digits(digits)
    display_sum(str(result))

if __name__=='__main__':
    main()


