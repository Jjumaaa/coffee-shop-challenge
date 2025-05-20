class Coffee:
    def __init__(self, name):
        name = name.strip()
        if not isinstance(name, str):
            raise TypeError("Expected name to be a string")
        if len(name) < 3:
            raise ValueError("Name must have at least 3 characters")
        
        self.__orders = []
        self.__name = name

    @property
    def name(self):
        return self.__name

    def orders(self):
        return list(self.__orders)

    def num_orders(self):
        return len(self.__orders)

    def average_price(self):
        count = self.num_orders()
        if count == 0:
            return 0
        total = 0
        for order in self.__orders:
            total += order.price
        return total / count
