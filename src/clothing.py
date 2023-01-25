from src.items import Clothing, Bag

# EXPLANATION OF SLOTS:
# Any kind of undergarment takes half a slot.
# Head:     Sits on or around the head.
# Face:     Covers or goes around the face.
# Eyes:     Covers the eyes.
# Neck:     Around the neck.
# Hands:    Different from usable slots
# Back:     Hangs from back (shield, cape)

# The classes listed below are just basic types with pre-assigned slots.

################
### HEADGEAR ###
################

class Hat(Clothing):
    def __init__(self, name, desc, primary_slot='head'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = { 'head': 1 }

class Veil(Clothing):
    # Anything thin that covers the head and can go under a hat or helm
    def __init__(self, name, desc, primary_slot='head'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = { 'head': 0.5 }

class Eyewear(Clothing):
    def __init__(self, name, desc, primary_slot='eyes'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = { 'eyes': 1 }

############
### TOPS ###
############

class Jacket(Clothing):
    def __init__(self, name, desc, primary_slot='torso'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = { 
            'l_should': 1, 'r_should': 1, 'l_arm': 1, 'r_arm': 1,
            'l_wrist': 1, 'r_wrist': 1, 'chest': 1, 'waist': 1
         }

class Shirt(Clothing):
    def __init__(self, name, desc, primary_slot='torso'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = { 
            'l_should': 1, 'r_should': 1, 'l_arm': 1, 'r_arm': 1,
            'chest': 1, 'waist': 1
         }

class Tunic(Clothing):
    def __init__(self, name, desc, primary_slot='torso'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = {
            'l_should': 1, 'r_should': 1, 'chest': 1, 'waist': 1
        }

###############
### BOTTOMS ###
###############

class Trousers(Clothing):
    def __init__(self, name, desc, primary_slot='legs'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = { 
            'hips': 1, 'l_thigh': 1, 'r_thigh': 1, 
            'l_shin': 0.5, "r_shin": 0.5
         }

class Skirt(Clothing):
    def __init__(self, name, desc, primary_slot='legs'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = { 'hips': 1 }

################
### FOOTWEAR ###
################

class Boots(Clothing):
    def __init__(self, name, desc, primary_slot='feet'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = {
            'l_foot': 1, 'r_foot': 1,
            'l_shin': 1, 'r_shin': 1,
        }

class Shoes(Clothing):
    # Can be sandals also
    def __init__(self, name, desc, primary_slot='feet'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = {
            'l_foot': 1, 'r_foot': 1,
        }

#################
### FULL BODY ###
#################

class Dress(Clothing):
    def __init__(self, name, desc, primary_slot='body'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = {
            'l_should': 1, 'r_should': 1, 'l_arm': 1, 'r_arm': 1,
            'chest': 1, 'waist': 1, 'hips': 0.5
        }

class Robe(Clothing):
    # A loose dress basically that's tighter on the hips (cinching)
    def __init__(self, name, desc, primary_slot='body'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = { 
            'l_should': 1.5, 'r_should': 1.5, 'l_arm': 0.5, 'r_arm': 0.5,
            'l_wrist': 0.5, 'r_wrist': 0.5, 'chest': 0.5, 
            'waist': 0.5, 'hips': 1.5
        }

##################
### BACK ITEMS ###
##################

class Cape(Clothing):
    def __init__(self, name, desc, primary_slot='back'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = {'back': 1}

class Backpack(Bag):
    def __init__(self, name, desc, primary_slot='back'):
        Bag.__init__(self, name, desc, primary_slot)
        self.used_slots = {'back': 1}
        self.list_desc = 'in this backpack'

###################
### ACCESSORIES ###
###################

class Gloves(Clothing):
    def __init__(self, name, desc, primary_slot='hands'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = {'l_hand': 1, 'r_hand': 1}

class Amulet(Clothing):
    def __init__(self, name, desc, primary_slot='neck'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = {'neck': 1.5}

class Choker(Clothing):
    def __init__(self, name, desc, primary_slot='neck'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = {'neck': 0.5}

class Ring(Clothing):
    def __init__(self, name, desc, primary_slot='finger'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = {'fingers': 1}

class wornShield(Clothing):
    def __init__(self, name, desc, primary_slot='back'):
        Clothing.__init__(self, name, desc, primary_slot)
        self.used_slots = {'back': 1}
