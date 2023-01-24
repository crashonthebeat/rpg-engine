import os

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
        self.inventory = {}
        self.container_inventory = []
        self.items_worn = []
        self.can_close = False
        self.open = True

    def desc(self):
        super(Person, self).desc()
        print("You are currently wearing:")
        for article in self.items_worn:
            print(f"{article.name.capitalize} on your {article.primary_slot}.")

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

    def look(self, obj, ind_obj):
        # This calls the describe method for an entity if the entity exists.

        # If player types 'look at object': 
        if ind_obj: obj = ind_obj
        else: pass
        
        # If player types 'look room' or 'look'
        if (obj == 'room' or obj == False):
            self.current_room.describe()
            return True
        else: 
            obj_id = self.current_room.find_object(obj)
            if obj_id == False:
                obj_id = self.current_room.find_box(obj)

        if obj_id == 'multiple': 
            print(f"Which {obj} do you want to look at?")
        elif obj_id == 'self':
            self.describe()
        elif obj_id: 
            obj_id.describe()
        else: 
            print(f"You can't find {obj}.")

    
    def search_for_box(self, box, parent_box):
        # This is the method to find a subcontainer in a given container.
        
        box_id = parent_box.find_box(box)
        if box_id == False:  # If the user box isn't found, stop function.
                print(f"You don't see the {box} here.")
        elif box_id == 'multiple':  # If search returned multiple boxes.
            print(f"Which {box} do you mean?")
            box_id = False
            # The user will need to be more specific.
        else: pass

        return box_id

    def open_box(self, box):
        box_id = self.search_for_box(box, self.current_room)
        
        if box_id == 'multiple': 
            pass
        elif box_id == False:
            pass
        else:
            box_id.open_self()

    def close_box(self, box):
        box_id = self.search_for_box(box, self.current_room)

        if box_id: box_id.close_self()

    
    def search_for_item(self, item, parent_box):
        # This searches a found container for an item given by user input
        # and returns the item_id as well as the id of any subcontainer it
        # was found in. 

        item_id, box_id = parent_box.find_item(item)

        if item_id == False:  # If the item isn't found, stop function.
            print(f"You don't see the {item} here.")
            return False, parent_box
        elif item_id == 'multiple':  # If there are multiple matches.
            print(f"Which {item} do you mean?")
            return False, parent_box
        else: return item_id, box_id


    def get_item(self, item, box):
        # This method will search for an item in the roomspace container and
        # all child containers, or from just a specific container if that 
        # container is given as the indirect object.

        # If the user gives a specific container, search for that first.
        if box: 
            box_id = self.search_for_box(box, self.current_room)
            if box_id == False: return True  # If no box is found, exit.
            elif box_id.open == False: 
                print(f"You need to open {box_id.name} first.")
                return True
        else: 
            box_id = self.current_room  # If no container is given.

        item_id, box_id = self.search_for_item(item, box_id)

        # If the item was found (and box if given), then add and remove the items.
        if item_id:
            box_id.remove_item(item_id)
            self.add_item(item_id)
            print(f"You get {item_id.name} from {box_id.name}!")
        else: pass


    def drop_item(self, item):
        # This method will find an item in the player's inventory and "drops" 
        # it into the room's inventory.

        item_id, box = self.search_for_item(item, self)

        if item_id:
            self.remove_item(item_id)
            self.current_room.add_item(item_id)
            print(f"You drop {item.name}")
        else: pass


    def place_item(self, item, box):
        # This method takes an item from the player's inventory and places it
        # into a given container.

        # First try to find the box, as in the methods above.
        box_id = self.search_for_box(box, self.current_room)
        if not box_id: return True
        elif box_id.open == False: 
            print(f"You need to open {box_id.name} first.")
            return True
        else: pass

        item_id, parent_id = self.search_for_item(item, self)
        if item_id:
            self.remove_item(item_id)
            box_id.add_item(item_id)
            print(f"You place {item_id.name} on {box_id.name.lower()}.")
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
            

    def wear_item(self, item):
        # This method takes an item from the player's inventory and
        # adds it to a slot.

        item_id, box_id = self.search_for_item(item, self)

        if not item_id:  # If there's no item on your body
            print(f"You don't have {item}")
            return True
        elif item_id.entityType != "wearable":
            print("You can't wear that!")
            return True
        else: pass

        if self.test_for_fit(item_id):
            for slot in item_id.used_slots.keys():
                self.wearable_slots[slot] -= item_id.used_slots[slot]
            
            print(f"You put on {item_id.name}")
            self.items_worn.append(item_id)
            self.remove_item(item_id)

    def unwear_item(self, item):
        item_id = False  # This might come back to bite me later.

        for article in self.items_worn:
            if item in article.name:
                item_id = article

        if item_id == False: return True
        else: pass
        
        for slot in item_id.used_slots.keys():
            self.wearable_slots[slot] += item_id.used_slots[slot]

        print(f"You remove {item_id.name}.")
        self.items_worn.remove(item_id)
        self.add_item(item_id)
