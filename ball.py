# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey
import random
import math


class Ball(Prey): 
    radius = 5
    def __init__(self, x, y):
        self.randomize_angle() # starts moving at a random angle
        Prey.__init__(self, x, y, 10, 10, self.get_angle(), 5)

    def update(self, model):
        self.move() # simple movement inherited from Prey->Mobile_Simulton class
            
    def display(self, canvas):
        canvas.create_oval(self._x-Ball.radius      , self._y-Ball.radius,
                                self._x+Ball.radius, self._y+Ball.radius,
                                fill='blue') # size of Ball objects never change, so i can use Ball.radius measurement/don't have to get dimensions every time
        