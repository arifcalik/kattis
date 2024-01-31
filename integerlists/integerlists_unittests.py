import unittest
from integerlists import process_testcase

class TestIntegerLists(unittest.TestCase):
    def test_two(self):
        commands = "RRRRDRRRRR"
        n = 1
        input_array = [13]
        self.assertEqual(process_testcase(n, input_array, commands), [], "empty")
        
    def test_five(self):
        commands = "RRRRRDRRRRR"
        n = 0
        input_array = []
        self.assertEqual(process_testcase(n, input_array, commands), "error", "error")
    	
    def test_eleven(self):
        commands = "RRRRDRRRRRDRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
        n = 2
        input_array = [13, 7,]       
        self.assertEqual(process_testcase(n, input_array, commands), [], "error")

    def test_nine(self):
        commands = "RRRRDRRRRRDDRRRRRRRRRDRRDRRRRRRRRRRRRRRR"
        n = 5
        input_array = [3, 27, 0, -12, 5]
        self.assertEqual(process_testcase(n, input_array, commands), [], "Empty")

    def test_fiveA(self):
        commands = "RRRRRDRRRRR"
        n = 1
        input_array = [5]
        self.assertEqual(process_testcase(n, input_array, commands), [], "empty")

    def test_fiveB(self):
        commands = "RRRRRDRRRRRRRRRRDRRRRRRRRRRRRRRRRRRRRRRRRRR"
        n = 1
        input_array = [5]
        self.assertEqual(process_testcase(n, input_array, commands), "error", "error")


    def test_kattisA(self):
        commands = "RDD"
        n = 4
        input_array = [1,2,3,4]
        self.assertEqual(process_testcase(n, input_array, commands), [2,1], "error")

    def test_kattisC(self):
        commands = "DD"
        n = 1
        input_array = [42]
        self.assertEqual(process_testcase(n, input_array, commands), "error", "error")

    def test_kattisB(self):
        commands = "RRD"
        n = 6
        input_array = [1,1,2,3,5,8]
        self.assertEqual(process_testcase(n, input_array, commands), [1,2,3,5,8], "error")

    def test_kattisF(self):
        commands = "D"
        n = 0
        input_array = []
        self.assertEqual(process_testcase(n, input_array, commands), "error", "error")

    	    	
if __name__=='__main__':
	unittest.main()

import unittest

