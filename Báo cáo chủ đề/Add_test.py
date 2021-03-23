#Importing library and Add function
import unittest
import random
from Add import Add

#Creating class unittest
class TestAdd(unittest.TestCase):
    def test_1_manual(self):
        with open("Add.in", 'w+') as f_in:          #Creating new file input
            with open("Add.out", 'w+') as f_out:    #Creating new file output
                self.assertEqual(Add(3,5), 8)       #Testing Add function if its work as expected 
                f_in.write('3 5')                   #Write down test case to input file
                f_out.write('{}'.format(Add(3,5)))  #Write down result to output file

    def test_2_auto(self):
        with open("Add.in", 'a+') as f_in:
            with open("Add.out", 'a+') as f_out:    
                for _ in range(100):                   #Random 100 cases
                    x=random.randint(-100,100)
                    y=random.randint(-100,100)
                    self.assertEqual(Add(x,y), x+y)    #Comparision with a true function
                    f_in.write('\n{} {}'.format(x,y))
                    f_out.write('\n{}'.format(Add(x,y)))

if __name__ == "__main__":
    unittest.main()
    '''You can also run code in terminal. Exp: python -m unittest Add_test'''
