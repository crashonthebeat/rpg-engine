from src.basicTypes import Entity

class Item(Entity):
    def __init__(self, name, desc):
        Entity.__init__(self, name)
        self.desc = desc
        self.entityType = "item"