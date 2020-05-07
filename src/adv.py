from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount beckons"""),

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input('Enter Name: '), room['outside'])
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

while True:
    print(f'{player.name}...{player.curr_room}')
    user_input = input('Enter a direction to travel (n, s, e, w) or (Q) to quit:')
    if user_input == 'Q':
        print('Game Over')
        break
    
    try:
        if user_input == 'n':
            if player.curr_room.n_to:
                print('**Moved North**')
                player.curr_room = player.curr_room.n_to
            else:
                print('**Cannot move that direction**')
        elif user_input == 's':
            if hasattr(player.curr_room, 's_to'):
                player.curr_room = player.curr_room.s_to
                print('**Moved South**')
            else:
                print('**Cannot move that direction**')
        elif user_input == 'e':
            if hasattr(player.curr_room, 'e_to'):
                player.curr_room = player.curr_room.e_to
                print('**Moved East**')
            else:
                print('**Cannot move that direction**')
        elif user_input == 'w':
            if player.curr_room.w_to:
                print('**Moved West**')
                player.curr_room = player.curr_room.w_to
            else:
                print('**Cannot move that direction**')
    except ValueError:
        print('Not a valid command!')

