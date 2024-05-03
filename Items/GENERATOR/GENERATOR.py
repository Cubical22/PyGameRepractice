from constants import OBS
import random
from Items.OB.OB import OB

class Generator:
    def generate_ob(self, ob):
        # first generate the ob with the OB SPAWN INDEX
        # then remove the last ob from the list

        next_layer = ob.layer + 8 # layer used to add the new OB

        # adding the new one
        OBS.append(OB(next_layer, self.generate_placement()))
        OBS.remove(ob)

    def reset_ob(self):
        OBS.clear()
     
        for i in range(0,8):
            OBS.append(OB(i, self.generate_placement(i == 0)))


    def generate_placement(self, is_first= False):
        placement = None
        while True:
            placement = random.randint(0, 2) # left middle right

            if not is_first:
                last_cell_pos = OBS[-1].place_index

                if last_cell_pos == 1 and placement == 1:
                    continue

            break
    
        return placement