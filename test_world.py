from src.player import Player
from src.rooms import Room
from src.items import Item
from src.basicTypes import Container
from src.clothing import *
from termcolor import colored

def intr(word):
    # This method will color parts of a name that are unique from all other
    # items, so that it can be uniquely interacted with.
    return colored(word, "cyan")

# PLAYER INITIALIZATION
pc = Player('Thom the Tester')

# ITEM INITIALIZATION
stick = Item(
    f"a basic {intr('stick')}", 
    ["A basic stick that could be used as a weapon in a pinch."]
    )

longsword = Item(
    f"a {intr('longsword')}",
    ["An adequately crafted longsword."]
)

wood_axe = Item(
    f"a {intr('woodcutters axe')}",
    ["Your trusty wood cutting axe."]
)

dagger = Item(
    f"a {intr('dagger')}",
    ["A sharp, easily concealed dagger."]
)

leather_torso = Tunic(
    f"a {intr('leather brigandine')}",
    [
        "A flexible looking leather vest that covers the wearers torso and hips",
        "but not the arms."
    ],
)

cotton_breeches = Trousers(
    f"a pair of {intr('cotton breeches')}",
    ["A sturdy and comfortable pair of brown breeches."]
)

leather_boots = Boots(
    f"a pair of {intr('leather boots')}",
    ["A strong and well worn pair of boots."]
)

cork_sandals = Shoes(
    f"A pair of {intr('cork sandals')}",
    ["You still don't know why you bought these."]
)

# CONTAINER INITIALIZATION

start_cabin_rack = Container(
    "Your weapon rack", "mounted on the weapon rack",
    True, False)

start_cabin_rack.inventory = {
    longsword: 1,
    wood_axe: 1
}

start_cabin_chest = Container(
    "Your bedside chest", "in your bedside chest",
    False, True)

start_cabin_chest.inventory = {
    leather_torso: 1,
    cotton_breeches: 1,
    leather_boots: 1
}

# ROOM INITIALIZATION

start_cabin = Room("Your Cabin")

cabin_clearing = Room("Outside your Cabin")
outhouse = Room("The Outhouse")
woodshed = Room("Cabinside Woodshed")
behind_cabin = Room("Behind your Cabin")
outdoor_kitchen = Room("A Small Eating Area")
riverbank_1 = Room("Riverbank")
riverbank_2 = Room("Riverbank")
forest_path_1 = Room("A path through the forest")
forest_path_2 = Room("A path through the forest")
forest_path_3 = Room("A path through the forest")

start_cabin.inventory = {
    cork_sandals: 1
}

start_cabin.container_inventory = [
    start_cabin_chest, start_cabin_rack
]

riverbank_1.inventory = {
    stick: 2
}

forest_path_2.inventory = {
    dagger: 1
}

# ROOM DESCRIPTIONS

start_cabin.desc = [
    "You look around your cabin, the place you've lived for the last ten",
    "years. It's the first place since childhood that's felt like home.",
    "Your bed sits nestled in the southeast corner next to a small table.",
    "In the center is a modest brick stove with a few cooking elements and",
    "a chimney that pierces your roof."
]
start_cabin.desc_quick = [
    "You are now in your cabin. It's warm and feels like home."
]
cabin_clearing.desc = [
    "You stand in front of your cabin, with walls made of oak logs and a",
    "steep slate-tile roof that also forms your east and west walls. The",
    "only window sits at the back of the cabin, but is usually covered",
    "with a large banner. You don't typically spend a lot of time indoors",
    "anyway."
]
cabin_clearing.desc_quick = [
    "You stand outside your cabin in a small clearing."
]
outhouse.desc = [
    "They say you should't defecate where you masticate, which is why you",
    "built your outhouse on the opposite side. Like all outhouses, it's a",
    "humble wooden shack with a seven pointed star on the door. Luckily for",
    "you, the landscape slopes to the southwest from here in case of any",
    "overflow issues."
]
outhouse.desc_quick = [
    "You stand next to your outhouse, it smells used."
]
woodshed.desc = [
    "The west wall of your cabin has been extended with a long, open shed to",
    "store firewood. You are standing in a small area cleared of foliage and",
    "branches. In the center is a large chopping block. "
]
woodshed.desc_quick = [
    "You stand by your woodshed, contemplating chopping more."
]
behind_cabin.desc = [
    "The backside of your cabin is decorated with an animal skull and the",
    "banner of your former lord."
]
behind_cabin.desc_quick = [
    "You lean against the back wall of your cabin, staring into the forest."
]
outdoor_kitchen.desc = [
    "On the river side of your cabin, you have set up a fire pit with a few",
    "wooden benches, and a table for when you are inclined to eat outside.",
    "There are a few tanning racks and drying huts that line this side of",
    "your cabin, and a couple barrels for storing things you don't want in",
    "the cabin."
]
outdoor_kitchen.desc_quick = [
    "You stand next to your outdoor firepit, watching the river roll by."
]
riverbank_1.desc = [
    "You are on the east bank of a tributary of the Evasor River. The river",
    "is gentle and full of fish when they're in season, a good reason why",
    "you built your cabin along it. On the other side of the river is a",
    "fairly steep hill, so even if you had a bridge to cross, there wouldn't",
    "be much of a point."
]
riverbank_1.desc_quick = [
    "You stand by the banks of a small river."
]
riverbank_2.desc = riverbank_1.desc
riverbank_2.desc_quick = riverbank_1.desc_quick
forest_path_1.desc = [
    "You are on a narrow path through the forest of Arvanion. Sunlight",
    "creeps in through the canopy above you, providing enough light to move",
    "comfortably and to see any threats that might be on the road before you.",
    "The road, though frequently travelled by you, is still barely worn",
    "through the thick brush. Over the sound of the river to the east, you",
    "can hear the birdsong and occasional predatory calls of nature."
]
forest_path_1.desc_quick = [
    "You stand the forest path between your home and the rest of the world."
]
forest_path_2.desc = forest_path_1.desc
forest_path_2.desc_quick = forest_path_1.desc
forest_path_3.desc = forest_path_1.desc
forest_path_3.desc_quick = forest_path_1.desc

# ROOM EXITS

start_cabin.exits = {
    "north": cabin_clearing
}
cabin_clearing.exits = {
    "north": forest_path_1,
    "east": riverbank_2,
    "southeast": outdoor_kitchen,
    "south": start_cabin,
    "southwest": woodshed,
    "west": outhouse,
}
outhouse.exits = {
    "east": cabin_clearing,
    "south": woodshed
}
woodshed.exits = {
    "north": outhouse,
    "northeast": cabin_clearing,
    "southeast": behind_cabin
}
behind_cabin.exits = {
    "northwest": woodshed,
    "northeast": outdoor_kitchen,
    "southeast": riverbank_1
}
outdoor_kitchen.exits = {
    "northwest": cabin_clearing,
    "north": riverbank_2,
    "south": riverbank_1,
    "southwest": behind_cabin
}
riverbank_1.exits = {
    "northwest": behind_cabin,
    "north": outdoor_kitchen,
}
riverbank_2.exits = {
    "south": outdoor_kitchen,
    "west": cabin_clearing
}
forest_path_1.exits = {
    "north": forest_path_2,
    "south": cabin_clearing
}
forest_path_2.exits = {
    "north": forest_path_3,
    "south": forest_path_1
}
forest_path_3.exits = {
    "south": forest_path_2
}

pc.current_room = start_cabin