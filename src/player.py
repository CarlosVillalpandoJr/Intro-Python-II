# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.items = items
    def move(self, direction):
        if getattr(self.current_room, direction + '_to'):
            self.current_room = getattr(self.current_room, direction + '_to')
            print(f'**CURRENT LOCATION**: {self.current_room.name}')
            print(f'**DESCRIPTION**: {self.current_room.description}')
        else:
            print("You cannot move in that direction!!")

