import csv
from typing import List


def longest_str_chain(words: List[str]) -> int:
    words.sort(key=lambda x: len(x))

    words_dict = {}
    max_chain = 0

    for word in words:
        iterator = 0
        current_max = 1
        while iterator < len(word):
            possible_word = word[:iterator] + word[iterator + 1:]
            iterator += 1
            if possible_word in words_dict:
                current_max = max(current_max, words_dict[possible_word] + 1)
        words_dict[word] = current_max
        max_chain = max(max_chain, current_max)

    return max_chain


def read_date_from_csv():
    date = []
    with open("input.csv") as input_file:
        csv_reader = csv.reader(input_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            date.append(row[0])
        print(date)
    return date


def read_input():
    date = []
    input()
    while True:
        word = input()
        if word == "":
            break
        date.append(word)
    print(date)
    return date


if __name__ == '__main__':
    words = read_input()

    print(longest_str_chain(words))
