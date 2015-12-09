# -*- coding: utf-8 -*-
"""
GUI of interactive video game Swim Little Fish Swim

@author: Amanda Sutherland, Ziyu (Selina) Wang

last modified: 12-08-15
"""
import pygame
from pygame.locals import *
import math

class SwimFishView:
    """ A view of swim little fish swim rendered in a Pygame window """
    def __init__(self, model, screen, level, countdown, lives):
        self.model = model
        self.screen = screen
        self.level = level
        self.countdown = countdown
        self.lives = lives

    def draw(self):
        ocean_floor = pygame.image.load('images/ocean.jpg') 
        self.screen.blit(ocean_floor,(0,0))
        # Draws the fish
        points = []
        points.append((self.model.fish.x,self.model.fish.y))
        points.append((self.model.fish.x-20,self.model.fish.y+45))
        points.append((self.model.fish.x+20,self.model.fish.y+45))
        pygame.draw.polygon(self.screen, pygame.Color(self.model.fish.color[0],self.model.fish.color[1],self.model.fish.color[2]),points,0)
        pygame.draw.ellipse(self.screen, pygame.Color(self.model.fish.color[0],self.model.fish.color[1],self.model.fish.color[2]),
        pygame.Rect(self.model.fish.x-self.model.fish.width/2,self.model.fish.y-self.model.fish.height/2,self.model.fish.width,self.model.fish.height),0)
        pygame.draw.circle(self.screen, (0,20,20),(int(self.model.fish.x+self.model.fish.width*0.25),int(self.model.fish.y-self.model.fish.width*0.25)),4,0)
        # Draws the monsters
        for monster in self.model.monsters:
            self.screen.blit(monster.scale,((int(monster.x)),int(monster.y)))
        pygame.draw.rect(self.screen, (175,238,238),(550,0,90,25),0)
        myfont = pygame.font.SysFont("monospace", 16)
        level = myfont.render("Level " + str(self.level), 1, (47,79,79))
        timeleft = myfont.render(str(self.countdown), 1, (47,79,79))
        if self.level < 10:
            self.screen.blit(level, (562, 3))
        if self.level >= 10:
            self.screen.blit(level, (556, 3))
        pygame.draw.rect(self.screen, (175,238,238),(0,0,30,25),0)
        if self.countdown >= 10:
            self.screen.blit(timeleft, (5, 3))
        if self.countdown < 10:
            self.screen.blit(timeleft, (10, 3))
        pygame.draw.rect(self.screen, (175,238,238),(505,455,135,25),0)
        livesleft = myfont.render('Lives left:'+str(self.lives), 1, (47,79,79))
        self.screen.blit(livesleft, (513, 458))
        pygame.display.update()


    def init_screen(self):
        pygame.draw.rect(self.screen, (154,255,154),(0,0,640,480),0)
        myfont = pygame.font.SysFont("monospace", 30)
        welcome = myfont.render("WELCOME TO SWIM LITTLE FISH SWIM!", 1, (47,79,79))
        self.screen.blit(welcome, (30, 210))
        pygame.display.update()

    def rules(self):
        pygame.draw.rect(self.screen, (154,255,154),(0,0,640,480),0)
        myfont = pygame.font.SysFont("monospace", 25)
        rules1 = myfont.render("AVOID the MONSTERS and STAY ALIVE", 1, (47,79,79))
        rules2 = myfont.render("you have 5 lives", 1, (47,79,79))
        rules3 = myfont.render("Each game is 20 seconds", 1, (47,79,79))
        game = myfont.render("your first game starts in 5 seconds", 1, (47,79,79))
        self.screen.blit(rules1, (70, 150))
        self.screen.blit(rules2, (190, 200))
        self.screen.blit(rules3, (140, 250))
        self.screen.blit(game, (65, 300))
        pygame.display.update()

    def eaten(self):
        pygame.draw.rect(self.screen, (255,127,80),(0,0,640,480),0)
        myfont = pygame.font.SysFont("monospace", 25)
        label = myfont.render("YOU GOT EATEN BY A MONSTER!", 1, (47,79,79))
        if self.lives >= 2:
            numlives = myfont.render("You have "+str(self.lives)+" lives left", 1, (47,79,79))
        if self.lives <= 1:
            numlives = myfont.render("You have "+str(self.lives)+" life left", 1, (47,79,79))
        next_game = myfont.render("your next game starts in 3 seconds", 1, (47,79,79))
        self.screen.blit(label, (130, 150))
        self.screen.blit(numlives, (170, 210))
        self.screen.blit(next_game, (70, 270))
        pygame.display.update()


    def level_up(self):
        pygame.draw.rect(self.screen, (175,238,238),(0,0,640,480),0)
        myfont = pygame.font.SysFont("monospace", 30)
        self.model.monsters = []
        label = myfont.render("YOU SURVIVED THE DANGEROUS SEA!", 1, (47,79,79))
        next_game = myfont.render("Level " + str(self.level) + " starts in 3 seconds", 1, (47,79,79))
        self.screen.blit(label, (50, 180))
        self.screen.blit(next_game, (75, 240))
        pygame.display.update()

    def lost(self):
        pygame.draw.rect(self.screen, (255,215,0),(0,0,640,480),0)
        myfont = pygame.font.SysFont("monospace", 30)
        lost = myfont.render("YOU GOT EATEN 5 TIMES!", 1, (47,79,79))
        game_over = myfont.render("GAME OVER", 1, (47,79,79))
        bye = myfont.render("BYE", 1, (47,79,79))
        self.screen.blit(lost, (110, 180))
        self.screen.blit(game_over, (220, 240))
        self.screen.blit(bye, (270, 300))
        pygame.display.update()