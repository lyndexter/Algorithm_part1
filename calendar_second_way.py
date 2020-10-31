from typing import List


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

    def get_list(self):
        element = self.head
        result = []
        while element:
            result.append(element.value)
            element = element.next

        return result

    def create_lincked_list(self, list: List):
        for raw_numbers in list:
            x = raw_numbers[0]
            y = raw_numbers[1]
            if self.head is None:
                self.head = Node((x, y))
                self.current_element = self.head

            elif x <= self.head.value[0]:
                temp = self.head
                self.head = Node((x, y))
                self.head.next = temp
            else:
                while self.current_element.next is not None \
                        and x > self.current_element.next.value[0]:
                    self.current_element = self.current_element.next
                else:
                    new_node = Node((x, y))
                    new_node.next = self.current_element.next
                    self.current_element.next = new_node

    def join_nodes(self):
        self.current_element = self.head
        while (True):
            if self.current_element is None or \
                    self.current_element.next is None:
                break

            if self.current_element.value[0] <= \
                    self.current_element.next.value[0] <= \
                    self.current_element.value[1] <= \
                    self.current_element.next.value[1]:
                self.current_element.value = (
                    self.current_element.value[0],
                    self.current_element.next.value[1])
                self.current_element.next = self \
                    .current_element.next.next
            elif self.current_element.value[1] > \
                    self.current_element.next.value[0]:
                self.current_element.value = (
                    self.current_element.value[0],
                    self.current_element.value[1])
                self.current_element.next = self \
                    .current_element.next.next
            else:
                self.current_element = \
                    self.current_element.next


if __name__ == '__main__':

    schedule = LinkedList()

    input_schedule = []
    while True:
        raw_numbers = input()
        if raw_numbers == "":
            break
        x, y = raw_numbers.split(" ")
        x = int(x)
        y = int(y)
        input_schedule.append((x, y))

    schedule.create_lincked_list(input_schedule)
    schedule.print_list()
    print()
    schedule.join_nodes()
    schedule.print_list()
