from termcolor import colored
from src.basicTypes import Location, Container

def ex(exit):
    return colored(exit.upper(), "yellow")

class Room(Location, Container):
    # This is the class for all Roomspaces. 
    # TODO Swap describe and detail describe (see location class)

    def __init__(self, name):
        Location.__init__(self, name)
        Container.__init__(self, name)
        self.desc = []
        self.entityType = "room"  # A roomspace will have type room.
        self.inventory = {}  # This is the 'root' inventory for the room.
        self.container_inventory = []  # This is the subcontainer inventory.
        self.exits = {}

    def detail_describe(self):
        super(Room, self).detail_describe()
        if self.inventory:
            super(Room, self).list_contents()
        if self.container_inventory:
            self.list_containers()
        if self.exits:
            self.list_exits()

    def describe(self, detail=False):
        if self.visited:
            super(Container, self).describe()
            if self.inventory:
                super(Room, self).list_contents()
            if self.container_inventory:
                self.list_containers()
            if self.exits:
                self.list_exits()
        else:
            self.detail_describe()
            self.visited = True
