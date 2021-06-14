import unittest
import os
from Tao import Tao_Solve0, Tao_Solve_Broken_Max, Tao_Solve_Broken_Min, Tao_Solve_Broken_Modular

class TestTao(unittest.TestCase):
    def test_1(self):
        for i in range(len(os.listdir(os.listdir(os.getcwd())[0]))):
            with open(f"{os.listdir(os.getcwd())[0]}/{os.listdir(os.listdir(os.getcwd())[0])[i]}") as f_in:
                n, k = [int(x) for x in f_in.readline().split()]

            with open(f"{os.listdir(os.getcwd())[1]}/{os.listdir(os.listdir(os.getcwd())[1])[i]}") as f_out:
                Ans = int(f_out.readline())

            self.assertEqual(Tao_Solve0(n, k), Ans)

    def test_2_Min(self):
        for i in range(len(os.listdir(os.listdir(os.getcwd())[0]))):
            with open(f"{os.listdir(os.getcwd())[0]}/{os.listdir(os.listdir(os.getcwd())[0])[i]}") as f_in:
                n, k = [int(x) for x in f_in.readline().split()]

            with open(f"{os.listdir(os.getcwd())[1]}/{os.listdir(os.listdir(os.getcwd())[1])[i]}") as f_out:
                Ans = int(f_out.readline())

            self.assertEqual(Tao_Solve_Broken_Min(n, k), Ans)

    def test_3_Max(self):
        for i in range(len(os.listdir(os.listdir(os.getcwd())[0]))):
            with open(f"{os.listdir(os.getcwd())[0]}/{os.listdir(os.listdir(os.getcwd())[0])[i]}") as f_in:
                n, k = [int(x) for x in f_in.readline().split()]

            with open(f"{os.listdir(os.getcwd())[1]}/{os.listdir(os.listdir(os.getcwd())[1])[i]}") as f_out:
                Ans = int(f_out.readline())

            self.assertEqual(Tao_Solve_Broken_Max(n, k), Ans)

    def test_4_Modular(self):
        for i in range(len(os.listdir(os.listdir(os.getcwd())[0]))):
            with open(f"{os.listdir(os.getcwd())[0]}/{os.listdir(os.listdir(os.getcwd())[0])[i]}") as f_in:
                n, k = [int(x) for x in f_in.readline().split()]

            with open(f"{os.listdir(os.getcwd())[1]}/{os.listdir(os.listdir(os.getcwd())[1])[i]}") as f_out:
                Ans = int(f_out.readline())

            self.assertEqual(Tao_Solve_Broken_Modular(n, k), Ans)

if __name__== '__main__':
    unittest.main()