from Managers.SortManager import SortManager
from Models.Book import Book
import random
import csv


def create_random_books_list():
    books = [Book(random.randint(1, 200), "Stepan Vovk",
                  random.randint(1, 200)) for i in range(32)]
    return books


def read_csv_file(path_csv_file):
    books = []
    try:
        with open(path_csv_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                books.append(Book(int(row[0]), row[1], int(row[2])))
    except:
        books = create_random_books_list()
    return books


if __name__ == '__main__':

    directory_of_file = input("Please input path of csv file:\n")

    books = read_csv_file(directory_of_file)

    SortManager.sort_by_price(books)

    for i in books:
        print(i)

    SortManager.sort_by_page_number(books)

    for i in books:
        print(i)
