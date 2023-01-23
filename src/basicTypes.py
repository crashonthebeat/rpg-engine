from termcolor import colored

def ex(exit):
    return colored(exit.upper(), "yellow")

class Entity:
    def __init__(self, name):
        self.name = name
        self.desc = []
        self.entityType = False

    def describe(self):
        for line in self.desc: 
            print(line)


class Container(Entity):
    def __init__(self, name):
        Entity.__init__(self, name)
        self.entityType = "box"
        self.list_desc = ""
        self.inventory = {}
        self.container_inventory = []
        self.open = False
        self.slots = False

    def list_contents(self):
        if len(self.inventory) == 1:
            for item in self.inventory.keys():
                print(self.list_desc.capitalize() + " is " + item.name + ".")
        elif len(self.inventory) > 1:
            print(self.list_desc + ":")
            for item in self.inventory.keys():
                print(item.name)
        else: print(f"There is nothing {self.list_desc}.")

    def list_containers(self):
        for holder in self.container_inventory:
            if holder.open == True: 
                holder.list_contents()
            else: 
                print(holder.name.capitalize() + " is here.")

    def describe(self):
        super(Container, self).describe()
        self.list_contents()

    def find_item(self, obj):
        obj_id = False
        found_container = False
        found = 0

        for item in self.inventory.keys():
            if obj in item.name.lower():
                found += 1
                obj_id =  item
            if obj in item.name and found > 1:
                obj_id = 'multiple'
        if self.container_inventory and found == 0:
            for box in self.container_inventory:
                if box.open: 
                    obj_id, holder = box.find_item(obj)
                    if obj_id: 
                        found += 1
                        found_container = box
                    if obj_id and found > 1: 
                        obj_id = 'multiple'

        return obj_id, found_container
    
    def find_box(self, box):
        box_id = False
        found = 0

        for item in self.container_inventory:
            if box in item.name.lower():
                found += 1
                box_id =  item
            if box in item.name and found > 1:
                box_id = 'multiple'

        return box_id
    
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


class Location(Entity):
    def __init__(self, name):
        Entity.__init__(self, name)
        self.entityType = "location"
        self.detail_desc = []
        self.exits = {}
        self.visited = False

    def list_exits(self):
        for dir, exit in zip(self.exits.keys(), self.exits.values()):
            print(f"{ex(dir)}: {exit.name.capitalize()}")

    def detail_describe(self):
        for line in self.detail_desc:
            print(line)

    def describe(self):
        if self.visited:
            super(Location, self).describe()
        else:
            self.detail_describe()
            self.visited = True
        if self.exits:
            self.list_exits()

    def enter(self):
        self.describe()