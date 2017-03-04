import pygame,random
from pygame.locals import *

class Controller:

    def __init__(self, location, l_key, r_key, u_key, d_key, place_key, image_path):
        self.location = location
        self.r_key = r_key
        self.l_key = l_key
        self.u_key = u_key
        self.d_key = d_key
        self.place_key = place_key
        self.image = pygame.load_image(image_path)

    def shift(self, direction):
        if direction == "right":
            self.location[1] += 1
        elif direction == "left":
            self.location[1] -= 1
        elif direction == "up":
            self.location[0] -= 1
        elif direction == "down":
            self.location[0] -= 1
