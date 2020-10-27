def input_values():
    list_of_tupple = []
    while True:
        raw_numbers = input()
        if raw_numbers == "":
            break;
        x, y = raw_numbers.split(" ")
        list_of_tupple.append((int(x), int(y)))

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


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.current_element = None

    def print_list(self):
        element = self.head
        while element:
            print(element.value)
            element = element.next


def create_LinckedList(array_list):
    linked_list = LinkedList()
    for iterator in array_list:
        if linked_list.head is None:
            linked_list.head = Node(iterator)
            temp = linked_list.head
        else:
            temp.next = Node(iterator)
            temp = temp.next
    return linked_list


def join_elements(lincked_list_of_tupple):
    lincked_list_of_tupple.current_element = lincked_list_of_tupple.head
    while (True):
        if lincked_list_of_tupple.current_element is None or \
                lincked_list_of_tupple.current_element.next is None:
            break
        if lincked_list_of_tupple.current_element.value[0] <= \
                lincked_list_of_tupple.current_element.next.value[0] <= \
                lincked_list_of_tupple.current_element.value[1] <= \
                lincked_list_of_tupple.current_element.next.value[1]:
            lincked_list_of_tupple.current_element.value = (
                lincked_list_of_tupple.current_element.value[0],
                lincked_list_of_tupple.current_element.next.value[1])
            lincked_list_of_tupple.current_element.next = \
                lincked_list_of_tupple \
                    .current_element.next.next
        elif lincked_list_of_tupple.current_element.value[1] > \
                lincked_list_of_tupple.current_element.next.value[0]:
            lincked_list_of_tupple.current_element.value = (
                lincked_list_of_tupple.current_element.value[0],
                lincked_list_of_tupple.current_element.value[1])
            lincked_list_of_tupple.current_element.next = \
                lincked_list_of_tupple \
                    .current_element.next.next
        else:
            lincked_list_of_tupple.current_element = \
                lincked_list_of_tupple.current_element.next


if __name__ == '__main__':
    array_list = input_values()

    quicksort(array_list, 0, len(array_list) - 1)
    print(array_list)

    lincked_list = create_LinckedList(array_list)

    join_elements(lincked_list)

    print()
    lincked_list.print_list()
