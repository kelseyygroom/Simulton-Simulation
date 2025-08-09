# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.time_between_meals = 0 # initialize counter
    
    def update(self, model):
        self.time_between_meals += 1 # always update time between meals
        if self.time_between_meals >= 30: # if counter > 30, reset and decrease size
            self.time_between_meals = 0
            self._height -= 1
            self._width -= 1
        if self._width <= 0 or self._height <= 0: # if the pulsator disappears, remove from simulation
            model.simultons.remove(self)
        for prey in Black_Hole.update(self, model): # increase size for each prey eaten
            self._width += 1
            self._height += 1
            self.time_between_meals = 0
