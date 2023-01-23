import os

from time import sleep
from src.basicTypes import Container

def clear_screen():
    sleep(1)

    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

class Player(Container):
    def __init__(self, name):
        Container.__init__(self, name)
        self.desc = [f"Nothing can be said about {self.name}."]

    def travel(self, action, direction):
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

    def get_item(self, obj, ind_obj):
        if ind_obj:
            ind_obj_id, holder = self.current_room.find_item(ind_obj)
            if ind_obj_id == 'multiple':
                print(f"Which {ind_obj} do you want to take from?")
            elif ind_obj_id == False:
                print(f"You can't find a {ind_obj} here.")
            else: 
                obj_id, holder = ind_obj_id.find_item(obj)
        else:
            obj_id, holder = self.current_room.find_item(obj)

        if obj_id == 'multiple':
            print(f"Which {obj} do you want to take?")
        elif obj_id and holder:
            holder.remove_item(obj_id)
            self.add_item(obj_id)
            print(f"You get {obj_id.name} from {holder.name.lower()}.")
        elif obj_id and holder == False:
            self.add_item(obj_id)
            print(f"You get {obj_id.name}")
        else:
            print(f"You can't find a {obj} here.")

    def drop_item(self, obj):
        obj_id, holder = self.find_item(obj)

        if obj_id == 'multiple':
            print(f"Which {obj} do you want to drop?")
        elif obj_id:
            self.remove_item(obj_id)
            self.current_room.add_item(obj_id)
            print(f"You drop {obj_id.name}")
        else:
            print(f"You don't have {obj}")

    def place_item(self, obj, ind_obj):
        print("DEBUG SEARCHING FOR " + ind_obj)
        box_id = self.current_room.find_box(ind_obj)
        if box_id == 'multiple':
            print(f"Which {ind_obj} do you want to take from?")
        elif box_id == False:
            print(f"You can't find a {ind_obj} here.")
            return True

        obj_id, holder = self.find_item(obj)

        if obj_id == 'multiple':
            print(f"Which {obj} do you want to drop?")
        elif obj_id:
            self.remove_item(obj_id)
            box_id.add_item(obj_id)
            print(f"You place {obj_id.name} on {box_id.name.lower()}.")
        else:
            print(f"You don't have {obj}")