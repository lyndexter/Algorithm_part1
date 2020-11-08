import unittest

from career_by_adding import Company


class CareerTest(unittest.TestCase):

    def test_find_max_experience1(self):
        company=Company()
        company.layers=[[4], [3, 1], [2, 1, 5], [1, 3, 2, 1]]
        company.num_layers=4
        self.assertEqual(company.find_max_experience(),12)

    def test_find_max_experience2(self):
        company = Company()
        company.layers = [[0], [1, 1], [0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1, 0]]
        company.num_layers = 5
        self.assertEqual(company.find_max_experience(), 3)

    def test_find_max_experience3(self):
        company = Company()
        company.layers = [[0], [5, 8], [6, 1, 1], [1, 8, 10, 3], [1, 6, 2, 10, 0], [9, 4, 7, 3, 3, 0]]
        company.num_layers = 6
        self.assertEqual(company.find_max_experience(), 32)

    def test_find_max_experience4(self):
        company = Company()
        company.layers = [[0], [5, 8], [6, 1, 1], [1, 8, 10, 3], [1, 6, 2, 11, 0], [9, 4, 7, 3, 3, 0]]
        company.num_layers = 6
        self.assertEqual(company.find_max_experience(), 33)

    def test_find_max_experience5(self):
        company = Company()
        company.layers = [[99999]]
        company.num_layers = 1
        self.assertEqual(company.find_max_experience(), 99999)


if __name__ == '__main__':
    unittest.main()

