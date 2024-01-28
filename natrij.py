# https://open.kattis.com/problems/natrij
import logging

def setup():
    logging.basicConfig(level=logging.INFO)

def process_subtraction(t1, t2):
    logging.debug(f"DEBUG: t1={t1}, t2={t2}")
    diff = [0,0,0]
    
    if t2[2] < t1[2]:
        t2[1] -= 1
        t2[2] += 60
    diff[2] = t2[2] - t1[2]
    
    if t2[1] < t1[1]:
        t2[0] -= 1
        t2[1] += 60
    diff[1] = t2[1] - t1[1]
    
    if t2[0] < t1[0]:
        t2[0] += 24    
    diff[0] = t2[0] - t1[0]
    # exception:
    if diff[2] == 0 and diff[1] == 0 and diff[0] == 0:
        diff[0] = 24
    diff = list(map(str,diff))
    res = ""
    for i, part in enumerate(diff):
        if len(part) < 2:
            res += '0' + part
            if i != len(diff) - 1:
                res += ':'
        else:
            res += part
            if i != len(diff) - 1:
                res += ':'
                
    logging.debug(f"DEBUG: diff={res}")
    return res

def main():
    setup()
    start = [h1, m1, s1] = list(map(int, input().split(':')))
    logging.debug(f"DEBUG: h={h1}, m={m1}, s={s1}")
    stop = [h2, m2, s2] = list(map(int, input().split(':')))
    logging.debug(f"DEBUG: h={h2}, m={m2}, s={s2}")
    diff = process_subtraction(start,stop)
    print(diff)
            
if __name__=="__main__":
    main()

