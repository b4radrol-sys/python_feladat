import unittest

def cucc(a: int, b: int):
    parososz = 0
    for i in range(a, b+1):
        if i % 2 == 0:
            parososz += i
    return parososz        

print(cucc(42, 100))

class TestParosokFunction(unittest.TestCase):

    def test_joszam(self):
        self.assertEqual(cucc(42, 100), 2130)

    def test_joszam1(self):
        self.assertGreater(cucc(0, 10), 0)

    def test_joszam2(self):
        self.assertLess(cucc(-40, -10), 0)

if __name__ == '__main__':
    unittest.main()