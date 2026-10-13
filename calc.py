import unittest

def calc(a: float, b: float, c: str):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b

class TestCalcFunction(unittest.TestCase):

    def test_jo_osszeadas(self):
        self.assertGreater(calc(5, 3, "+"), 0)

    def test_jo_kivonas(self):
        self.assertLess(calc(10, 7, "-"), 10)

    def test_jo_szorzas(self):
        self.assertGreater(calc(4, 2, "*"), 4)

    def test_jo_osztas(self):
        self.assertLess(calc(9, 3, "/"), 9)

if __name__ == '__main__':
    unittest.main()

print(calc(int(input("1. szám: ")), int(input("2. szám: ")), input("művelet: ")))