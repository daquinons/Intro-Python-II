class Item():
    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    def __str__(self):
        return f"{self.__name}: {self.__description}"

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description
