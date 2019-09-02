import numpy as np
import random
import movement


class objects:
    def __init__(self, canvas, width, height, power):
        self.CANVAS = canvas
        self.WIDTH = width
        self.HEIGHT = height
        self.floor = self.HEIGHT * (4 / 5)
        self.wall = self.WIDTH * (1 / 10)
        self.power = power
        self.current = []
        self.collisions = 0

    def make_floor(self):
        self.CANVAS.create_line((0, self.HEIGHT * (4 / 5), self.WIDTH, self.HEIGHT * (4 / 5)), width=2, tag="floor")

    def make_wall(self):
        self.CANVAS.create_line((self.WIDTH * (1 / 10), 0, self.WIDTH * (1 / 10), self.HEIGHT * (4 / 5)), width=2, tag="wall")

    def make_block(self, start, side, mass, fill, velocity, name):
        self.current.append(
            movement.moveable(self.CANVAS, start, self.floor, side, mass, fill, velocity, name)
            )

    def create_environment(self):
        self.make_floor()
        self.make_wall()
        self.make_block(self.WIDTH * 0.5, 50, 100, "red", 0, "bob")
        self.make_block(self.WIDTH * 0.9, 100, 100 ** self.power, "blue", -0.8, "bob")

    def draw_frame(self):
        self.detect_block_collision(self.current)
        for moveable in self.current:
            if moveable.detect_wall_collision(self.wall):
                self.collisions += 1
                print(self.collisions)
            moveable.update_coords()

    def detect_block_collision(self, obj):
        if obj[0].start >= obj[1].start - obj[1].side_length:
            m1, m2 = obj[0].mass, obj[1].mass
            u1, u2 = obj[0].velocity, obj[1].velocity

            v1 = (((m1 - m2) / (m1 + m2)) * u1) + (((2 * m2) / (m1 + m2)) * u2)
            v2 = (((2 * m1) / (m1 + m2)) * u1) + (((m2 - m1) / (m1 + m2)) * u2)

            obj[0].velocity = v1
            obj[1].velocity = v2

            self.collisions += 1
            print(self.collisions)

