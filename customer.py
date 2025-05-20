class Customer:
    def __init__(self, name):
        self._validate_name(name)
        self.__name = name
        self.__orders = []

    def _validate_name(self, value):
        if type(value) != str:
            raise TypeError("Customer name must be a string")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Customer name must be 1 to 15 characters long")

    