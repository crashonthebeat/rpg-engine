import os, itertools

from time import sleep
from src.basicTypes import Container, Person

def clear_screen():
    # This method will clear the screen to clean it up.

    return True  # Disabling this method while in production.
    
    sleep(0.5)

    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

class Player(Person, Container):
    # The player has an inventory, so it is a container. 

    def __init__(self, name):
        Person.__init__(self, name)
        self.desc = [f"Nothing can be said about {self.name}."]
        self.list_desc = 'in your hands'
        self.inventory = {}
        self.container_inventory = []
        self.items_worn = []
        self.items_held = []
        self.helditems_d = ['You are currently holding:']
        self.wornitems_d = ['You are currently wearing:']
        self.can_close = False
        self.open = True

    def describe(self):
        # This is the method that will display the self description, as well
        # as print the inventory and held items.

        # The two lines below 
        cols = [self.wornitems_d, self.helditems_d]
        items_table = self.make_table(cols)

        super(Container, self).describe()
        print(items_table)

        # These two functions resets any added spaces in the items table.
        # Otherwise there's a leapfrogging effect for the columns
        self.wornitems_d = [i for i in self.wornitems_d if i != ' ']
        self.helditems_d = [i for i in self.helditems_d if i != ' ']

    def travel(self, action, direction):
        # This is the travel method used to move the player between
        # roomspaces, as well as sub-spaces and overworld.
        shorthand = {
            "n": "north", "s": "south", "e": "east", "w": "west",
            "nw": "northwest", "ne": "northeast", 
            "se": "southeast", "sw": "southwest"
        }

        if direction in shorthand.keys():
            direction = shorthand[direction]
        else: pass

        if direction in self.current_room.exits.keys():
            print(f"You {action} {direction}.")
            new_room = self.current_room.exits[direction]
            # clear_screen()
            print(f"---{new_room.name}---")
            new_room.enter()
            self.current_room = new_room
        else:
            print(f"You cannot go {direction}.")
    
    def search_for_box(self, box, action):
        # This is the method to find a subcontainer in a given container.
        
        box_id = self.current_room.find_box(box, self.container_inventory)
        if box_id == False:  # If the user box isn't found, stop function.
                print(f"You don't see the {box} {self.current_room.list_desc.lower()}.")
        elif box_id == 'multiple':  # If search returned multiple boxes.
            print(f"Which {box} do you want to {action}?")
            box_id = False
            # The user will need to be more specific.
        elif box_id.is_container == False:
            print(f"{box_id.name.capitalize()} is not a container.")
        else: pass

        return box_id

    def find_equipped_item(self, search_item):
        for item in itertools.chain(self.items_held, self.items_worn):
            if search_item in item.name:
                return item, self
        else: return False, self

    def search_for_item(self, item, parent_box, action):
        # This searches a found container for an item given by user input
        # and returns the item_id as well as the id of any subcontainer it
        # was found in. 
        
        item_id, box_id = parent_box.find_item(item)
        if parent_box == self and item_id == False:
            item_id, box_id = self.find_equipped_item(item)
        if parent_box == self and item_id == False:    
            self.current_room.find_item(item)

        if item_id == False:  # If the item isn't found, stop function.
            print(f"You don't see the {item} {parent_box.list_desc.lower()}.")
            return False, parent_box
        elif item_id == 'multiple':  # If there are multiple matches.
            print(f"Which {item} do you want to {action}?")
            return False, parent_box
        else: return item_id, box_id

    def look(self, obj, ind_obj):
        # This calls the describe method for an entity if the entity exists.

        # If player types 'look at object': 
        if obj == False: obj = ind_obj
        else: pass
        
        # If player types 'look room' or 'look'
        if (obj == 'room' or obj == False):
            self.current_room.describe()
            return True
        elif obj == 'self':
            self.describe()
            return True
        else:  # If player specified a non-self object:
            obj_id, parent_id = self.search_for_item(
                obj, self, 'look at')
            # Search for items that match.

        if obj_id: obj_id.describe()

    def open_box(self, box):
        box_id = self.search_for_box(box, "open")
        
        if box_id == 'multiple': 
            pass
        elif box_id == False:
            pass
        else:
            box_id.open_self()

    def close_box(self, box):
        box_id = self.search_for_box(box, "close")

        if box_id: box_id.close_self()


    def get_item(self, item, box):
        # This method will search for an item in the roomspace container and
        # all child containers, or from just a specific container if that 
        # container is given as the indirect object.

        # If the user gives a specific container, search for that first.
        if box: 
            box_id = self.search_for_box(box, "get")
            if box_id == False: return True  # If no box is found, exit.
            elif box_id.open == False: 
                print(f"You need to open {box_id.name} first.")
                return True
        else: 
            box_id = self.current_room  # If no container is given.

        item_id, box_id = self.search_for_item(item, box_id, "get")

        # If the item was found (and box if given), then add and remove the items.
        if item_id:
            box_id.remove_item(item_id)
            self.add_item(item_id)
            if item_id.is_container: 
                self.container_inventory.append(item_id)
            print(f"You get {item_id.name} from {box_id.name}!")


    def drop_item(self, item):
        # This method will find an item in the player's inventory and "drops" 
        # it into the room's inventory.

        item_id, parent_id = self.search_for_item(item, self, "drop")

        if item_id:
            self.remove_item(item_id)
            if item_id.is_container: self.container_inventory.remove(item_id)
            self.current_room.add_item(item_id)
            print(f"You drop {item_id.name}")
        else: pass


    def place_item(self, item, box, prep):
        # This method takes an item from the player's inventory and places it
        # into a given container.

        box_id = self.search_for_box(box, "place into")

        if not box_id: return True
        elif box_id.open == False: 
            print(f"You need to open {box_id.name} first.")
            return True
        else: pass

        item_id, parent_id = self.search_for_item(item, self, "place")
        if item_id:
            self.remove_item(item_id)
            if item_id.is_container: self.container_inventory.remove(item_id)
            box_id.add_item(item_id)
            print(f"You place {item_id.name} {prep} {box_id.name.lower()}.")
        else: pass


    def test_for_fit(self, item):
        # This method loops through the values of the used slots on the clothing
        # item and tests if it will fit. If there are fewer available slots than
        # what is needed, the function will return false.

        for slot in item.used_slots.keys():
            if self.wearable_slots[slot] < item.used_slots[slot]:
                print(f"{item.name.capitalize()} won't fit over what you're wearing.")
                return False
        else: return True
            

    def equip_item(self, item, action):
        # This method takes an item from the player's inventory and
        # adds it to a slot.

        item_id, box_id = self.search_for_item(item, self, action)

        if not item_id:  # If there's no item in your inventory.
            return True

        # If the item is clothing or armor: do the following    
        elif item_id.entityType == "wearable":
            if self.test_for_fit(item_id):  # Test if item will fit
                # Subtracting the item's used slots from the pc's available slots
                for slot in item_id.used_slots.keys():
                    self.wearable_slots[slot] -= item_id.used_slots[slot]
            
                print(f"You put on {item_id.name}")
                self.items_worn.append(item_id)  # Add to worn items
                self.wornitems_d.append(item_id.wear_d)
                # Add string to self description for worn items
                if item_id.is_container: item_id.equip_bag()
                # Allow self-search to find items in container if it is.
                self.remove_item(item_id)

        # If the item is a tool or weapon: do the following
        elif item_id.entityType == "wieldable":
            if item_id.hand_slots > self.free_hands:
                print(f"You need {item_id.hand_slots} free hands for this.")
            else:
                self.free_hands -= item_id.hand_slots  # Remove hand slots
                self.remove_item(item_id)  # Remove from inventory
                self.items_held.append(item_id)  # Add to held items
                self.helditems_d.append(item_id.hold_d)
                # Add string to self-description
                print(f"You {action} {item_id.name}.")
        else: print(f"You can't {action} that!")
        

    def unequip_item(self, item):
        # This method removes an article of clothing or armor from
        # the pc's worn/held items slots and places it back in their
        # inventory.

        item_id = False  # This might come back to bite me later.

        for article in itertools.chain(self.items_worn, self.items_held):
            # The iterating find loop to translate the input string
            # into the actual item.
            if item in article.name: item_id = article

        if not item_id: pass
        elif item_id.entityType == 'wearable':
            print(f"You remove {item_id.name}.")
            for slot in item_id.used_slots.keys():
                # Adding the item's used slots back into the available slots
                self.wearable_slots[slot] += item_id.used_slots[slot]

            if item_id.is_container: item_id.unequip_bag()  # close bag
            self.items_worn.remove(item_id)  # Remove item from worn items
            self.wornitems_d.remote(item_id.wear_d)  # Remove from desc
            self.add_item(item_id)  # Add item back into inventory
        elif item_id.entityType == 'wieldable':
            self.free_hands += item_id.hand_slots  # add hand slots back

            print(f"You put away {item_id.name}.")
            self.items_held.remove(item_id)  # Remove from held items
            self.helditems_d.remove(item_id.hold_d)  # Remove from desc
            self.add_item(item_id)  # Add back to inventory
        else: pass