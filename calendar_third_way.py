def input_values():
    list_of_tupple = []
    while True:
        raw_numbers = input()
        if raw_numbers == "":
            break;
        x, y = raw_numbers.split(" ")
        x = int(x)
        y = int(y)
        list_of_tupple.append([int(x), int(y)])

    return list_of_tupple


def quicksort(list, left_position, right_position):
    if left_position >= right_position:
        return
    pivot = partition(list, left_position, right_position)
    quicksort(list, left_position, pivot - 1)
    quicksort(list, pivot + 1, right_position)


def partition(list, left_position, right_position):
    pivot = list[right_position]
    min_element_position = left_position
    for elements_position in range(left_position, right_position):
        if list[elements_position][0] < pivot[0]:
            list[elements_position], list[min_element_position] = \
                list[min_element_position], list[elements_position]
            min_element_position += 1
    list[right_position], list[min_element_position] = \
        list[min_element_position], list[right_position]
    return min_element_position


def optimaze_sheldue(list):
    new_list = []
    for item in list:
        if not join_element(new_list, item[0], item[1]):
            new_list.append([item[0], item[1]])
    return new_list


def join_element(list, x, y):
    for item in list:
        if item[0] <= x <= item[1]:
            if item[1] < y:
                item[1] = y
                return True
            return True

        if item[0] <= y <= item[1]:
            if item[0] > x:
                item[0] = x
                print("w", item)
                return True
            return True
    return False


if __name__ == '__main__':
    input_schedule = input_values()
    quicksort(input_schedule, 0, len(input_schedule) - 1)
    list = optimaze_sheldue(input_schedule)
    print(list)
