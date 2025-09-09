import time
from picoscroll import PicoScroll, WIDTH, HEIGHT
from random import randrange
scroll = PicoScroll()

# Set up to make sure this works
for i in range(50,255):
    scroll.clear()
    scroll.set_pixel(1, 1, 255 - i)
    scroll.show()
    time.sleep(.01)

# The actual program: Sparkle
locations = []
while True:
    locations.append([randrange(0, WIDTH), randrange(0, HEIGHT)])
    scroll.clear()
    for i in range(0, len(locations)):
        currentLocation = locations[i]
        scroll.set_pixel(currentLocation[0], currentLocation[1], int(100 / (((5 - i) + 1) * 2)))
    scroll.show()
    if(len(locations) == 5):
        locations.pop(0)
        print(locations)
    time.sleep(0.1)