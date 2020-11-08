import csv


class Company:
    def __init__(self):
        self.num_layers = 0
        self.layers = []
        self.max_expirience = 0

    def write_layers(self):
        self.num_layers = int(input())
        for layer_index in range(self.num_layers):
            self.layers.append(list(map(lambda x: int(x), input().split())))

        print(self.layers)

    def read_structure_from_csv(self):
        with open("input.csv") as input_file:
            csv_reader = csv.reader(input_file, delimiter=",")
            next(csv_reader)
            for row in csv_reader:
                self.layers.append(list(map(lambda x: int(x), row)))
            print(self.layers)
            self.num_layers = len(self.layers)

    def find_bigger(self, layer_index, position_index):
        left_position = self.layers[layer_index + 1][position_index]
        right_position = self.layers[layer_index + 1][position_index + 1]

        if left_position > right_position:
            self.layers[layer_index][position_index] += left_position
        else:
            self.layers[layer_index][position_index] += right_position

    def find_max_experience(self):
        for layer_index in range(self.num_layers - 2, -1, -1):
            for position_index in range(layer_index + 1):
                self.find_bigger(layer_index, position_index)
        return self.layers[0][0]


if __name__ == '__main__':
    company = Company()
    company.read_structure_from_csv()

    max_experience = company.find_max_experience()

    print(max_experience)
