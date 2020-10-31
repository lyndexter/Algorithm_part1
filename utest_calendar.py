import unittest
import calendar


class CalendaTest(unittest.TestCase):

    def test_quicksort(self):
        list = [(5, 2), (6, 8), (12, 6), (7, 8), (9, 5), (12, 1), (23, 2),
                (76, 5)]
        result = [(5, 2), (6, 8), (7, 8), (9, 5), (12, 1), (12, 6), (23, 2),
                  (76, 5)]
        calendar.quicksort(list, 0, len(list) - 1)
        self.assertEqual(list, result)

    def test_join_elements_1(self):
        result = [(5, 8), (6, 8), (7, 8), (9, 10), (12, 15), (12, 16), (2, 6),
                  (0, 1), (-2, -1)]
        calendar.quicksort(result, 0, len(result) - 1)
        linked_list = calendar.create_LinckedList(result)
        calendar.join_elements(linked_list)
        self.assertEqual(linked_list.get_list(),
                         [(-2, -1), (0, 1), (2, 8), (9, 10), (12, 16)])

    def test_join_elements_2(self):
        result = [(1, 8), (3, 4), (5, 7), (5, 8), (1, 6), (67, 81), (34, 45),
                  (45, 67)]
        calendar.quicksort(result, 0, len(result) - 1)
        linked_list = calendar.create_LinckedList(result)
        calendar.join_elements(linked_list)
        self.assertEqual(linked_list.get_list(), [(1, 8), (34, 81)])

    def test_join_elements_3(self):
        result = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        calendar.quicksort(result, 0, len(result) - 1)
        linked_list = calendar.create_LinckedList(result)
        calendar.join_elements(linked_list)
        self.assertEqual(linked_list.get_list(), [(0, 1), (3, 8), (9, 12)])

    def test_join_elements_4(self):
        result = [(3, 5), (5, 7), (4, 6), (8, 9), (12, 34), (45, 67)]
        calendar.quicksort(result, 0, len(result) - 1)
        linked_list = calendar.create_LinckedList(result)
        calendar.join_elements(linked_list)
        self.assertEqual(linked_list.get_list(), [(3, 7), (8, 9), (12, 34),
                                                   (45, 67)])

    def test_join_elements_5(self):
        result = [(1, 6), (6, 7), (7, 8), (9, 12), (10, 11), (13, 23)]
        calendar.quicksort(result, 0, len(result) - 1)
        linked_list = calendar.create_LinckedList(result)
        calendar.join_elements(linked_list)
        self.assertEqual(linked_list.get_list(), [(1, 8), (9, 12), (13, 23)])


if __name__ == '__main__':
    unittest.main()
