# -*- coding: utf-8 -*-
"""
Controller of interactive video game Swim Little Fish Swim

@author: Amanda Sutherland, Ziyu (Selina) Wang

last modified: 10-29-15
"""
import pygame
from pygame.locals import *

class SwimFishMouseController:
    def __init__(self,model,view):
        self.model = model
        self.view = view
    
    def handle_mouse_event(self,event):
        if event.type == MOUSEMOTION:
            self.model.fish.x = event.pos[0]
            self.model.fish.y = event.pos[1]
            self.model.fish.rect.x = event.pos[0]-.5*self.model.fish.width
            self.model.fish.rect.y = event.pos[1]-.5*self.model.fish.height

    def handle_collision(self):
        for monster in self.model.monsters:
            if self.model.fish.rect.colliderect(monster.rect):
                return True


