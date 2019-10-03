# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__n_to = None
        self.__s_to = None
        self.__e_to = None
        self.__w_to = None

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def n_to(self):
        return self.__n_to

    @n_to.setter
    def n_to(self, room):
        self.__n_to = room

    @property
    def s_to(self):
        return self.__s_to

    @s_to.setter
    def s_to(self, room):
        self.__s_to = room

    @property
    def e_to(self):
        return self.__e_to

    @e_to.setter
    def e_to(self, room):
        self.__e_to = room

    @property
    def w_to(self):
        return self.__w_to

    @w_to.setter
    def w_to(self, room):
        self.__w_to = room
