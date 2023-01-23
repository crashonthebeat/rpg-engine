import os

from time import sleep
from src.basicTypes import Container

def clear_screen():
    # This method will clear the screen to clean it up.

    return True  # Disabling this method while in production.
    
    sleep(0.5)

    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

class Player(Container):
    # The player has an inventory, so it is a container. 

    def __init__(self, name):
        Container.__init__(self, name)
        self.desc = [f"Nothing can be said about {self.name}."]

    def travel(self, action, direction):
        # This is the travel method used to move the player between
        # roomspaces, as well as sub-spaces and overworld.

        if direction in self.current_room.exits.keys():
            print(f"You {action} {direction}.")
            new_room = self.current_room.exits[direction]
            # clear_screen()
            print(f"You enter {new_room.name}")
            new_room.enter()
            self.current_room = new_room
        else:
            print(f"You cannot go {direction}.")

    def look(self, obj, ind_obj):
        # This calls the describe method for an entity if the entity exists.

        # If player types 'look at object': 
        if ind_obj: obj = ind_obj
        
        # If player types 'look room' or 'look'
        if (obj == 'room' or obj == False):
            self.current_room.detail_describe()
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


    def get_item(self, item, box):
        # This method will search for an item in the roomspace container and
        # all child containers, or from just a specific container if that 
        # container is given as the indirect object.

        # If the user gives a specific container, search for that first.
        if box: 
            box_id = self.current_room.find_box(box)
            if box_id == False:  # If the user box isn't found, stop function.
                print(f"You don't see the {box} here.")
                return True
            elif box_id == 'multiple':  # If search returned multiple boxes.
                print(f"Which {box} do you mean?")
                # The user will need to be more specific.
                return True
            elif box_id == 'closed':
                print(f"You need to open that first!")
                return True
        else: box_id = self.current_room  # If no container is given.

        # Finally, search for the item in the given box or in the room.
        item_id, parent_id = box_id.find_item(item)

        if item_id == False:  # If the item isn't found, stop function.
            print(f"You don't see the {item} here.")
            return True
        elif item_id == 'multiple':  # If there are multiple matches.
            print(f"Which {item} do you mean?")
            return True
        elif item_id and parent_id:  # If item was found in a sub-container.
            box_id = parent_id
        else: 
            box_id = self.current_room

        # If the item was found (and box if given), then add and remove the items.
        box_id.remove_item(item_id)
        self.add_item(item_id)
        print(f"You get {item_id.name} from {box_id.name}!")


    def drop_item(self, obj):
        # This method will find an item in the player's inventory and "drops" 
        # it into the room's inventory.

        obj_id, holder = self.find_item(obj)

        if obj_id == 'multiple':
            print(f"Which {obj} do you want to drop?")
        elif obj_id:
            self.remove_item(obj_id)
            self.current_room.add_item(obj_id)
            print(f"You drop {obj_id.name}")
        else:
            print(f"You don't have {obj}")

    def place_item(self, item, box):
        # This method takes an item from the player's inventory and places it
        # into a given container.

        # First try to find the box, as in the methods above.
        box_id = self.current_room.find_box(box)
        if box_id == 'multiple':
            print(f"Which {box} do you want to take from?")
        elif box_id == False:
            print(f"You can't find a {box} here.")
            return True
        elif box_id == 'closed':
            print(f"You need to open {box_id.name} first!")
            return True

        item_id, parent_id = self.find_item(item)

        if item_id == 'multiple':
            print(f"Which {item} do you want to drop?")
        elif item_id:
            self.remove_item(item_id)
            box_id.add_item(item_id)
            print(f"You place {item_id.name} on {box_id.name.lower()}.")
        else:
            print(f"You don't have {item}")