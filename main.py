import gui


WIDTH = 800
HEIGHT = 600
FRAMERATE = 0.01
POWERS_OF_ONE_HUNDRED = 2 #int(input("power: "))

window = gui.gui(WIDTH, HEIGHT, FRAMERATE, POWERS_OF_ONE_HUNDRED)
window.update_frames()
