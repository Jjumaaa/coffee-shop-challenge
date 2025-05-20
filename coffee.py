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
