class Book:
    def __init__(self, page_number: int, name_author, price_in_UAH: int):
        self.page_number = page_number
        self.name_author = name_author
        self.price_in_UAH = price_in_UAH

    def __str__(self):
        return "page number: {}, author name: {}, price(UAN): {}".format(
            self.page_number, self.name_author, self.price_in_UAH)
