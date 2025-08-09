# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10  
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 20, 20)
    
    def update(self, model):
        eaten = set()
        for prey in model.find(lambda p: isinstance(p, Prey)): # if object is a prey
            if self.contains(prey): # if prey is inside black hole
                eaten.add(prey)     # eat it and remove from simulation
                model.simultons.remove(prey)
        return eaten
        
    
    def display(self, canvas):
        dimension = self.get_dimension() # need to get dimensions so when pulsator inherits, it changes size
        canvas.create_oval(self._x-dimension[0]      , self._y-dimension[1],
                                self._x+dimension[0], self._y+dimension[1],
                                fill='black')
    
    def contains(self, prey_object):
        return Simulton.distance(self, (prey_object._x, prey_object._y)) < self._width
