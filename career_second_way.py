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

    def find_expirience(self, previous_exp, layer_index, position_index):
        current_exp = previous_exp + self.layers[layer_index][position_index]
        if current_exp > self.max_expirience:
            self.max_expirience = current_exp

        if layer_index + 1 == self.num_layers:
            return

        self.find_expirience(current_exp, layer_index + 1,
                             position_index)

        self.find_expirience(current_exp, layer_index + 1,
                             position_index + 1)

    def find_max_experience(self):
        self.find_expirience(0, 0, 0)
        return self.max_expirience


if __name__ == '__main__':
    company = Company()
    company.write_layers()

    max_experience = company.find_max_experience()

    print(max_experience)
