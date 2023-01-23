class Item:
    def __init__(self, name, room_desc):
        self.name = name
        self.room_desc = room_desc
        self.desc = [f"I see nothing special about {self.name}."]

    def describe(self):
        for line in self.desc:
            print(line)
