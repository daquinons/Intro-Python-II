# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room):
        self.__name = name
        self.__current_room = current_room

    @property
    def current_room(self):
        return self.__current_room

    @current_room.setter
    def current_room(self, current_room):
        self.__current_room = current_room

    @property
    def name(self):
        return self.__name
