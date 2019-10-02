# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room):
        self.__name = name
        self.__current_room = current_room

    @property
    def current_room(self):
        return self.__current_room

    @property
    def name(self):
        return self.__name

    def move_to(self, direction):
        selected_room = None
        if direction is 'n':
            selected_room = self.__current_room.n_to
        elif direction is 's':
            selected_room = self.__current_room.s_to
        elif direction is 'e':
            selected_room = self.__current_room.e_to
        elif direction is 'w':
            selected_room = self.__current_room.w_to

        if selected_room is None:
            print("\n\nNothing on that direction! Try with another one\n")
        else:
            self.__current_room = selected_room
