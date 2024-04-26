from constants import OBS
import random
from Items.OB.OB import OB

class Generator:
    def generate_ob(self, ob):
        # first generate the ob with the OB SPAWN INDEX
        # then remove the last ob from the list

        next_layer = ob.layer + 8 # layer used to add the new OB
        placement = random.randint(0, 2) # left middle right

        # adding the new one
        OBS.append(OB(next_layer, placement))
        OBS.remove(ob)

        print("replaced")
