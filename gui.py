import tkinter as tk
import time
import objects


class gui:
    def __init__(self, width, height, framerate, power):
        self.WIDTH = width
        self.HEIGHT = height
        self.FRAMERATE = framerate
        self.root = tk.Tk()
        self.CANVAS = tk.Canvas(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.CANVAS.pack()
        self.OBJECTS = objects.objects(self.CANVAS, self.WIDTH, self.HEIGHT, power)
        self.setup()

    def setup(self):
        self.OBJECTS.create_environment()

    def clear_frames(self, tags):
        for tag in tags:
            for item in self.CANVAS.find_withtag(tag):
                self.CANVAS.delete(item)

    def update_frames(self):
        while True:
            time.sleep(self.FRAMERATE)
            self.clear_frames(['box', 'bob'])
            self.OBJECTS.draw_frame()
            self.CANVAS.update()

