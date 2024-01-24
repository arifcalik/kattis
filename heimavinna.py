def parse(s):
    total = 0
    for subs in s.split(';'):
        if '-' not in subs:
            total += 1
        else:
            start, stop = [int(num) for num in subs.split('-')]
            total +=  stop - start + 1

    return total
        
def main():
    line = input()
    print(parse(line))
        
if __name__=="__main__":
    main()
