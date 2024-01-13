import re


def main():
    pattern = re.compile(r'0[xX][0-9a-fA-F]+')
    while True:
        try:
            line = input()
            matches = re.findall(pattern, line)
            for match in matches:
                print(match, int(match[2:], 16))
        except EOFError:
            break
        
if __name__=='__main__':
    main()
