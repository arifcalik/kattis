# https://open.kattis.com/problems/integerlists
import logging

def setup():
    logging.basicConfig(level=logging.INFO)

def process_testcase(size, array, commands):
    logging.debug(f"DEBUG: size={size} input={array} command set={commands}")
    count_reverse = 0
    for i, command in enumerate(commands):
        if command == 'R':
            count_reverse += 1
            logging.debug(f"DEBUG: just increase ReverseCount={count_reverse}")
        else:
            if count_reverse and count_reverse % 2 != 0:
                if array:
                    array.reverse()
                    logging.debug(f"DEBUG: ReverseCount={count_reverse} apply")
                    count_reverse = 0                    
            if array:
                array = array[1:len(array)]
                logging.debug(f"DEBUG: Delete={array} apply")
                # no more processing needed!
                if not array:
                    if 'D' not in commands[i+1:]:
                        return []
                    else:
                        return "error"
            else:        
                return "error"

    if count_reverse and count_reverse % 2 != 0:
        if array:
            array.reverse()
            logging.debug(f"DEBUG: Just reverse={count_reverse}")
        else:
            return []
        
    logging.debug(f"DEBUG: Returning array={array}")
    return array
        
def main():
    setup()
    testcases = int(input())
    for _ in range(testcases):
        commands = input()
        n = int(input())
        input_s = input()[1:-1]
        if input_s:
            input_array = list(map(int, input_s.split(",")))
        else:
            input_array = ""
        result = process_testcase(n, input_array, commands)
        print(result)
        

    logging.debug(f"DEBUG: result={result}")
    
if __name__=="__main__":
    main()

