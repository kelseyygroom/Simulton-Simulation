# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random, uniform


class Floater(Prey): 
    radius = 5
    def __init__(self, x, y):
        self.randomize_angle()
        Prey.__init__(self, x, y, 10, 10, self.get_angle(), 5)
    
    def update(self, model):
        change = random() # >=0.3, change both; <0.3, change neither
        bounds = [3, 7]
        if change <= 0.3:
            self._angle = self._angle + uniform(-0.5, 0.5)
            speed = self._speed + uniform(-0.5, 0.5)
            if speed < 3:
                self._speed = 3
            elif speed > 7:
                self._speed = 7
            else:
                self._speed = speed
            #self._speed = self._speed * uniform if 
            # change both the speed and the angle
        self.move()
        self.wall_bounce()
    
    def display(self, canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill='red')
