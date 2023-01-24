from src.basicTypes import Entity

class Item(Entity):
    # Basic item class, will be passed to all item types. Nothing is here
    # yet but it is separated from an entity for expansion's sake.
    def __init__(self, name, desc):
        Entity.__init__(self, name)
        self.desc = desc
        self.entityType = "item"  # The coding name for an item.

class Interactable(Item):
    # These are items that cannot be moved from their locations but can
    # be used or interacted with.
    def __init__(self, name, desc):
        Entity.__init__(self, name)
        self.desc = desc
        self.entityType = "interactable"

class Wieldable(Item):
    # These are all the items that can be used or 'wielded'
    def __init__(self, name, desc):
        Entity.__init__(self, name)
        self.desc = desc
        self.entityType = "wieldable"
        self.hand_slots = 1  # How many hands does this item need to hold it?

class Wearable(Item):
    # These are all the things that can be worn on a person.
    def __init__(self, name, desc):
        Entity.__init__(self, name)
        self.desc = desc
        self.entityType = "wearable"
        self.used_slots = {}  # What body slots the wearable uses.
        self.primary_slot = False

class Clothing(Wearable):
    # These are all the things that can be worn on a person.
    def __init__(self, name, desc):
        Wearable.__init__(self, name, desc)