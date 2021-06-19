#Importing library and DBT Solve
import unittest
import random
from DBT import *

#Creating class unittest
class TestDBT(unittest.TestCase):
        def test_1_manual(self):
                with open("DBT1.in", 'w+') as f_in:          # Creating new file input
                        with open("DBT1.out", 'w+') as f_out:    # Creating new file output
                                self.assertEqual(DBT_Solve1(1), DBT_Solve2(1))       # Testing DBT function if its work as expected 
                                f_in.write('1')                   # Write down test case to input file
                                f_out.write('{}'.format(DBT_Solve1(1)))  # Write down result to output file

                with open("DBT2.in", 'w+') as f_in:          # Creating new file input
                        with open("DBT2.out", 'w+') as f_out:    # Creating new file output
                                self.assertEqual(DBT_Solve1(int(1e12)), DBT_Solve2((int(1e12))))       # Testing DBT function if its work as expected 
                                f_in.write('1000000000000')                   # Write down test case to input file
                                f_out.write('{}'.format(DBT_Solve1(int(1e12))))  # Write down result to output file
        
        def test_2_auto(self):
                for i in range(3, 11):      # Create random 8 new input/output files
                        with open("DBT{}.in".format(i), 'w+') as f_in:
                                with open("DBT{}.out".format(i), 'w+') as f_out:                  
                                        n = random.randint(1, int(1e12))
                                        self.assertEqual(DBT_Solve1(int(1e12)), DBT_Solve2((int(1e12))))       # Testing DBT function if its work as expected 
                                        f_in.write('{}'.format(n))
                                        f_out.write('{}'.format(DBT_Solve1(n)))

if __name__ == "__main__":
    unittest.main()
    '''You can also run code in terminal. Exp: python -m unittest DBT_test'''