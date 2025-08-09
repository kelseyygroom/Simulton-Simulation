# SPECIAL CLASS SPECIFICATIONS:
# This Special class acts as a Prey spawner. When it is placed in the simulation, it acts as a random spawner for prey objects. 20% of the time it adds either a Ball or Floater 
# object to the simulation. The other 80% of the time, it does nothing. A 'spawner' is benign; it can't consume any Prey and is not a Prey object. It simply randomly adds
# Prey objects to the simulation. 

from simulton import Simulton
import random
from ball import Ball
from floater import Floater


class Special(Simulton):
    height = 30
    width = 30
    
    def __init__(self, x, y):   # x and y arguments are the top left x,y coords
        Simulton.__init__(self, x, y, Special.height, Special.width)
    
    def update(self, model):
        add = random.random()
        if add <= 0.1:
            x, y = self.get_spawn_point()
            ball = Ball(x, y)
            model.add(ball)
        elif 0.1 < add <= 0.2:
            x,y = self.get_spawn_point()
            floater = Floater(x, y)
            model.add(floater)
    
    def get_spawn_point(self):
        x,y = self.get_location()
        w,h = self.get_dimension()
        return x+(w/2), y-(h/2)
        
    def display(self, canvas):
        canvas.create_rectangle(self._x, self._y, self._x+Special.height, self._y-Special.width, fill='cyan')

        