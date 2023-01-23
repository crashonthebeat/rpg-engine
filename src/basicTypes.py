from termcolor import colored  # Use terminal colors.

def ex(exit):
    # This allows the location class to color the directions
    # in the exit print list.
    return colored(exit.upper(), "yellow")

class Entity:
    # Everything that exists in the world will have the methods and 
    # attributes listed in this class. So far, a name and a description.

    def __init__(self, name):
        self.name = name
        self.desc = []  # A list of strings. 
        self.entityType = False
        # Entity type is a string that tells the game what the primary type
        # the object is. Used for validation of actions. If the code is
        # looking for an id (variable name) it will look for:
        # entityType_id (box_id, item_id, etc.)

    def describe(self):
        # This method is run when the player looks at an entity.
        for line in self.desc: 
            print(line)


class Container(Entity):
    # Everything that has a limited inventory will inherit from this class.
    # Containers can be carried or worn items, immovable items, or fixtures
    # of a roomspace (like a shelf). Every container will have a unique id.
    # ID of an item is just the object variable name.

    def __init__(self, name):
        Entity.__init__(self, name)
        self.entityType = "box"  # This is the common term for a container.
        self.list_desc = ""  # A string that prints before the listed items.
        self.inventory = {}  # A key pair value of item id and quantity.
        self.container_inventory = []  # A list of containers held within.
        self.open = False  # If the contents will be listed with the parent
        self.slots = False  # Size capacity of the container.

    def list_contents(self):
        # This method loops through and lists all items contained within itself.
        # If there are open containers, it will also list those items.
        # If a container is closed, it will list as an item before open containers.

        # TODO CLEAN UP
        if len(self.inventory) == 1:
            for item in self.inventory.keys():
                print(self.list_desc.capitalize() + " is " + item.name + ".")
        elif len(self.inventory) > 1:
            print(self.list_desc + ":")
            for item in self.inventory.keys():
                print(item.name)
        else: print(f"There is nothing {self.list_desc}.")

    def list_containers(self):
        # This method lists all containers in an inventory and their contents.

        for holder in self.container_inventory:
            if holder.open == True: 
                holder.list_contents()
            else: 
                print(holder.name.capitalize() + " is here.")

    def describe(self):
        # This takes the entity describe method and adds the call to search
        # contents if the container is open.

        super(Container, self).describe()
        self.list_contents()

    def find_item(self, obj):
        # This method is called when a user wants to interact with an item
        # in a container. It loops over all items in its own inventory and
        # the inventories of child containers. If the item is found in a
        # child inventory, then it returns what container it was found in.

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
        # This method is like find_item, but for child containers.

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
        # This method checks if removing the item will reduce its quantity to 
        # zero, in which case the item should be removed from the key/value
        # pairs. 

        if self.inventory[obj] == 1:
            self.inventory.pop(obj)
        else:
            self.inventory[obj] -= 1

    def add_item(self, obj):
        # Like the remove_item, this checks if the item exists in inventory,
        # and either increase it's quantity or create a new key/value pair.

        if obj in self.inventory.keys():
            self.inventory[obj] += 1
        else: 
            self.inventory[obj] = 1


class Location(Entity):
    # This is the super class for all location entities. The reason why it 
    # isn't just a room, is because there will be overworld map locations
    # that don't have items but have their own special properties. 

    def __init__(self, name):
        Entity.__init__(self, name)
        self.entityType = "location"
        self.detail_desc = []
        self.exits = {}
        self.visited = False

    def list_exits(self):
        # This method lists all the exists for a location as well as their
        # direction, which is highlighted.

        for dir, exit in zip(self.exits.keys(), self.exits.values()):
            print(f"{ex(dir)}: {exit.name.capitalize()}")

    def detail_describe(self):
        # This method will print the full description of the location, if
        # this is the player's first time visiting or they want a full
        # description of the room. 
        # TODO Make this the describe method, and subsequent visits are
        #      quick describe.

        for line in self.detail_desc:
            print(line)

    def describe(self):
        # This method will print a simple description of the room. It will
        # change depending on if the location type is a roomspace or an
        # overworld space.

        if self.visited:
            super(Location, self).describe()
        else:
            self.detail_describe()
            self.visited = True
        if self.exits:
            self.list_exits()

    def enter(self):
        # This method is used to print all the relevant stats of a room
        # when it is entered. This, as well as the main method will be
        # roughly the same. 

        self.describe()