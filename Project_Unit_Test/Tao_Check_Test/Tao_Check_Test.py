import unittest
from Tao import Tao_Solve0, Tao_Solve_Broken_Max, Tao_Solve_Broken_Min, Tao_Solve_Broken_Modular

class TestTao(unittest.TestCase):
    def test_1(self):
        with open("Tao.in") as f_in:
            In=[line.split() for line in f_in]

        with open("Tao.out") as f_out:
            Out=[int(line.strip()) for line in f_out]

        for i in range(100):
            self.assertEqual(Tao_Solve0(int(In[i][0]), int(In[i][1])), Out[i])

    def test_2_Min(self):
        with open("Tao.in") as f_in:
            In=[line.split() for line in f_in]

        with open("Tao.out") as f_out:
            Out=[int(line.strip()) for line in f_out]

        for i in range(100):
            self.assertEqual(Tao_Solve_Broken_Min(int(In[i][0]), int(In[i][1])), Out[i])

    def test_3_Max(self):
        with open("Tao.in") as f_in:
            In=[line.split() for line in f_in]

        with open("Tao.out") as f_out:
            Out=[int(line.strip()) for line in f_out]

        for i in range(100):
            self.assertEqual(Tao_Solve_Broken_Max(int(In[i][0]), int(In[i][1])), Out[i])

    def test_4_Modular(self):
        with open("Tao.in") as f_in:
            In=[line.split() for line in f_in]

        with open("Tao.out") as f_out:
            Out=[int(line.strip()) for line in f_out]

        for i in range(100):
            self.assertEqual(Tao_Solve_Broken_Modular(int(In[i][0]), int(In[i][1])), Out[i])

if __name__== '__main__':
    unittest.main()