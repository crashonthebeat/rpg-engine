import src.cmdparse as cmd

from test_world import *

# List of action verbs for each category of action
# These are explained below in the validate_action method.
travel_actions = ['go', 'travel', 'enter', 'walk', 'run', 'jog', 'sneak']
describe_actions = ['look', 'view', 'describe']
take_actions = ['take', 'get', 'grab', 'retrieve', 'nab']
drop_actions = ['drop', 'yeet', 'toss']
place_actions = ['place', 'put', 'set', 'mount']
wear_actions = ['equip', 'eq', 'wear', 'don', 'wield', 'arm']
unwear_actions = ['unequip', 'uq', 'remove', 'strip', 'unarm']


def validate_action(action, obj, ind_obj, prep):
    # Travel Action (Moving between roomspaces): 
    if action in travel_actions: pc.travel(action, obj)
    # Describe Action (Getting an object's description): 
    elif action in describe_actions: pc.look(obj, ind_obj)
    # Take Action (Taking an item from an inventory):
    elif action in take_actions: pc.get_item(obj, ind_obj)
    # Drop Action (Removing an item from pc's inventory):
    elif action in drop_actions: pc.drop_item(obj)
    # Place Action (Placing an own item into another inventory):
    elif action in place_actions: pc.place_item(obj, ind_obj, prep)
    # Open and Close Actions (Container State Interaction):
    elif action == 'open': pc.open_box(obj)
    elif action == 'close': pc.close_box(obj)
    # Equip and Unequip Actions (Holding Items):
    elif action in wear_actions: pc.equip_item(obj, action)
    elif action in unwear_actions: pc.unequip_item(obj)
    # Exit to Menu: 
    elif action == "exit": return False
    # Default: 
    else: print(f"You don't know how to {action}")

    return True

def command_loop(game=True):
    pc.current_room.enter()
    while game:
        print("What would you like to do?")
        user_input = input("> ")
        action, obj, ind_obj, prep = cmd.parse(user_input)

        game = validate_action(action, obj, ind_obj, prep)


if __name__ == "__main__":
    command_loop()