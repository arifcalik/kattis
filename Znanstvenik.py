def check_same_columns(columns):
    i = 1    
    while True:
        new_columns = []
        for col in columns:
            new_columns.append(col[i:])
        if len(columns) != len(set(new_columns)):
            return i - 1
        else:
            i += 1
        if i == len(columns[0]):
            return i - 1

def main():
    r, c = [int(num) for num in input().split()]
    columns = []
    for rindex in range(r):
        i = 0
        row = input()
        for _ in range(c):
            if not rindex:
                col = ""
                col += row[i]
                columns.append(col)
            else:
                columns[i] += row[i]
            i += 1
    #print(columns)
    print(check_same_columns(columns))

if __name__=='__main__':
    main()
