import csv
from KMP_algorithm_modified import find_substring


def read_csv(path):
    with open(path) as file:
        csv_reader = csv.reader(file)

        strings = []
        for row in csv_reader:
            strings.append([row[0], row[1]])
        return strings


def input_text():
    text = input("Please write text where will be search")
    pattern = input("Please write what you want search")
    return text, pattern


def write_csw(data, path):
    with open(path, 'w', newline='') as file:
        csv_writter = csv.writer(file)

        for row in data:
            csv_writter.writerow(row)


if __name__ == '__main__':
    # text, pattern = input_text()
    # print(find_substring(text, pattern))

    data = read_csv("input.csv")
    result = []
    for text, pattern in data:
        substrings_intervals = []
        substrings_starts = find_substring(text, pattern)
        for substrings_start in substrings_starts:
            substrings_intervals.append((substrings_start,
                                         substrings_start + len(pattern)))
        result.append(substrings_intervals)
    write_csw(result, "output.csv")
