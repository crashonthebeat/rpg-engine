from src.basicTypes import Entity

class Item(Entity):
    # Basic item class, will be passed to all item types. Nothing is here
    # yet but it is separated from an entity for expansion's sake.

    def __init__(self, name, desc):
        Entity.__init__(self, name)
        self.desc = desc
        self.entityType = "item"  # The coding name for an item.