from termcolor import colored

def ex(exit):
    return colored(exit.upper(), "yellow")

class Room:
    def __init__(self, name):
        self.name = name
        self.exits = None # Dict of direction: room id
        self.enter_desc = None # Short description of room.
        self.desc = None # Longer desc of room, called with 'look'
        self.inventory = None # Dict of item id: quantity
        self.visited = False

    def describe(self):
        # This method displays a longer description of the room as well
        # as listing the items in the room.

        for line in self.desc: 
            print(line)
        if self.inventory:
            for item in self.inventory.keys():
                print(item.room_desc)
        if self.exits:
            for exit in self.exits.keys():
                exit_desc = self.exits[exit].name.capitalize()
                print(f"{ex(exit)}: {exit_desc}")

    def enter(self):
        # This method displays the description and exits of a room
        # If the player has not visited this room, it will display
        # the full description.

        if not self.visited:
            self.describe()
            self.visited = True
        else:   
            for line in self.enter_desc:
                print(line)
            if self.exits:
                for exit in self.exits.keys():
                    exit_desc = self.exits[exit].name.capitalize()
                    print(f"{ex(exit)}: {exit_desc}")

    def find_object(self, object):
        # This method finds an object based on text provided by the user.

        for item in self.inventory.keys():
            if object in item.name.lower():
                found = True
                return item
            if object in item.name and found:
                return 'multiple'

        return False

    def remove_item(self, obj):
        if self.inventory[obj] == 1:
            self.inventory.pop(obj)
        else:
            self.inventory[obj] -= 1

    def add_item(self, obj):
        if obj in self.inventory.keys():
            self.inventory[obj] += 1
        else: 
            self.inventory[obj] = 1

    