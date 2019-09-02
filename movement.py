import numpy as np


class moveable:
    def __init__(self, canvas, start, floor, side_length, mass, fill, velocity, name):
        self.CANVAS = canvas
        self.name = name
        self.start = start
        self.side_length = side_length
        self.mass = mass
        self.fill = fill
        self.floor = floor
        self.velocity = velocity
        self.draw()

    def draw(self):
        self.CANVAS.create_rectangle((self.start, 
                                      self.floor, 
                                      self.start - self.side_length, 
                                      self.floor - self.side_length), 
        fill=self.fill, tag=self.name)

    def update_coords(self):
        self.start += self.velocity
        self.draw()

    def detect_wall_collision(self, wall):
        if self.start - self.side_length <= wall:
            self.velocity = -self.velocity
            return True
        return False
    