import unittest
from word_chain import read_date_from_csv, longest_str_chain


class CainTest(unittest.TestCase):

    def test_read(self):
        date = read_date_from_csv()
        self.assertEqual(date,
                         ['crates', 'car', 'cats', 'crate', 'rate', 'at', 'ate',
                          'tea', 'rat', 'a'])

    def test_longest_chain1(self):
        words = ['b', 'bcad', 'bca', 'bad', 'bd']

        self.assertEqual(4, longest_str_chain(words))

    def test_longest_chain2(self):
        words = ['crates', 'car', 'cats', 'crate', 'rate', 'at', 'ate',
                 'tea', 'rat', 'a']

        self.assertEqual(6, longest_str_chain(words))

    def test_longest_chain3(self):
        words = ['word', 'anotherword', 'yetanotherword']

        self.assertEqual(1, longest_str_chain(words))

    def test_longest_chain4(self):
        words = ["a", "b", "ba", "bca", "bda", "bdca"]

        self.assertEqual(4, longest_str_chain(words))


if __name__ == '__main__':
    unittest.main()
