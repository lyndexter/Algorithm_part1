import time
from typing import List

from Models.Book import Book


class SortManager:

    @staticmethod
    def sort_by_page_number(books: List[Book]):
        """
        :param books:
        :return:descending sorted list by Insertion sort
        """
        start_time = time.time()
        length_books = len(books)
        quantity_operation_compare = 0
        quantity_operation_change = 0

        for sorting_index in range(1, length_books):

            sorting_element = books[sorting_index]
            comparing_index = sorting_index - 1
            quantity_operation_compare += 1

            while comparing_index >= 0 and books[comparing_index].page_number \
                    < sorting_element.page_number:
                books[comparing_index + 1] = books[comparing_index]
                comparing_index -= 1

                quantity_operation_change += 1
                quantity_operation_compare += 1

            books[comparing_index + 1] = sorting_element

        end_time = time.time()
        print(
            "\n\n    ---- Insertion Sort Descending by page number ---- \n "
            "quantity of compare operation: {}, \n quantity of change "
            "operation {}, \n time: {} \n".format(quantity_operation_compare,
                                                  quantity_operation_change,
                                                  end_time - start_time))

    @staticmethod
    def merge_sort(books: List[Book], quantity_operation_compare: int,
                   quantity_operation_change: int):
        """

        :param quantity_operation_change: for calculation change operation
        :param quantity_operation_compare: for calculation compare operation
        :param books:
        :return: descending sorted  list of books by Merge sort, quantity
        compare operation in algorithm and quantity change operation in
        algorithm
        """
        length_books = len(books)

        if length_books > 1:

            middle = length_books // 2
            left_array, quantity_operation_compare_previous, \
            quantity_operation_change_previous = SortManager.merge_sort(
                books[:middle], 0, 0)
            right_array, quantity_operation_compare_previous, \
            quantity_operation_change_previous = SortManager.merge_sort(
                books[middle:], 0, 0)

            quantity_operation_compare += quantity_operation_compare_previous
            quantity_operation_change += quantity_operation_change_previous

            books.clear()

            while len(left_array) > 0 and len(right_array) > 0:

                quantity_operation_compare += 1

                if left_array[0].price_in_UAH > right_array[0].price_in_UAH:
                    books.append(left_array.pop(0))

                    quantity_operation_change += 1
                else:
                    books.append(right_array.pop(0))

                    quantity_operation_change += 1

            if len(left_array) > 0:
                books.extend(left_array)

                quantity_operation_change += len(left_array)

            if len(right_array) > 0:
                books.extend(right_array)

                quantity_operation_change += len(right_array)

        return books, quantity_operation_compare, quantity_operation_change

    @staticmethod
    def sort_by_price(books: List[Book]):
        """

        :param books:
        :return:Sorted list of books(by Merge Sort) by price descending
        """
        quantity_operation_compare = 0
        quantity_operation_change = 0
        start_time = time.time()

        books, quantity_operation_compare, quantity_operation_change = \
            SortManager.merge_sort(books, quantity_operation_compare,
                                   quantity_operation_change)

        end_time = time.time()
        print(
            "\n\n    ---- Merge Sort Descending py price ---- \n quantity of "
            "compare operation: {}, \n quantity of change "
            "operation {}, \n time: {}\n".format(quantity_operation_compare,
                                                 quantity_operation_change,
                                                 end_time - start_time))
