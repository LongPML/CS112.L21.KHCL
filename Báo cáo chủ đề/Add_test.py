#Importing library and Add function
import unittest
import random
from Add import Add

#Creating class unittest
class TestAdd(unittest.TestCase):
    def test_1_manual(self):
        with open("Add1.in", 'w+') as f_in:          # Creating new file input
            with open("Add1.out", 'w+') as f_out:    # Creating new file output
                self.assertEqual(Add(3,5), 8)       # Testing Add function if its work as expected 
                f_in.write('3 5')                   # Write down test case to input file
                f_out.write('{}'.format(Add(3,5)))  # Write down result to output file

    def test_2_auto(self):
        for i in range(2, 6):      # Create random 4 new input/output files
            with open("Add{}.in".format(i), 'w+') as f_in:
                with open("Add{}.out".format(i), 'w+') as f_out:                  
                    x=random.randint(-100,100)
                    y=random.randint(-100,100)
                    self.assertEqual(Add(x,y), x+y)    # Comparision with a true function
                    f_in.write('{} {}'.format(x,y))
                    f_out.write('{}'.format(Add(x,y)))

if __name__ == "__main__":
    unittest.main()
    '''You can also run code in terminal. Exp: python -m unittest Add_test'''
