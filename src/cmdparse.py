# This is the command parser. It takes a user input and then divides that
# input into three basic elements: the verb (primary action), the direct 
# object (the recipient of the action), and the indirect object (the 
# recipient of the object). 
# 
# For those who slept through grammar class, in the command "drop sword", 
# drop is the verb, and sword is the direct object, as the sword is what
# you are dropping. In the command, "take sword from stone", "take" is 
# the action, the sword is what you are "taking", and the stone is the 
# indirect object, indicating that is where you are taking the sword from.
# This indirect object is typically after a preposition. 
# 
# This will be explained to players in the help file. 

fillers = ["the", "a", "an", "i", "we", "me", "us", "some"]
prepositions = ["with", "to", "in", "from", "on", "of", "at"]
directions = ["north", "n", "east", "e", "south", "s", "west", "w",
              "up", "down", "northeast", "ne", "southeast", "se", 
              "southwest", "sw", "northwest", "nw"]

def remove_fillers(user_input):
    i = 0
    while i < len(user_input):
        if user_input[i] in fillers:
            user_input.remove(user_input[i])
            i += 1
        else: 
            i += 1

    return user_input

def get_objects(user_input):
    prep = False
    ind_obj = False

    for i in range(len(user_input)-1):
        if user_input[i] in prepositions:
            prep = user_input.pop(i)
            indobj_index = i
        else: continue

    if prep:
        ind_obj = " ".join(user_input[indobj_index:])
        obj = " ".join(user_input[:indobj_index])
    else:
        obj = ' '.join(user_input)
        
    return obj, ind_obj, prep

def parse(user_input):
    # This is the primary function of this file, and will return all
    # grammatical objects. 

    user_input = user_input.lower().split(" ") # Split user_input into a list
    user_input = remove_fillers(user_input) # Remove filler words

    action = user_input.pop(0) # Get action from user_input

    if action in directions: # Allows a user to input just a direction.
        return "go", action, False, False

    if len(user_input) == 0: return action, False, False, False

    obj, ind_obj, prep = get_objects(user_input)

    return action, obj, ind_obj, prep