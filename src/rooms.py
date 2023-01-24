from termcolor import colored
from src.basicTypes import Location, Container

def ex(exit):
    return colored(exit.upper(), "yellow")

class Room(Location, Container):
    # This is the class for all Roomspaces. 
    # TODO Swap describe and detail describe (see location class)

    def __init__(self, name):
        Location.__init__(self, name)
        self.desc = []
        self.list_desc = "lying on the ground" # Basic list_desc for all rooms
        self.entityType = "room"  # A roomspace will have type room.
        self.inventory = {}  # This is the 'root' inventory for the room.
        self.container_inventory = []  # This is the subcontainer inventory.
        self.exits = {}
        self.open = True
        self.can_close = False

    def describe(self):
        # Since this location type is unique, looking at the room will
        # also list its contents.
        for line in self.desc: print(line)
        self.list_contents()
