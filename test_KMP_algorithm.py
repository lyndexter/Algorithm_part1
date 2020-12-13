import unittest
from KMP_algorithm_modified import find_substring


class TestDFA(unittest.TestCase):

    def test1(self):
        self.assertEqual([9], find_substring("rfgdgekesefes", "efes"))

    def test2(self):
        self.assertEqual([], find_substring("rfgdgekesfes", "efes"))

    def test3(self):
        self.assertEqual([9, 15], find_substring("rfgdgekesefesddefes", "efes"))

    def test4(self):
        self.assertEqual([21],
                         find_substring("rfgdgekesefesekedredseker dsdsa",
                                        "eker"))

    def test5(self):
        self.assertEqual([0], find_substring("efes", "efes"))

    def test6(self):
        self.assertEqual([0, 11, 37],
                         find_substring(
                             "efesseffereefesfesfsefsfesfefsefefsefefesfsfse",
                             "efes"))

    def test7(self):
        self.assertEqual([0, 20],
                         find_substring("efesfessrefdergefsdfefesfdgsef",
                                        "efes"))


    def test8(self):
        self.assertEqual([0, 2],
                         find_substring("efefefesefes",
                                        "efef"))


if __name__ == '__main__':
    unittest.main()
