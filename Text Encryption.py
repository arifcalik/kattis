
def create_indices(width, length):
    indices = []
    j = 0
    while len(indices) < length:
        indices.append(j)
        j += width
        if j >= length:
            j = j%width + 1
    return indices
                

def encrypt(indices, s):
    i = 0
    l = len(s)
    encrypted_s = {}
    while i < l:
        encrypted_s[indices[i]] = s[i]
        i += 1
    return dict(sorted(encrypted_s.items(), key=lambda item: item[0]))

def main():
    while True:
        width = int(input())
        if width == 0:
            break
        line = input().replace(' ','').upper()
        indices = create_indices(width, len(line))
        res = encrypt(indices, line)
        for value in res.values():
            print(value,end='')
        print()
        

if __name__=="__main__":
    main()

    
