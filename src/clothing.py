from src.items import Clothing

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
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = { 'head': 1 }
        self.primary_slot = "head"

class Veil(Clothing):
    # Anything thin that covers the head and can go under a hat or helm
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = { 'head': 0.5 }
        self.primary_slot = "head"

class Eyewear(Clothing):
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = { 'eyes': 1 }
        self.primary_slot = "eyes"

############
### TOPS ###
############

class Jacket(Clothing):
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = { 
            'l_should': 1, 'r_should': 1, 'l_arm': 1, 'r_arm': 1,
            'l_wrist': 1, 'r_wrist': 1, 'chest': 1, 'waist': 1
         }
        self.primary_slot = "torso"

class Shirt(Clothing):
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = { 
            'l_should': 1, 'r_should': 1, 'l_arm': 1, 'r_arm': 1,
            'chest': 1, 'waist': 1
         }
        self.primary_slot = "torso"

class Tunic(Clothing):
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = { 
            'l_should': 1, 'r_should': 1, 'chest': 1, 'waist': 1
         }
        self.primary_slot = "torso"

###############
### BOTTOMS ###
###############

class Trousers(Clothing):
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = { 
            'hips': 1, 'l_thigh': 1, 'r_thigh': 1, 
            'l_shin': 0.5, "r_shin": 0.5
         }
        self.primary_slot = "legs"

class Skirt(Clothing):
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = { 'hips': 1 }
        self.primary_slot = "legs"

################
### FOOTWEAR ###
################

class Boots(Clothing):
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = {
            'l_foot': 1, 'r_foot': 1,
            'l_shin': 1, 'r_shin': 1,
        }
        self.primary_slot = "feet"

class Shoes(Clothing):
    # Can be sandals also
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = {
            'l_foot': 1, 'r_foot': 1,
        }
        self.primary_slot = "feet"

#################
### FULL BODY ###
#################

class Dress(Clothing):
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = {
            'l_should': 1, 'r_should': 1, 'l_arm': 1, 'r_arm': 1,
            'chest': 1, 'waist': 1, 'hips': 0.5
        }
        self.primary_slot = "body"

class Robe(Clothing):
    # A loose dress basically that's tighter on the hips (cinching)
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = { 
            'l_should': 1.5, 'r_should': 1.5, 'l_arm': 0.5, 'r_arm': 0.5,
            'l_wrist': 0.5, 'r_wrist': 0.5, 'chest': 0.5, 
            'waist': 0.5, 'hips': 1.5
        }
        self.primary_slot = "body"

###################
### ACCESSORIES ###
###################

class Gloves(Clothing):
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = {'l_hand': 1, 'r_hand': 1}
        self.primary_slot = "hands"

class Amulet(Clothing):
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = {'neck': 1.5}
        self.primary_slot = "neck"

class Choker(Clothing):
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = {'neck': 0.5}
        self.primary_slot = "neck"

class Ring(Clothing):
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = {'fingers': 1}
        self.primary_slot = "finger"

class Cape(Clothing):
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = {'back': 1}
        self.primary_slot = "back"

class wornShield(Clothing):
    def __init__(self, name, desc):
        Clothing.__init__(self, name, desc)
        self.used_slots = {'back': 1}
        self.primary_slot = "back"
