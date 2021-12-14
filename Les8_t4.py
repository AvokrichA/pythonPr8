class Sklad:
    def __init__(self, name):
        self.name = name


class OfficeEquipment:
    def __init__(self, type, article, pieces, price):
        self.type = type
        self.article = article
        self.pieces = pieces
        self.price = price

class Printer(OfficeEquipment):
    def __init__(self, model, printing_technology, print_color):
        self.model = model
        self.printing_technology = printing_technology
        self.print_color = print_color
        super().__init__(type, article, pieces, price)

class Scanner(OfficeEquipment):
    def __init__(self, model, type_of_scanner, sensor, size):
        self.model = model
        self.type_of_scanner = type_of_scanner
        self.sensor = sensor
        self.size = size
        super().__init__(type, article, pieces, price)

class Copier(OfficeEquipment):
    def __init__(self, model,printing_technology, print_color ):
        self.model = model
        self.printing_technology = printing_technology
        self.print_color = print_color

        super().__init__(type, article, pieces, price))
