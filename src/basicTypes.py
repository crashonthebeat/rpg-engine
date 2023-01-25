from termcolor import colored  # Use terminal colors.
from tabulate import tabulate

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

    def __init__(self, name, list_desc, open, can_close):
        Entity.__init__(self, name)
        self.entityType = "box"  # This is the common term for a container.
        self.list_desc = list_desc  # A string that prints before the listed items.
        self.inventory = {}  # A key pair value of item id and quantity.
        self.container_inventory = []  # A list of containers held within.
        self.open = open  # If the contents will be listed with the parent
        self.can_close = can_close  # If the container can close. 
        self.slots = False  # Size capacity of the container.
        self.is_container = True

    def list_contents(self):
        # This method loops through and lists all items contained within itself.
        # If there are open containers, it will also list those items.
        # If a container is closed, it will list as an item before open containers.

        # TODO CLEAN UP
        if len(self.inventory) == 1:
            for item in self.inventory.keys():
                print(self.list_desc.capitalize() + " is " + item.name + ".")
            self.list_containers()
        elif len(self.inventory) > 1:
            print(self.list_desc.capitalize() + ":")
            for item in self.inventory.keys():
                print(item.name)
            self.list_containers()
        else: 
            self.list_containers()
            print(f"There is nothing {self.list_desc}.")

    def list_containers(self):
        # This method lists all containers in an inventory and their contents.

        if len(self.container_inventory) == 0:
            return True

        for box in self.container_inventory:
            if box.open == True: 
                box.list_contents()
            else: 
                print(box.name.capitalize() + " is here.")

    def describe(self):
        # This takes the entity describe method and adds the call to search
        # contents if the container is open.

        super(Container, self).describe()
        if self.open: self.list_contents()
        elif self.entityType == 'wearable': self.list_contents()
        # List contents if wearable, since you're not gonna lock a backpack.

    def find_item(self, search_item):
        # This method creates an array of all open containers in the search
        # space (incl the root container), and iterates through all lists
        # in order to find the item.

        found = 0  # Item not found yet
        item_id = False  # Returns if item can't be found
        parent_id = False  # Same as above
        
        all_boxes = [self]  # Create list of all containers, start with self
        for box in self.container_inventory:
            if box.open: all_boxes.append(box)
            # Of all containers in this container, add any open containers.

        for box in all_boxes: 
            for item in box.inventory.keys():
                if search_item in item.name.lower():
                    # If the item is found, increase found count, but keep
                    # searching in case there are more.
                    found += 1
                    item_id = item
                    parent_id = box
                if search_item in item.name.lower() and found > 1:
                    # If the method finds multiple, user needs to specify.
                    return 'multiple', parent_id  # Stop searching
        
        return item_id, parent_id    

    def find_box(self, box, pc_boxes):
        # This method is like find_item, but for child containers.

        search_area= []  # Create blank search area
        search_area.extend(self.container_inventory)  # Append room containers
        search_area.extend(pc_boxes)  # Append all the PC's containers


        box_id = False
        found = 0

        for container in search_area:
            if box in container.name.lower():
                found += 1
                box_id = container
            if box in container.name and found > 1:
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

    def open_self(self):
        if self.open:
            print(f"{self.name.capitalize()} is already open.")
        else:
            self.open = True
            print(f"You open {self.name}")

    def close_self(self):
        if self.open == False:
            print(f"{self.name.capitalize()} is already closed.")
        elif self.can_close:
            print(f"You close {self.name}.")
            self.open = False
        else:
            print(f"You can't close {self.name}!")


class Location(Entity):
    # This is the super class for all location entities. The reason why it 
    # isn't just a room, is because there will be overworld map locations
    # that don't have items but have their own special properties. 

    def __init__(self, name):
        Entity.__init__(self, name)
        self.entityType = "location"
        self.desc_quick = []
        self.exits = {}
        self.visited = False

    def list_exits(self):
        # This method lists all the exists for a location as well as their
        # direction, which is highlighted.

        for dir, exit in zip(self.exits.keys(), self.exits.values()):
            print(f"{ex(dir)}: {exit.name.capitalize()}")

    def quick_describe(self):
        # This method will print a quick description of a location if the
        # user has already visited the location before and nothing has
        # changed. 
        for line in self.desc_quick: print(line)

    def enter(self):
        # This method is used to print all the relevant stats of a room
        # when it is entered. This, as well as the main method will be
        # roughly the same. 

        if self.visited: 
            self.quick_describe()
        else: 
            self.describe()
            self.visited = True

        
        self.list_exits()

class Person(Entity):
    # This is the super class for all living non-beast entities. Objects of
    # this class can wear armor and wield items. This will also be where all
    # methods that aren't player actions go.

    def __init__(self, name):
        Entity.__init__(self, name)
        self.entityType = "person"
        self.free_hands = 2  # All races will have 2 hands.
        # The following attributes are for wearables.
        # See wearables for explanation of slot amounts.
        self.items_held = []
        self.wearable_slots = {
            'head': 3, 'face': 1, 'eyes': 1, 'neck': 2, 'back': 2, 
            'l_should': 2.5, 'l_arm': 2.5, 'l_wrist': 1.5, 'l_hand': 1.5,
            'r_should': 2.5, 'r_arm': 2.5, 'r_wrist': 1.5, 'r_hand': 1.5,
            'chest': 2.5, 'waist': 2.5, 'hips': 2.5, 'fingers': 8,
            'l_thigh': 1.5, 'l_shin': 1.5, 'l_foot': 1.5,
            'r_thigh': 1.5, 'r_shin': 1.5, 'r_foot': 1.5
        }
        self.items_worn = []

    def make_table(self, cols):
        # This method will take a series of columns and format it into
        # a table to be printed to the console.

        # This function appends spaces to the end of each list so that
        # each list will have an equal number of rows.
        maxlen = 0
        for col in cols: maxlen = max(maxlen, len(col))
        for col in cols: col +=[' '] * (maxlen - len(col))
        table = list(zip(*cols))
        return tabulate(table, maxcolwidths=(80 / len(cols)))
        
