import src.cmdparse as cmd # Import the command parser module

from test_world import *

travel_actions = ['go', 'travel', 'enter', 'walk', 'run', 'jog', 'sneak']
describe_actions = ['look', 'view', 'describe']
take_actions = ['take', 'get', 'grab', 'retrieve', 'nab']
drop_actions = ['drop', 'yeet', 'toss']
place_actions = ['place', 'put', 'set', 'mount']

def validate_action(action, obj, ind_obj, prep):
    # Travel Action: 
    if action in travel_actions: pc.travel(action, obj)
    # Describe Action: 
    elif action in describe_actions: pc.look(obj, ind_obj)
    # Take Action:
    elif action in take_actions: pc.get_item(obj, ind_obj)
    # Drop Action:
    elif action in drop_actions: pc.drop_item(obj)
    # Place Action:
    elif action in place_actions: pc.place_item(obj, ind_obj)
    # Exit to Menu: 
    elif action == "exit": return False
    # Default: 
    else: print(f"You don't know how to {action}")

    return True

def command_loop(game=True):
    while game:
        print("What would you like to do?")
        user_input = input("> ")
        action, obj, ind_obj, prep = cmd.parse(user_input)

        game = validate_action(action, obj, ind_obj, prep)


if __name__ == "__main__":
    pc.current_room.enter()
    command_loop()