COEFFS = "432765-4321"

def check_validity(cpr):
    l = len(cpr)
    sum = 0
    for i in range(l):
        if i != 6:
            sum += int(cpr[i]) * int(COEFFS[i])
    return 1 if sum % 11 == 0 else 0
    
def main():    
    cpr = input()
    print(check_validity(cpr))

if __name__=='__main__':
    main()
