from src.player import Player
from src.rooms import Room
from src.items import Item
from src.basicTypes import Container
from termcolor import colored

def intr(word):
    return colored(word, "cyan")

# PLAYER INITIALIZATION
pc = Player('testplayer')

# ITEM INITS
stick = Item(
    "a basic stick", 
    f"A {intr('stick')} lies unused, looking suspiciously like a weapon."
    )

sword = Item(
    "a longsword",
    f"A {intr('longsword')} sits in this room, ready to draw blood."
)

leather_armor = Item(
    "a set of leather armor",
    f"A {intr('set of leather armor')} is laid on the floor."
)

player_room_rack = Container("A weapon rack")
player_room_rack.list_desc = ("mounted on the weapon rack")
player_room_rack.open = True

player_room_chest = Container(f"{pc.name}'s chest")
player_room_chest.list_desc = (f"in {pc.name}'s chest")
player_room_chest.open = False

# ROOM INITS
player_room = Room(f"{pc.name.capitalize()}'s Room")
player_room.list_desc = "Lying on the floor"
endless_hallway = Room("An endless hallway")

pc.current_room = player_room   # Initializes current room for test world.

# INVENTORY INITS
player_room.inventory = {
    stick: 2,
}

player_room_rack.inventory = {
    sword: 1
}

player_room_chest.inventory = {
    leather_armor :1
}

player_room.container_inventory = [
    player_room_rack,
    player_room_chest
]

# ROOM DESCRIPTIONS (list of strings)
player_room.detail_desc = [
    f"{pc.name.capitalize()}'s room is a spartan but cozy room. The ",
    "floor is made of unfinished pine covered with hide rugs. The ", 
    "exterior facing walls, are mostly masonry with an oak frame, while ",
    "the interior walls are simply oak planks. At the center of the ",
    "sole exterior wall lies your bed, just big enough for ome person to ",
    "sleep somewhat comfortably on."
]

player_room.desc = [
    "Your room is just the way you left it."
]

endless_hallway.detail_desc = [
    "This is a featureless hallway, there are no doors except for the one",
    "you just came through, and nothing hangs on the walls. You try to look",
    "at either end and just see darkness."
]

endless_hallway.desc = [
    "The endless hallway continues to exert a horrifying presence."
]

# ROOM EXITS (dict of direction: room var)
player_room.exits = {
    "south": endless_hallway
}

endless_hallway.exits = {
    "north": player_room,
    "east": endless_hallway,
    "west": endless_hallway
}