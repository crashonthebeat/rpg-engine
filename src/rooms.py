from termcolor import colored
from src.basicTypes import Location, Container

def ex(exit):
    return colored(exit.upper(), "yellow")

class Room(Location, Container):
    def __init__(self, name):
        Location.__init__(self, name)
        Container.__init__(self, name)
        self.desc = []
        self.entityType = "room"
        self.inventory = {}
        self.container_inventory = []
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
