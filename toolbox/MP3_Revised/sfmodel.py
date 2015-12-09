# -*- coding: utf-8 -*-
"""
Model of interactive video game Swim Little Fish Swim

@author: Amanda Sutherland, Ziyu (Selina) Wang

last modified: 10-29-15
"""
import pygame
from pygame.locals import *
from random import randint
import time

class SwimFishModel:
    """ Encodes the game state """
    def __init__(self):
        self.fish = Fish((209, 95, 238), 60, 50, 200, 450)
        self.monsters = []
        self.choices = ['images/octopus1_png.png', 'images/crab1.png', 'images/jellyfish.png', 'images/shark.png', 'images/stingray.png']

class Monster:
    """ Encodes the state of a monster in the game """
    def __init__(self,height,width,img,x,y):
        self.height = height
        self.width = width
        self.img = pygame.image.load(img)
        self.scale = pygame.transform.scale(self.img, (int(width), int(height)))
        self.x = x
        self.y = y
        #Adjust the positions of rectangles surrounding the monsters to give a smoother game play experience
        self.rect = pygame.Rect(x+60,y,width,height)
        
    def move_monster(self):
        """ Describes how the monsters and their encapsulating rectangles move """
        # choose to move left or right
        new_pose = randint(-2,2)
        screen_width_sections = 10
        self.x = self.x + (new_pose*screen_width_sections)
        self.rect.x = self.x
        # move down
        screen_height_sections = 60 
        height_pixel = 480/screen_height_sections # 480 is the total height of the screen set in the execution program
        self.y = self.y + height_pixel    
        self.rect.y = self.y

class Fish:
    """ Encodes the state of the fish in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,width,height+15)
