from src.basicTypes import Entity, Container

class Item(Entity):
    # Basic item class, will be passed to all item types. Nothing is here
    # yet but it is separated from an entity for expansion's sake.
    def __init__(self, name, desc):
        Entity.__init__(self, name)
        self.desc = desc
        self.entityType = "item"  # The coding name for an item.
        self.is_container = False

class Interactable(Item):
    # These are items that cannot be moved from their locations but can
    # be used or interacted with.
    def __init__(self, name, desc):
        Entity.__init__(self, name)
        self.desc = desc
        self.entityType = "interactable"

class Tool(Item):
    # These are all the items that can be used or 'wielded' incl weapons.
    def __init__(self, name, desc, hand_slots):
        Entity.__init__(self, name)
        self.desc = desc
        self.hand_slots = hand_slots  # How many hands does this item need?
        self.entityType = "wieldable"
        self.hold_d = f"{self.name.capitalize()}"

class Clothing(Item):
    # These are all the things that can be worn on a person incl armor.
    def __init__(self, name, desc, primary_slot):
        Entity.__init__(self, name)
        self.desc = desc
        self.primary_slot = primary_slot
        self.entityType = "wearable"
        self.used_slots = {}  # What body slots the wearable uses.
        self.wear_d = f"{self.name.capitalize()} on your {self.primary_slot}."
        self.is_container = False

class Bag(Clothing, Container):
    # This class is for all containers that can be worn.
    def __init__(self, name, desc, primary_slot):
        Clothing.__init__(self, name, desc, primary_slot)
        self.desc = desc
        self.primary_slot = primary_slot
        self.entityType = "wearable"
        self.is_container = True
        self.open = False  # All wearable boxes are closed by default
        self.can_close = True
        self.inventory = {}
        self.container_inventory = []

    def equip_bag(self):
        # These are the actions that happen when a bag is equipped
        self.open = True
        self.can_close = False

    def unequip_bag(self):
        # These happen when a bag is unequipped.
        self.open = False
        self.can_close = True

# The following are classes I'm naming for future addition.

# Not sure how combat is going to work yet, so I'm waiting until then to
# build out these two classes.
class Weapon(Tool):
    def __init__(self, name, desc, hand_slots):
        Tool.__init__(self, name, desc, hand_slots)

class Armor(Clothing):
    def __init__(self, name, desc, primary_slot):
        Clothing.__init__(self, name, desc, primary_slot)