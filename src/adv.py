from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'weapons': Room("Room Full of Weapons", """It's your lucky day! You found different
weapons that are going to help you in your adventure! It was well hidden in
the Treasure Room.""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].e_to = room['weapons']
room['weapons'].w_to = room['treasure']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("David", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

user_input = None

available_commands = ["q", "n", "s", "e", "w"]

input_instructions = """Instructions:\n- Enter 'n' to move to the North, 's' to move to the South,
 'e' to move to the East and 'w' to move to the West.\n
- Enter 'q' to quit the game.\n\nAction: """

while user_input is not "q":
    print("Current Room:", player.current_room.name)
    print("Description:", player.current_room.description)
    print("\n")
    user_input = input(input_instructions)
    print("\n")

    if user_input not in available_commands:
        print("\nInvalid command, try again! \n")

    elif user_input is not 'q':
        player.move_to(user_input)
