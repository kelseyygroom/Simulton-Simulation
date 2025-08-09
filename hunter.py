# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    distance = 200
    
    def __init__(self, x, y):
        self.randomize_angle()
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self,x,y,20,20,self.get_angle(),5) # initialize base classes
         
    def update(self, model):
        in_range = {} # to associate distances (within 200) with prey objects
        for prey in model.find(lambda p: isinstance(p, Prey)):
            distance = Mobile_Simulton.distance(self, prey.get_location()) # explicitly call Mobile_Simulton distance method/not use self or it may get confused with class distance attribute 200
            if distance <= Hunter.distance:
                in_range[distance] = prey # associate distance with prey object
        if len(in_range) > 0:
            chase = in_range[min(in_range.keys())] # find closest prey object
            px, py = chase.get_location()
            hx, hy = self.get_location() # get center of prey and hunter
            x = px-hx
            y = py-hy   # calculate difference in centers of prey and hunter
            self.set_angle(atan2(x,y)) # calculate angle hunter must have to reach/eat closest prey
        self.move()
        Pulsator.update(self, model) # ensure that it grows and shrinks like a Pulsator
        
