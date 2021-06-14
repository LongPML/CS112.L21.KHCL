import unittest
import random
from Tao import Tao_Solve0, Tao_Solve1

class TestTao(unittest.TestCase):
    def test_1_manual(self):
        with open("Tao1.in", 'w+') as f_in:
            with open("Tao1.out", 'w+') as f_out:
                self.assertEqual(Tao_Solve0(1,1), Tao_Solve1(1,1))
                f_in.write('1 1')
                f_out.write('{}'.format(Tao_Solve0(1,1)))

        with open("Tao2.in", 'w+') as f_in:
            with open("Tao2.out", 'w+') as f_out:
                self.assertEqual(Tao_Solve0(int(1e3), int(1e5)), Tao_Solve1(int(1e3), int(1e5)))
                f_in.write('1000 100000')
                f_out.write('{}'.format(Tao_Solve0(int(1e3), int(1e5))))

    def test_2_auto(self):
        for i in range(3, 5):
            with open("Tao{}.in".format(i), 'w+') as f_in:
                with open("Tao{}.out".format(i), 'w+') as f_out:    
                    n=random.randint(1, 1000)
                    k=random.randint(1, int(1e5))
                    self.assertEqual(Tao_Solve0(n,k), Tao_Solve1(n,k))
                    f_in.write('{} {}'.format(n,k))
                    f_out.write('{}'.format(Tao_Solve0(n,k)))

if __name__ == "__main__":
    unittest.main()